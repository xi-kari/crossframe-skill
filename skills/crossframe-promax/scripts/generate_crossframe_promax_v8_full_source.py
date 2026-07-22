from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from uuid import uuid4
from zipfile import ZipFile
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"

EXPECTED_SOURCE_SHA256 = (
    "3186805a3e46e1b16948a4e51d08e7693a8e0dd04aa6b4604e796266d649936c"
)
EXPECTED_PARAGRAPHS = 3863
EXPECTED_NON_WHITESPACE_CHARS = 155721
EXPECTED_TABLES = 117
EXPECTED_SECTIONS = 16

CANONICAL_PARTS = (
    ("01-guide", "第一部分　导读"),
    ("02-boundary-method", "第二部分　边界与方法"),
    ("03-universal-grammar", "第三部分　通用结构语法"),
    ("04-root-assumptions", "第四部分　根假设与推论"),
    ("05-scale-transformation", "第五部分　跨尺度与跨圈层变换"),
    ("06-operation-evolution", "第六部分　运转与演化"),
    ("07-human-world", "第七部分　人类结构化世界"),
    ("08-human-state-prototype", "第八部分　人类状态原型"),
    ("09-actor-state-personality", "第九部分　行动者状态与人格假设"),
    ("10-multicircle-joint-state", "第十部分　多圈层对象与联合状态"),
    ("11-event-dynamic-deduction", "第十一部分　事件驱动的动态推演"),
    ("12-conditional-forecast-choice", "第十二部分　条件前瞻与有限选择"),
    ("13-interface-tools", "第十三部分　接口与工具"),
    ("14-normative-selection", "第十四部分　规范选择"),
    ("15-intervention-applications", "第十五部分　干涉与应用"),
    ("16-governance", "第十六部分　治理"),
)
CANONICAL_TITLES = tuple(title for _slug, title in CANONICAL_PARTS)


@dataclass(frozen=True)
class V8Paragraph:
    pid: str
    style: str
    text: str


@dataclass(frozen=True)
class V8Table:
    tid: str
    paragraph_ids: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    cell_paragraph_ids: tuple[tuple[tuple[str, ...], ...], ...]


@dataclass(frozen=True)
class V8Section:
    slug: str
    title: str
    start_heading_id: str
    paragraph_ids: tuple[str, ...]
    table_ids: tuple[str, ...]


@dataclass(frozen=True)
class V8Snapshot:
    source_sha256: str
    paragraphs: tuple[V8Paragraph, ...]
    tables: tuple[V8Table, ...]
    sections: tuple[V8Section, ...]
    non_whitespace_chars: int


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_document_xml(source_docx: Path) -> ET.Element:
    with ZipFile(Path(source_docx)) as archive:
        return ET.fromstring(archive.read("word/document.xml"))


def _paragraph_text(element: ET.Element) -> str:
    return "".join(node.text or "" for node in element.iter(f"{W}t"))


def _paragraph_style(element: ET.Element) -> str:
    properties = element.find(f"{W}pPr")
    style = None if properties is None else properties.find(f"{W}pStyle")
    return "" if style is None else style.attrib.get(f"{W}val", "")


def _paragraph_elements(
    document_root: ET.Element,
) -> tuple[tuple[ET.Element, str, str], ...]:
    found: list[tuple[ET.Element, str, str]] = []
    for element in document_root.iter(f"{W}p"):
        text = _paragraph_text(element)
        if text.strip():
            found.append((element, _paragraph_style(element), text))
    return tuple(found)


def extract_v8_paragraphs(document_root: ET.Element) -> tuple[V8Paragraph, ...]:
    return tuple(
        V8Paragraph(f"V8-P{index:04d}", style, text)
        for index, (_element, style, text) in enumerate(
            _paragraph_elements(document_root), start=1
        )
    )


