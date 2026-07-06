from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
DEFAULT_SOURCE = Path(r"D:\下载\跨尺度结构解释框架_v6.0.docx")
SOURCE_RE = re.compile(r"^<!-- source_paragraph:(P\d{4}) style=([^>]*) -->$")
EXCLUDED_SOURCE_IDS = set()
EXPECTED_INCLUDED_PARAGRAPHS = 3273
GENERATED_INDEX_FILES = {"00-index.md", "00-heading-index.md", "00-term-index.md", "00-table-index.md"}


@dataclass(frozen=True)
class Paragraph:
    pid: str
    style: str
    text: str


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_paragraphs(source_docx: Path) -> list[Paragraph]:
    with ZipFile(source_docx) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    paragraphs: list[Paragraph] = []
    for p in root.iter(f"{{{W_NS}}}p"):
        text = "".join(t.text or "" for t in p.iter(f"{{{W_NS}}}t"))
        if not text.strip():
            continue
        p_pr = p.find(f"{{{W_NS}}}pPr")
        style = ""
        if p_pr is not None:
            p_style = p_pr.find(f"{{{W_NS}}}pStyle")
            if p_style is not None:
                style = p_style.attrib.get(f"{{{W_NS}}}val", "")
        paragraphs.append(Paragraph(f"P{len(paragraphs) + 1:04d}", style, text))
    return [paragraph for paragraph in paragraphs if paragraph.pid not in EXCLUDED_SOURCE_IDS]


def extract_table_count(source_docx: Path) -> int:
    with ZipFile(source_docx) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    return sum(1 for _ in root.iter(f"{{{W_NS}}}tbl"))


def read_generated(source_dir: Path) -> list[Paragraph]:
    paragraphs: list[Paragraph] = []
    files = sorted(
        p
        for p in source_dir.glob("*.md")
        if p.name not in GENERATED_INDEX_FILES
    )
    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            match = SOURCE_RE.match(lines[i])
            if not match:
                i += 1
                continue
            pid, style = match.groups()
            if i + 1 >= len(lines):
                raise SystemExit(f"{path}: missing text after {pid}")
            paragraphs.append(Paragraph(pid, style, lines[i + 1]))
            i += 2
    return paragraphs


