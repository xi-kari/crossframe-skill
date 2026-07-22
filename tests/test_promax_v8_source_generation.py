from __future__ import annotations

from dataclasses import replace
import importlib.util
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
from zipfile import ZIP_DEFLATED, ZipFile
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_XML = ROOT / "tests/fixtures/promax-v8-source/document.xml"
GENERATOR_PATH = (
    ROOT
    / "skills/crossframe-promax/scripts/generate_crossframe_promax_v8_full_source.py"
)
REAL_SOURCE = Path(r"E:\世界模型\跨尺度多圈层结构推演框架_v8.0.docx")

if not GENERATOR_PATH.is_file():
    raise ModuleNotFoundError(
        "CrossFrame ProMax v8 source generator has not been implemented"
    )
spec = importlib.util.spec_from_file_location("promax_v8_source_generator", GENERATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load generator module: {GENERATOR_PATH}")
generator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = generator
spec.loader.exec_module(generator)


def write_fixture_docx(path: Path, xml_bytes: bytes | None = None) -> None:
    payload = FIXTURE_XML.read_bytes() if xml_bytes is None else xml_bytes
    with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
        archive.writestr("word/document.xml", payload)


def fixture_root() -> ET.Element:
    return ET.fromstring(FIXTURE_XML.read_bytes())


def non_whitespace(text: str) -> int:
    return sum(not character.isspace() for character in text)


def valid_release_snapshot():
    paragraphs = [
        generator.V8Paragraph(f"V8-P{index:04d}", "", "x")
        for index in range(1, generator.EXPECTED_PARAGRAPHS + 1)
    ]
    heading_indexes = [index * 100 for index in range(generator.EXPECTED_SECTIONS)]
    for heading_index, title in zip(
        heading_indexes, generator.CANONICAL_TITLES, strict=True
    ):
        paragraphs[heading_index] = replace(
            paragraphs[heading_index], style="1", text=title
        )

    for index, text in zip(range(2000, 2004), ("a", "b", "c", "d"), strict=True):
        paragraphs[index] = replace(paragraphs[index], text=text)

    current_non_ws = sum(non_whitespace(paragraph.text) for paragraph in paragraphs)
    padding = generator.EXPECTED_NON_WHITESPACE_CHARS - current_non_ws
    if padding < 0:
        raise AssertionError("synthetic snapshot unexpectedly exceeds release character count")
    paragraphs[-1] = replace(paragraphs[-1], text="x" * (padding + 1))
    paragraph_tuple = tuple(paragraphs)

    tables = [
        generator.V8Table(
            tid="V8-T001",
            paragraph_ids=("V8-P2001", "V8-P2002", "V8-P2003", "V8-P2004"),
            rows=(("a", "b"), ("c", "d")),
            cell_paragraph_ids=(
                (("V8-P2001",), ("V8-P2002",)),
                (("V8-P2003",), ("V8-P2004",)),
            ),
        )
    ]
    for table_index in range(2, generator.EXPECTED_TABLES + 1):
        paragraph_id = f"V8-P{2100 + table_index:04d}"
        tables.append(
            generator.V8Table(
                tid=f"V8-T{table_index:03d}",
                paragraph_ids=(paragraph_id,),
                rows=(("x",),),
                cell_paragraph_ids=(((paragraph_id,),),),
            )
        )
    table_tuple = tuple(tables)
    sections = generator.split_v8_sections(paragraph_tuple, table_tuple)
    return generator.V8Snapshot(
        source_sha256=generator.EXPECTED_SOURCE_SHA256,
        paragraphs=paragraph_tuple,
        tables=table_tuple,
        sections=sections,
        non_whitespace_chars=generator.EXPECTED_NON_WHITESPACE_CHARS,
    )


class V8XmlExtractionTests(unittest.TestCase):
    def test_read_document_xml_reads_the_ooxml_body(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "fixture.docx"
            write_fixture_docx(source)
            root = generator.read_document_xml(source)
        self.assertTrue(root.tag.endswith("}document"))

    def test_extract_paragraphs_walks_table_cells_in_document_order(self) -> None:
        paragraphs = generator.extract_v8_paragraphs(fixture_root())
        self.assertEqual(
            [paragraph.text for paragraph in paragraphs[:10]],
            [
                "封面",
                "第一部分　导读",
                "第一部分　导读",
                "导读正文",
                "A1",
                "A2",
                "B1",
                "B2",
                "第二部分　边界与方法",
                "第二部分正文",
            ],
        )
        self.assertEqual(
            [paragraph.pid for paragraph in paragraphs],
            [f"V8-P{index:04d}" for index in range(1, len(paragraphs) + 1)],
        )

    def test_extract_tables_preserves_rows_cells_and_source_bindings(self) -> None:
        tables = generator.extract_v8_tables(fixture_root())
        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0].tid, "V8-T001")
        self.assertEqual(tables[0].paragraph_ids, tuple(f"V8-P{i:04d}" for i in range(5, 9)))
        self.assertEqual(tables[0].rows, (("A1", "A2"), ("B1", "B2")))
        self.assertEqual(
            tables[0].cell_paragraph_ids,
            (
                (("V8-P0005",), ("V8-P0006",)),
                (("V8-P0007",), ("V8-P0008",)),
            ),
        )

    def test_split_sections_ignores_same_named_toc1_and_uses_exact_style1(self) -> None:
        paragraphs = generator.extract_v8_paragraphs(fixture_root())
        tables = generator.extract_v8_tables(fixture_root())
        sections = generator.split_v8_sections(paragraphs, tables)
        self.assertEqual(len(sections), 16)
        self.assertEqual(sections[0].start_heading_id, "V8-P0003")
        self.assertEqual(sections[0].paragraph_ids, tuple(f"V8-P{i:04d}" for i in range(3, 9)))
        self.assertEqual(sections[0].table_ids, ("V8-T001",))
        self.assertEqual(sections[1].start_heading_id, "V8-P0009")

    def test_split_sections_rejects_missing_duplicate_and_reordered_titles(self) -> None:
        paragraphs = list(generator.extract_v8_paragraphs(fixture_root()))
        tables = generator.extract_v8_tables(fixture_root())
        title_positions = [
            index
            for index, paragraph in enumerate(paragraphs)
            if paragraph.style == "1" and paragraph.text in generator.CANONICAL_TITLES
        ]

        cases = {}
        missing = paragraphs.copy()
        missing[title_positions[-1]] = replace(missing[title_positions[-1]], style="")
        cases["missing"] = missing
        duplicate = paragraphs.copy()
        duplicate[title_positions[-1]] = replace(
            duplicate[title_positions[-1]], text=generator.CANONICAL_TITLES[0]
        )
        cases["duplicate"] = duplicate
        reordered = paragraphs.copy()
        first, second = title_positions[:2]
        reordered[first] = replace(reordered[first], text=generator.CANONICAL_TITLES[1])
        reordered[second] = replace(reordered[second], text=generator.CANONICAL_TITLES[0])
        cases["order"] = reordered
        ascii_space = paragraphs.copy()
        ascii_space[first] = replace(
            ascii_space[first], text=generator.CANONICAL_TITLES[0].replace("　", " ")
        )
        cases["exact"] = ascii_space

        for label, candidate in cases.items():
            with self.subTest(label=label), self.assertRaisesRegex(ValueError, label):
                generator.split_v8_sections(tuple(candidate), tables)