def extract_v8_tables(document_root: ET.Element) -> tuple[V8Table, ...]:
    paragraph_ids = {
        id(element): f"V8-P{index:04d}"
        for index, (element, _style, _text) in enumerate(
            _paragraph_elements(document_root), start=1
        )
    }
    tables: list[V8Table] = []
    for table_index, table_element in enumerate(
        document_root.iter(f"{W}tbl"), start=1
    ):
        rows: list[tuple[str, ...]] = []
        row_cell_ids: list[tuple[tuple[str, ...], ...]] = []
        table_paragraph_ids: list[str] = []
        for row_element in table_element.findall(f"{W}tr"):
            cells: list[str] = []
            cell_ids_for_row: list[tuple[str, ...]] = []
            for cell_element in row_element.findall(f"{W}tc"):
                cell_texts: list[str] = []
                cell_ids: list[str] = []
                for paragraph in cell_element.iter(f"{W}p"):
                    text = _paragraph_text(paragraph)
                    if not text.strip():
                        continue
                    paragraph_id = paragraph_ids[id(paragraph)]
                    cell_texts.append(text)
                    cell_ids.append(paragraph_id)
                    table_paragraph_ids.append(paragraph_id)
                cells.append("\n".join(cell_texts))
                cell_ids_for_row.append(tuple(cell_ids))
            rows.append(tuple(cells))
            row_cell_ids.append(tuple(cell_ids_for_row))
        tables.append(
            V8Table(
                tid=f"V8-T{table_index:03d}",
                paragraph_ids=tuple(table_paragraph_ids),
                rows=tuple(rows),
                cell_paragraph_ids=tuple(row_cell_ids),
            )
        )
    return tuple(tables)


def _anchor_number(anchor: str) -> int:
    return int(anchor.rsplit("P", 1)[1])


def split_v8_sections(
    paragraphs: tuple[V8Paragraph, ...],
    tables: tuple[V8Table, ...],
) -> tuple[V8Section, ...]:
    heading_positions: list[int] = []
    duplicate_titles: list[str] = []
    missing_titles: list[str] = []
    for title in CANONICAL_TITLES:
        matches = [
            index
            for index, paragraph in enumerate(paragraphs)
            if paragraph.style == "1" and paragraph.text == title
        ]
        if len(matches) > 1:
            duplicate_titles.append(title)
        elif not matches:
            missing_titles.append(title)
        else:
            heading_positions.append(matches[0])
    if duplicate_titles:
        raise ValueError(
            "duplicate exact canonical heading: " + ", ".join(duplicate_titles)
        )
    if missing_titles:
        raise ValueError(
            "missing exact canonical heading: " + ", ".join(missing_titles)
        )
    if heading_positions != sorted(heading_positions):
        raise ValueError("canonical heading order does not match the fixed sixteen parts")

    boundaries = heading_positions + [len(paragraphs)]
    sections: list[V8Section] = []
    for part_index, ((slug, title), start) in enumerate(
        zip(CANONICAL_PARTS, heading_positions, strict=True)
    ):
        end = boundaries[part_index + 1]
        section_paragraphs = paragraphs[start:end]
        start_number = _anchor_number(section_paragraphs[0].pid)
        end_number = _anchor_number(section_paragraphs[-1].pid)
        section_table_ids = tuple(
            table.tid
            for table in tables
            if table.paragraph_ids
            and start_number <= _anchor_number(table.paragraph_ids[0]) <= end_number
        )
        sections.append(
            V8Section(
                slug=slug,
                title=title,
                start_heading_id=section_paragraphs[0].pid,
                paragraph_ids=tuple(
                    paragraph.pid for paragraph in section_paragraphs
                ),
                table_ids=section_table_ids,
            )
        )
    return tuple(sections)


def _non_whitespace_count(paragraphs: tuple[V8Paragraph, ...]) -> int:
    return sum(
        not character.isspace()
        for paragraph in paragraphs
        for character in paragraph.text
    )