def read_manifest(repo: Path) -> dict:
    manifest_path = repo / "skills" / "crossframe-max" / "references" / "source_manifest.json"
    if not manifest_path.exists():
        raise SystemExit(f"missing source_manifest.json: {manifest_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def check_generated_index(repo: Path, source_dir: Path, actual: list[Paragraph], manifest: dict) -> None:
    index = source_dir / "00-index.md"
    if not index.exists():
        raise SystemExit(f"missing full-source index: {index}")
    heading_index = source_dir / "00-heading-index.md"
    term_index = source_dir / "00-term-index.md"
    table_index = source_dir / "00-table-index.md"
    if not heading_index.exists():
        raise SystemExit(f"missing generated heading index: {heading_index}")
    if not term_index.exists():
        raise SystemExit(f"missing generated term index: {term_index}")
    if not table_index.exists():
        raise SystemExit(f"missing generated table index: {table_index}")
    tables_dir = source_dir / "tables"
    if not tables_dir.is_dir():
        raise SystemExit(f"missing generated tables directory: {tables_dir}")

    if len(actual) != EXPECTED_INCLUDED_PARAGRAPHS:
        raise SystemExit(f"paragraph count mismatch: expected {EXPECTED_INCLUDED_PARAGRAPHS}, got {len(actual)}")

    expected_ids = [f"P{i:04d}" for i in range(1, EXPECTED_INCLUDED_PARAGRAPHS + 1)]
    actual_ids = [paragraph.pid for paragraph in actual]
    if actual_ids != expected_ids:
        raise SystemExit("generated paragraph ids are not a complete continuous P0001-P3273 range")

    leaked = sorted(set(actual_ids) & EXCLUDED_SOURCE_IDS)
    if leaked:
        raise SystemExit(f"unexpected excluded source ids configured but present: {', '.join(leaked)}")

    if manifest.get("included_paragraphs") != EXPECTED_INCLUDED_PARAGRAPHS:
        raise SystemExit("source_manifest.json included_paragraphs mismatch")
    if manifest.get("source_path_note") != "original local path is metadata only, not validation key":
        raise SystemExit("source_manifest.json must declare source path is metadata only")
    if not isinstance(manifest.get("table_count"), int):
        raise SystemExit("source_manifest.json table_count must be an integer")

    index_text = index.read_text(encoding="utf-8")
    required_markers = [
        "CrossFrame Max v6 Full Source Index",
        "Source path is metadata only",
        f"Extracted paragraph count: `{EXPECTED_INCLUDED_PARAGRAPHS}`",
        "source role: revision-meta",
        "Raw full-source files preserve source wording",
        "Final max results require a full-source exhaustive pass",
        "Before final output, read every layered file listed above",
    ]
    for marker in required_markers:
        if marker not in index_text:
            raise SystemExit(f"index missing marker: {marker}")

    table_index_text = table_index.read_text(encoding="utf-8")
    table_markers = [
        "CrossFrame Max v6 Table Index",
        "preserves Word table structure separately",
        "Extracted table count:",
        "Full-source exhaustive pass is still measured by `P0001`-`P3273`",
    ]
    for marker in table_markers:
        if marker not in table_index_text:
            raise SystemExit(f"table index missing marker: {marker}")

    table_files = sorted(tables_dir.glob("T*.md"))
    if len(table_files) != manifest["table_count"]:
        raise SystemExit(
            f"generated table count mismatch: manifest={manifest['table_count']}, files={len(table_files)}"
        )
    for path in table_files:
        text = path.read_text(encoding="utf-8")
        for marker in ["CrossFrame Max v6 Table", "Source paragraph range:", "Cell Source Paragraph Ids"]:
            if marker not in text:
                raise SystemExit(f"{path}: missing table marker: {marker}")


def check(repo: Path, source_docx: Path | None, allow_source_path_mismatch: bool) -> None:
    source_dir = repo / "skills" / "crossframe-max" / "references" / "v6-full-source"
    if not source_dir.is_dir():
        raise SystemExit(f"missing full-source directory: {source_dir}")
    manifest = read_manifest(repo)
    actual = read_generated(source_dir)
    check_generated_index(repo, source_dir, actual, manifest)

    source_sha = manifest["source_sha256"]
    if source_docx is None:
        total_chars = sum(len(p.text) for p in actual)
        total_non_ws = sum(sum(1 for ch in p.text if not ch.isspace()) for p in actual)
        print(f"ok: full source paragraphs={len(actual)} chars={total_chars} non_ws={total_non_ws}")
        print(f"ok: source sha256={source_sha}")
        print("ok: source path is metadata only; no source docx was required for generated coverage check")
        return

    source_docx = source_docx.resolve()
    expected = extract_paragraphs(source_docx)
    if len(expected) != EXPECTED_INCLUDED_PARAGRAPHS:
        raise SystemExit(f"source docx paragraph count mismatch: expected {EXPECTED_INCLUDED_PARAGRAPHS}, got {len(expected)}")

    for expected_paragraph, actual_paragraph in zip(expected, actual):
        if expected_paragraph != actual_paragraph:
            raise SystemExit(
                "paragraph mismatch: "
                f"expected {expected_paragraph.pid}/{expected_paragraph.style}/{expected_paragraph.text[:80]!r}, "
                f"got {actual_paragraph.pid}/{actual_paragraph.style}/{actual_paragraph.text[:80]!r}"
            )

    actual_sha = sha256(source_docx)
    if actual_sha != source_sha:
        raise SystemExit(f"source sha256 mismatch: manifest={source_sha}, source_docx={actual_sha}")
    source_table_count = extract_table_count(source_docx)
    if source_table_count != manifest.get("table_count"):
        raise SystemExit(
            f"source table count mismatch: manifest={manifest.get('table_count')}, source_docx={source_table_count}"
        )

    total_chars = sum(len(p.text) for p in actual)
    total_non_ws = sum(sum(1 for ch in p.text if not ch.isspace()) for p in actual)
    print(f"ok: full source paragraphs={len(actual)} chars={total_chars} non_ws={total_non_ws}")
    print(f"ok: source sha256={actual_sha}")
    if allow_source_path_mismatch:
        print("ok: --allow-source-path-mismatch accepted; source path is metadata only")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check crossframe-max v6 full-source coverage.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    parser.add_argument("--source-docx", default=None, help="Optional path to the v6 source docx for content comparison.")
    parser.add_argument(
        "--allow-source-path-mismatch",
        action="store_true",
        help="Accept a source docx path different from the metadata path; source path is metadata only.",
    )
    args = parser.parse_args()
    source_docx = Path(args.source_docx) if args.source_docx else (DEFAULT_SOURCE if DEFAULT_SOURCE.exists() else None)
    check(Path(args.repo).resolve(), source_docx, args.allow_source_path_mismatch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