class V8SnapshotValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.snapshot = valid_release_snapshot()

    def test_release_constants_and_valid_snapshot_are_exact(self) -> None:
        self.assertEqual(
            generator.EXPECTED_SOURCE_SHA256,
            "3186805a3e46e1b16948a4e51d08e7693a8e0dd04aa6b4604e796266d649936c",
        )
        self.assertEqual(generator.EXPECTED_PARAGRAPHS, 3863)
        self.assertEqual(generator.EXPECTED_NON_WHITESPACE_CHARS, 155721)
        self.assertEqual(generator.EXPECTED_TABLES, 117)
        self.assertEqual(generator.EXPECTED_SECTIONS, 16)
        self.assertEqual(generator.validate_v8_snapshot(self.snapshot), [])

    def test_validate_snapshot_rejects_wrong_sha(self) -> None:
        errors = generator.validate_v8_snapshot(
            replace(self.snapshot, source_sha256="0" * 64)
        )
        self.assertTrue(any("SHA256" in error for error in errors), errors)

    def test_validate_snapshot_rejects_deleted_and_duplicate_paragraph_anchors(self) -> None:
        for label, replacement_id in (
            ("deleted", "V8-P9999"),
            ("duplicate", self.snapshot.paragraphs[0].pid),
        ):
            paragraphs = list(self.snapshot.paragraphs)
            paragraphs[1] = replace(paragraphs[1], pid=replacement_id)
            candidate = replace(self.snapshot, paragraphs=tuple(paragraphs))
            with self.subTest(label=label):
                errors = generator.validate_v8_snapshot(candidate)
                self.assertTrue(any("anchor" in error for error in errors), errors)