def validate_v8_snapshot(snapshot: V8Snapshot) -> list[str]:
    errors: list[str] = []
    if snapshot.source_sha256.lower() != EXPECTED_SOURCE_SHA256:
        errors.append(
            "source SHA256 mismatch: "
            f"expected {EXPECTED_SOURCE_SHA256}, got {snapshot.source_sha256}"
        )
    if len(snapshot.paragraphs) != EXPECTED_PARAGRAPHS:
        errors.append(
            f"paragraph count mismatch: expected {EXPECTED_PARAGRAPHS}, "
            f"got {len(snapshot.paragraphs)}"
        )
    expected_paragraph_ids = tuple(
        f"V8-P{index:04d}" for index in range(1, len(snapshot.paragraphs) + 1)
    )
    actual_paragraph_ids = tuple(
        paragraph.pid for paragraph in snapshot.paragraphs
    )
    if actual_paragraph_ids != expected_paragraph_ids:
        errors.append("paragraph anchor sequence is not continuous and unique")

    measured_non_whitespace = _non_whitespace_count(snapshot.paragraphs)
    if snapshot.non_whitespace_chars != measured_non_whitespace:
        errors.append(
            "snapshot non-whitespace character metric does not match paragraph content"
        )
    if measured_non_whitespace != EXPECTED_NON_WHITESPACE_CHARS:
        errors.append(
            "non-whitespace character count mismatch: "
            f"expected {EXPECTED_NON_WHITESPACE_CHARS}, got {measured_non_whitespace}"
        )

    if len(snapshot.tables) != EXPECTED_TABLES:
        errors.append(
            f"table count mismatch: expected {EXPECTED_TABLES}, got {len(snapshot.tables)}"
        )
    expected_table_ids = tuple(
        f"V8-T{index:03d}" for index in range(1, len(snapshot.tables) + 1)
    )
    actual_table_ids = tuple(table.tid for table in snapshot.tables)
    if actual_table_ids != expected_table_ids:
        errors.append("table anchor sequence is not continuous and unique")

    paragraph_text_by_id = {
        paragraph.pid: paragraph.text for paragraph in snapshot.paragraphs
    }
    for table in snapshot.tables:
        flattened_ids = tuple(
            paragraph_id
            for row in table.cell_paragraph_ids
            for cell in row
            for paragraph_id in cell
        )
        if flattened_ids != table.paragraph_ids:
            errors.append(f"{table.tid}: table paragraph anchor binding mismatch")
        if len(table.rows) != len(table.cell_paragraph_ids):
            errors.append(f"{table.tid}: row and cell-anchor shape mismatch")
            continue
        for row_index, (row, cell_ids) in enumerate(
            zip(table.rows, table.cell_paragraph_ids, strict=True), start=1
        ):
            if len(row) != len(cell_ids):
                errors.append(
                    f"{table.tid}: row {row_index} and cell-anchor shape mismatch"
                )
                continue
            for column_index, (cell_text, ids) in enumerate(
                zip(row, cell_ids, strict=True), start=1
            ):
                if any(paragraph_id not in paragraph_text_by_id for paragraph_id in ids):
                    errors.append(
                        f"{table.tid}: R{row_index}C{column_index} has unknown paragraph anchor"
                    )
                    continue
                expected_text = "\n".join(
                    paragraph_text_by_id[paragraph_id] for paragraph_id in ids
                )
                if cell_text != expected_text:
                    errors.append(
                        f"{table.tid}: R{row_index}C{column_index} text does not match bound paragraphs"
                    )

    if len(snapshot.sections) != EXPECTED_SECTIONS:
        errors.append(
            f"section count mismatch: expected {EXPECTED_SECTIONS}, "
            f"got {len(snapshot.sections)}"
        )
    try:
        expected_sections = split_v8_sections(snapshot.paragraphs, snapshot.tables)
    except ValueError as error:
        errors.append(str(error))
    else:
        if snapshot.sections != expected_sections:
            errors.append("section boundaries or table bindings do not match source anchors")
    return list(dict.fromkeys(errors))


def _source_file_lines(
    title: str,
    role: str,
    paragraphs: tuple[V8Paragraph, ...],
    source_sha256: str,
) -> list[str]:
    start = paragraphs[0].pid if paragraphs else "EMPTY"
    end = paragraphs[-1].pid if paragraphs else "EMPTY"
    lines = [
        f"# {title}",
        "",
        f"Source SHA256: `{source_sha256}`",
        f"Source role: `{role}`",
        f"Paragraph range: `{start}`-`{end}`",
        f"Paragraph count: `{len(paragraphs)}`",
        "",
        "## Source Paragraphs",
        "",
    ]
    for paragraph in paragraphs:
        lines.extend(
            [
                f"<!-- source_paragraph:{paragraph.pid} style={paragraph.style} -->",
                paragraph.text,
                "",
            ]
        )
    return lines


def _markdown_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", "<br>").strip()


def _write_text(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def _render_table(
    table: V8Table, source_sha256: str, output_path: Path
) -> None:
    columns = max((len(row) for row in table.rows), default=0)
    lines = [
        f"# CrossFrame ProMax v8 Table {table.tid}",
        "",
        f"Source SHA256: `{source_sha256}`",
        f"Table ID: `{table.tid}`",
        "Source paragraph IDs: "
        + (", ".join(f"`{pid}`" for pid in table.paragraph_ids) or "`EMPTY`"),
        f"Row count: `{len(table.rows)}`",
        f"Column count: `{columns}`",
        "",
        "## Rows",
        "",
    ]
    if columns:
        lines.append("| " + " | ".join(f"column {index}" for index in range(1, columns + 1)) + " |")
        lines.append("| " + " | ".join("---" for _ in range(columns)) + " |")
        for row in table.rows:
            padded = row + ("",) * (columns - len(row))
            lines.append("| " + " | ".join(_markdown_cell(cell) for cell in padded) + " |")
    lines.extend(["", "## Cell Paragraph IDs", ""])
    for row_index, row in enumerate(table.cell_paragraph_ids, start=1):
        for column_index, cell_ids in enumerate(row, start=1):
            value = ", ".join(f"`{pid}`" for pid in cell_ids) or "`EMPTY`"
            lines.append(f"- R{row_index}C{column_index}: {value}")
    lines.extend(
        [
            "",
            "## Canonical Structure",
            "",
            "```json",
            json.dumps(
                {
                    "tid": table.tid,
                    "paragraph_ids": table.paragraph_ids,
                    "rows": table.rows,
                    "cell_paragraph_ids": table.cell_paragraph_ids,
                },
                ensure_ascii=False,
                indent=2,
            ),
            "```",
        ]
    )
    _write_text(output_path, lines)


def render_v8_source_tree(snapshot: V8Snapshot, output_dir: Path) -> None:
    errors = validate_v8_snapshot(snapshot)
    if errors:
        raise ValueError("invalid v8 snapshot: " + "; ".join(errors))
    output_dir = Path(output_dir)
    if output_dir.exists():
        if not output_dir.is_dir() or any(output_dir.iterdir()):
            raise ValueError(f"render target must be an empty directory: {output_dir}")
    else:
        output_dir.mkdir(parents=True)
    paragraph_by_id = {
        paragraph.pid: paragraph for paragraph in snapshot.paragraphs
    }
    first_section_start = _anchor_number(snapshot.sections[0].start_heading_id)
    envelope = snapshot.paragraphs[: first_section_start - 1]
    _write_text(
        output_dir / "00-source-envelope.md",
        _source_file_lines(
            "CrossFrame ProMax v8 Source Envelope",
            "source-envelope",
            envelope,
            snapshot.source_sha256,
        ),
    )
    for section in snapshot.sections:
        section_paragraphs = tuple(
            paragraph_by_id[paragraph_id] for paragraph_id in section.paragraph_ids
        )
        _write_text(
            output_dir / f"{section.slug}.md",
            _source_file_lines(
                section.title,
                section.slug,
                section_paragraphs,
                snapshot.source_sha256,
            ),
        )

    index_lines = [
        "# CrossFrame ProMax v8 Full Source Index",
        "",
        f"Source SHA256: `{snapshot.source_sha256}`",
        f"Paragraph count: `{len(snapshot.paragraphs)}`",
        f"Non-whitespace characters: `{snapshot.non_whitespace_chars}`",
        f"Table count: `{len(snapshot.tables)}`",
        f"Section count: `{len(snapshot.sections)}`",
        "",
        "| file | title | paragraph range | paragraph count | tables |",
        "| --- | --- | --- | --- | --- |",
    ]
    envelope_range = (
        f"{envelope[0].pid}-{envelope[-1].pid}" if envelope else "EMPTY"
    )
    index_lines.append(
        f"| `00-source-envelope.md` | Source envelope | `{envelope_range}` | "
        f"`{len(envelope)}` | |"
    )
    for section in snapshot.sections:
        table_ids = ", ".join(section.table_ids)
        index_lines.append(
            f"| `{section.slug}.md` | {section.title} | "
            f"`{section.paragraph_ids[0]}-{section.paragraph_ids[-1]}` | "
            f"`{len(section.paragraph_ids)}` | {table_ids} |"
        )
    _write_text(output_dir / "00-index.md", index_lines)

    heading_lines = [
        "# CrossFrame ProMax v8 Heading Index",
        "",
        "| paragraph id | style | text |",
        "| --- | --- | --- |",
    ]
    for paragraph in snapshot.paragraphs:
        if paragraph.style:
            heading_lines.append(
                f"| `{paragraph.pid}` | `{paragraph.style}` | "
                f"{_markdown_cell(paragraph.text)} |"
            )
    _write_text(output_dir / "00-heading-index.md", heading_lines)

    _write_text(
        output_dir / "00-term-index.md",
        [
            "# CrossFrame ProMax v8 Term Index",
            "",
            f"Source SHA256: `{snapshot.source_sha256}`",
            "",
            "Use exact source anchors and full-text search; this locator does not replace source reads.",
        ],
    )

    table_index_lines = [
        "# CrossFrame ProMax v8 Table Index",
        "",
        f"Source SHA256: `{snapshot.source_sha256}`",
        f"Table count: `{len(snapshot.tables)}`",
        "",
        "| table | paragraph ids | rows | columns | file |",
        "| --- | --- | --- | --- | --- |",
    ]
    for table in snapshot.tables:
        columns = max((len(row) for row in table.rows), default=0)
        table_index_lines.append(
            f"| `{table.tid}` | `{len(table.paragraph_ids)}` | "
            f"`{len(table.rows)}` | `{columns}` | `tables/{table.tid}.md` |"
        )
        _render_table(
            table,
            snapshot.source_sha256,
            output_dir / "tables" / f"{table.tid}.md",
        )
    _write_text(output_dir / "00-table-index.md", table_index_lines)


def _tree_bytes(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def validate_generated_v8_tree(
    generated_dir: Path, snapshot: V8Snapshot
) -> list[str]:
    snapshot_errors = validate_v8_snapshot(snapshot)
    if snapshot_errors:
        return [f"snapshot: {error}" for error in snapshot_errors]
    generated_dir = Path(generated_dir)
    if not generated_dir.is_dir():
        return [f"generated source tree does not exist: {generated_dir}"]
    with tempfile.TemporaryDirectory() as directory:
        expected_dir = Path(directory) / "expected"
        render_v8_source_tree(snapshot, expected_dir)
        expected = _tree_bytes(expected_dir)
    actual = _tree_bytes(generated_dir)
    errors: list[str] = []
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    if missing:
        errors.append("missing generated files: " + ", ".join(missing))
    if extra:
        errors.append("unexpected generated files: " + ", ".join(extra))
    for relative_path in sorted(set(expected) & set(actual)):
        if actual[relative_path] != expected[relative_path]:
            errors.append(f"content mismatch: {relative_path}")
    return errors


def _remove_tree(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def atomic_replace_tree(stage_dir: Path, live_dir: Path) -> None:
    stage_dir = Path(stage_dir)
    live_dir = Path(live_dir)
    if not stage_dir.is_dir():
        raise ValueError(f"stage directory does not exist: {stage_dir}")
    if stage_dir.parent.resolve() != live_dir.parent.resolve():
        raise ValueError("stage and live directories must have the same parent")
    backup = live_dir.parent / f".{live_dir.name}.backup-{uuid4().hex}"
    backup_created = False
    try:
        if live_dir.exists():
            os.replace(live_dir, backup)
            backup_created = True
        os.replace(stage_dir, live_dir)
    except BaseException:
        if live_dir.exists():
            _remove_tree(live_dir)
        if backup_created and backup.exists():
            os.replace(backup, live_dir)
            backup_created = False
        if stage_dir.exists():
            _remove_tree(stage_dir)
        if backup.exists():
            _remove_tree(backup)
        raise
    if backup_created and backup.exists():
        _remove_tree(backup)


def generate(repo: Path, source_docx: Path) -> Path:
    repo = Path(repo).resolve()
    source_docx = Path(source_docx).resolve()
    source_sha256 = sha256_file(source_docx)
    if source_sha256 != EXPECTED_SOURCE_SHA256:
        raise ValueError(
            "source SHA256 mismatch: "
            f"expected {EXPECTED_SOURCE_SHA256}, got {source_sha256}"
        )
    document_root = read_document_xml(source_docx)
    paragraphs = extract_v8_paragraphs(document_root)
    tables = extract_v8_tables(document_root)
    sections = split_v8_sections(paragraphs, tables)
    snapshot = V8Snapshot(
        source_sha256=source_sha256,
        paragraphs=paragraphs,
        tables=tables,
        sections=sections,
        non_whitespace_chars=_non_whitespace_count(paragraphs),
    )
    snapshot_errors = validate_v8_snapshot(snapshot)
    if snapshot_errors:
        raise ValueError("invalid v8 source snapshot: " + "; ".join(snapshot_errors))

    live_dir = repo / "skills/crossframe-promax/references/v8-full-source"
    live_dir.parent.mkdir(parents=True, exist_ok=True)
    stage_dir = Path(
        tempfile.mkdtemp(
            prefix=f".{live_dir.name}.stage-",
            dir=live_dir.parent,
        )
    )
    try:
        render_v8_source_tree(snapshot, stage_dir)
        generated_errors = validate_generated_v8_tree(stage_dir, snapshot)
        if generated_errors:
            raise ValueError(
                "generated v8 source validation failed: "
                + "; ".join(generated_errors)
            )
        atomic_replace_tree(stage_dir, live_dir)
    finally:
        if stage_dir.exists():
            _remove_tree(stage_dir)
    return live_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate the CrossFrame ProMax v8 full-source tree safely."
    )
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--source-docx", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output = generate(args.repo, args.source_docx)
    except (OSError, ValueError, ET.ParseError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"generated v8 full source: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