class V8GeneratedTreeValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.snapshot = valid_release_snapshot()

    def render(self, root: Path) -> Path:
        stage = root / "v8-full-source"
        generator.render_v8_source_tree(self.snapshot, stage)
        self.assertEqual(generator.validate_generated_v8_tree(stage, self.snapshot), [])
        return stage

    def test_changed_character_with_same_count_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            stage = self.render(Path(directory))
            source_file = stage / "16-governance.md"
            original = source_file.read_text(encoding="utf-8")
            changed = original.replace("\nx\n\n", "\ny\n\n", 1)
            self.assertNotEqual(changed, original)
            source_file.write_text(changed, encoding="utf-8", newline="\n")
            errors = generator.validate_generated_v8_tree(stage, self.snapshot)
        self.assertTrue(any("content mismatch" in error for error in errors), errors)

    def test_deleted_and_duplicate_generated_anchors_are_rejected(self) -> None:
        marker = "<!-- source_paragraph:V8-P1502 style= -->"
        for label, replacement in (("deleted", ""), ("duplicate", f"{marker}\n{marker}")):
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                stage = self.render(Path(directory))
                source_file = stage / "16-governance.md"
                original = source_file.read_text(encoding="utf-8")
                self.assertIn(marker, original)
                source_file.write_text(
                    original.replace(marker, replacement, 1),
                    encoding="utf-8",
                    newline="\n",
                )
                errors = generator.validate_generated_v8_tree(stage, self.snapshot)
                self.assertTrue(any("content mismatch" in error for error in errors), errors)

    def test_table_cell_mutation_and_row_exchange_are_rejected(self) -> None:
        mutations = (
            ("cell", "| a | b |", "| z | b |"),
            ("rows", "| a | b |\n| c | d |", "| c | d |\n| a | b |"),
        )
        for label, old, new in mutations:
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                stage = self.render(Path(directory))
                table_file = stage / "tables/V8-T001.md"
                original = table_file.read_text(encoding="utf-8")
                self.assertIn(old, original)
                table_file.write_text(
                    original.replace(old, new, 1),
                    encoding="utf-8",
                    newline="\n",
                )
                errors = generator.validate_generated_v8_tree(stage, self.snapshot)
                self.assertTrue(any("content mismatch" in error for error in errors), errors)


class V8GenerationSafetyTests(unittest.TestCase):
    def test_real_source_sha_matches_frozen_constant_when_source_is_available(self) -> None:
        if not REAL_SOURCE.is_file():
            self.skipTest(f"real v8 source is unavailable: {REAL_SOURCE}")
        self.assertEqual(generator.sha256_file(REAL_SOURCE), generator.EXPECTED_SOURCE_SHA256)

    def test_prevalidation_failure_preserves_existing_live_tree(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            live = repo / "skills/crossframe-promax/references/v8-full-source"
            live.mkdir(parents=True)
            sentinel = live / "sentinel.txt"
            sentinel.write_text("keep-me", encoding="utf-8")
            source = root / "fixture.docx"
            write_fixture_docx(source)
            fixture_sha = generator.sha256_file(source)
            with mock.patch.object(generator, "EXPECTED_SOURCE_SHA256", fixture_sha):
                with self.assertRaisesRegex(ValueError, "paragraph count"):
                    generator.generate(repo, source)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep-me")
            self.assertEqual(
                list(live.parent.glob(f".{live.name}.stage-*")),
                [],
            )

    def test_wrong_sha_fails_before_touching_live_tree(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            live = repo / "skills/crossframe-promax/references/v8-full-source"
            live.mkdir(parents=True)
            sentinel = live / "sentinel.txt"
            sentinel.write_text("keep-me", encoding="utf-8")
            source = root / "fixture.docx"
            write_fixture_docx(source)
            with self.assertRaisesRegex(ValueError, "SHA256"):
                generator.generate(repo, source)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep-me")

    def test_atomic_replace_restores_live_tree_and_cleans_stage_on_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            live = parent / "v8-full-source"
            stage = parent / ".v8-full-source.stage-test"
            live.mkdir()
            stage.mkdir()
            (live / "sentinel.txt").write_text("old", encoding="utf-8")
            (stage / "new.txt").write_text("new", encoding="utf-8")
            real_replace = os.replace
            calls = 0

            def fail_install(source: os.PathLike[str], target: os.PathLike[str]) -> None:
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("injected install failure")
                real_replace(source, target)

            with mock.patch.object(generator.os, "replace", side_effect=fail_install):
                with self.assertRaisesRegex(OSError, "injected install failure"):
                    generator.atomic_replace_tree(stage, live)
            self.assertEqual((live / "sentinel.txt").read_text(encoding="utf-8"), "old")
            self.assertFalse(stage.exists())
            self.assertEqual(list(parent.glob(".v8-full-source.backup-*")), [])


if __name__ == "__main__":
    unittest.main()
