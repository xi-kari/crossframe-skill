from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
DEFAULT_SOURCE = Path(r"D:\下载\跨尺度结构解释框架_v6.0.docx")
EXCLUDED_SOURCE_IDS = set()
EXPECTED_INCLUDED_PARAGRAPHS = 3273
REVISION_META_IDS = {f"P{i:04d}" for i in range(3, 30)}
TERM_INDEX_TERMS = [
    "结构域",
    "开放性承担行动",
    "解释准入",
    "工具准入",
    "干涉授权",
    "七闸",
    "五闸十三步",
    "开放断言",
    "命题验证表",
    "强判断八件套",
    "低条件试探行动",
    "权力封闭度",
    "低权力主体保护",
    "观测反身性",
    "过程性产物边界",
    "来源-证据-判断-行动上限",
    "责任链硬规则",
    "T0",
    "T1",
    "T2",
    "T3",
    "T4",
    "不浪费爱原则",
    "反模型殖民",
    "反领域殖民",
    "概念武器化",
    "正当不透明",
    "非文本证据",
    "虚稳态",
    "有序退场",
    "良性消亡",
]


@dataclass(frozen=True)
class Paragraph:
    pid: str
    style: str
    text: str


@dataclass(frozen=True)
class Table:
    tid: str
    source_range: tuple[str, str] | None
    paragraph_ids: list[str]
    rows: list[list[str]]
    cell_paragraph_ids: list[list[list[str]]]


@dataclass(frozen=True)
class Section:
    slug: str
    title: str
    role: str
    start_heading: str | None


SECTIONS = [
    Section(
        "00-source-envelope",
        "V6 Full Source - Source Envelope and Directory",
        "source-envelope",
        None,
    ),
    Section(
        "01-guide",
        "V6 Full Source - Guide",
        "guide",
        "第一部分：极简导读：这套框架解释什么",
    ),
    Section(
        "02-boundary-layer",
        "V6 Full Source - Boundary Layer",
        "boundary-layer",
        "第二部分：边界层：解释对象、适用范围与盲区",
    ),
    Section(
        "03-world-layer",
        "V6 Full Source - World Layer",
        "world-layer",
        "第三部分：世界层：核心概念、根假设与结构动力学",
    ),
    Section(
        "04-state-layer",
        "V6 Full Source - State Layer",
        "state-layer",
        "第四部分：状态层：演化阶段、路径、失稳与恢复",
    ),
    Section(
        "05-interface-layer",
        "V6 Full Source - Interface Layer",
        "interface-layer",
        "第五部分：接口层：从结构解释到现实判断",
    ),
    Section(
        "06-tool-layer",
        "V6 Full Source - Tool Layer",
        "tool-layer",
        "第六部分：工具层：诊断、预判、证据与输出",
    ),
    Section(
        "07-intervention-layer",
        "V6 Full Source - Intervention Layer",
        "intervention-layer",
        "第七部分：干涉层：疗愈、修复、转移与退场",
    ),
    Section(
        "08-application-layer",
        "V6 Full Source - Application Layer",
        "application-layer",
        "第八部分：应用层：关系、组织、平台、制度与公共结构",
    ),
    Section(
        "09-governance-layer",
        "V6 Full Source - Governance Layer",
        "governance-layer",
        "第九部分：治理层：证伪、版本治理、误用防护与替代接口",
    ),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def document_root(source_docx: Path) -> ET.Element:
    with ZipFile(source_docx) as z:
        return ET.fromstring(z.read("word/document.xml"))


def paragraph_text(paragraph: ET.Element) -> str:
    return "".join(t.text or "" for t in paragraph.iter(f"{{{W_NS}}}t"))


def paragraph_style(paragraph: ET.Element) -> str:
    p_pr = paragraph.find(f"{{{W_NS}}}pPr")
    if p_pr is None:
        return ""
    p_style = p_pr.find(f"{{{W_NS}}}pStyle")
    if p_style is None:
        return ""
    return p_style.attrib.get(f"{{{W_NS}}}val", "")


def extract_paragraphs(source_docx: Path) -> list[Paragraph]:
    root = document_root(source_docx)
    paragraphs: list[Paragraph] = []
    for p in root.iter(f"{{{W_NS}}}p"):
        text = paragraph_text(p)
        if not text.strip():
            continue
        paragraphs.append(Paragraph(f"P{len(paragraphs) + 1:04d}", paragraph_style(p), text))
    return [paragraph for paragraph in paragraphs if paragraph.pid not in EXCLUDED_SOURCE_IDS]


def extract_tables(source_docx: Path) -> list[Table]:
    root = document_root(source_docx)
    pid_by_element: dict[int, str] = {}
    paragraph_index = 0
    for paragraph in root.iter(f"{{{W_NS}}}p"):
        if not paragraph_text(paragraph).strip():
            continue
        paragraph_index += 1
        pid_by_element[id(paragraph)] = f"P{paragraph_index:04d}"

    tables: list[Table] = []
    for table_index, table_element in enumerate(root.iter(f"{{{W_NS}}}tbl"), start=1):
        rows: list[list[str]] = []
        cell_paragraph_ids: list[list[list[str]]] = []
        table_paragraph_ids: list[str] = []
        for row_element in table_element.findall(f"{{{W_NS}}}tr"):
            row_cells: list[str] = []
            row_cell_ids: list[list[str]] = []
            for cell_element in row_element.findall(f"{{{W_NS}}}tc"):
                cell_texts: list[str] = []
                cell_ids: list[str] = []
                for paragraph in cell_element.iter(f"{{{W_NS}}}p"):
                    text = paragraph_text(paragraph)
                    if not text.strip():
                        continue
                    pid = pid_by_element[id(paragraph)]
                    cell_texts.append(text)
                    cell_ids.append(pid)
                    table_paragraph_ids.append(pid)
                row_cells.append("<br>".join(cell_texts))
                row_cell_ids.append(cell_ids)
            if row_cells:
                rows.append(row_cells)
                cell_paragraph_ids.append(row_cell_ids)
        if not rows:
            continue
        sorted_ids = sorted(set(table_paragraph_ids), key=lambda pid: int(pid[1:]))
        source_range = (sorted_ids[0], sorted_ids[-1]) if sorted_ids else None
        tables.append(
            Table(
                tid=f"T{table_index:03d}",
                source_range=source_range,
                paragraph_ids=sorted_ids,
                rows=rows,
                cell_paragraph_ids=cell_paragraph_ids,
            )
        )
    return tables


def section_ranges(paragraphs: list[Paragraph]) -> list[tuple[Section, list[Paragraph]]]:
    heading_to_index = {p.text: i for i, p in enumerate(paragraphs)}
    starts: list[int] = [0]
    for section in SECTIONS[1:]:
        if section.start_heading not in heading_to_index:
            raise RuntimeError(f"missing section heading: {section.start_heading}")
        starts.append(heading_to_index[section.start_heading])
    starts.append(len(paragraphs))

    ranges: list[tuple[Section, list[Paragraph]]] = []
    for i, section in enumerate(SECTIONS):
        ranges.append((section, paragraphs[starts[i] : starts[i + 1]]))
    return ranges


def write_section(
    out_dir: Path,
    section: Section,
    paragraphs: list[Paragraph],
    source_docx: Path,
    source_sha: str,
) -> Path:
    path = out_dir / f"{section.slug}.md"
    start = paragraphs[0].pid if paragraphs else "EMPTY"
    end = paragraphs[-1].pid if paragraphs else "EMPTY"
    lines = [
        f"# {section.title}",
        "",
        f"Source docx: `{source_docx}`",
        f"Source SHA256: `{source_sha}`",
        f"Section role: `{section.role}`",
        "Source path is metadata only; validation is based on content hash and paragraph coverage.",
        f"Paragraph range: `{start}`-`{end}`",
        f"Paragraph count: `{len(paragraphs)}`",
        "",
        "This file preserves the extracted source paragraphs verbatim at paragraph level.",
        "Each paragraph is preceded by a stable source id for exact coverage checks.",
        "",
        "## Source Paragraphs",
        "",
    ]
    for paragraph in paragraphs:
        lines.append(f"<!-- source_paragraph:{paragraph.pid} style={paragraph.style} -->")
        lines.append(paragraph.text)
        if paragraph.pid in REVISION_META_IDS:
            lines.append("<!-- source role: revision-meta -->")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def write_index(
    out_dir: Path,
    ranges: list[tuple[Section, list[Paragraph]]],
    source_docx: Path,
    source_sha: str,
    total_chars: int,
    total_non_ws: int,
) -> None:
    lines = [
        "# CrossFrame Max v6 Full Source Index",
        "",
        "`crossframe-max` uses this directory as the full-source primary knowledge base for `跨尺度结构解释框架 v6.0`.",
        "",
        "Runtime rule:",
        "",
        "- Read order may be staged by the active question.",
        "- Final max results require a full-source exhaustive pass across every layered file in this directory.",
        "- Raw full-source files preserve source wording and concept definitions.",
        "- Do not summarize these files as replacement definitions. Cite the paragraph ids and then reason through the full source.",
        "",
        "## Source Metadata",
        "",
        f"- Source docx: `{source_docx}`",
        "- Source path is metadata only; validation is based on content hash and paragraph coverage.",
        f"- Source SHA256: `{source_sha}`",
        f"- Extracted paragraph count: `{sum(len(paragraphs) for _, paragraphs in ranges)}`",
        f"- Extracted text chars: `{total_chars}`",
        f"- Extracted non-whitespace chars: `{total_non_ws}`",
        "- Opening source role: revision-meta for `P0003`-`P0029`; these paragraphs remain part of the full-source corpus.",
        "",
        "## Layered Files",
        "",
        "| file | role | paragraph range | paragraph count |",
        "| --- | --- | --- | --- |",
    ]
    for section, paragraphs in ranges:
        start = paragraphs[0].pid if paragraphs else "EMPTY"
        end = paragraphs[-1].pid if paragraphs else "EMPTY"
        lines.append(
            f"| `{section.slug}.md` | `{section.role}` | `{start}`-`{end}` | `{len(paragraphs)}` |"
        )
    lines.extend(
        [
            "",
            "## Read Strategy",
            "",
            "1. Read this index and create a full-source read ledger.",
            "2. Start with the layer file matching the active question when triage is needed.",
            "3. Read the paragraph ids around the target concept, not only the nearest heading.",
            "4. If a concept crosses layers, read each affected layer file and record all paragraph ids.",
            "5. Before final output, read every layered file listed above and record its paragraph range as completed.",
            "6. Final max artifacts must record the full-source exhaustive pass status and the paragraph ids used for key claims.",
        ]
    )
    (out_dir / "00-index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_heading_index(out_dir: Path, paragraphs: list[Paragraph]) -> None:
    lines = [
        "# CrossFrame Max v6 Heading Index",
        "",
        "This index is generated from source paragraph styles. It is a locator only and never replaces full-source reads.",
        "",
        "| paragraph id | style | text |",
        "| --- | --- | --- |",
    ]
    for paragraph in paragraphs:
        if paragraph.style:
            text = paragraph.text.replace("|", "\\|")
            lines.append(f"| `{paragraph.pid}` | `{paragraph.style}` | {text} |")
    (out_dir / "00-heading-index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_term_index(out_dir: Path, paragraphs: list[Paragraph]) -> None:
    lines = [
        "# CrossFrame Max v6 Term Index",
        "",
        "This generated locator maps high-risk runtime terms to source paragraph ids. It is not a definition layer.",
        "",
        "| term | paragraph ids |",
        "| --- | --- |",
    ]
    for term in TERM_INDEX_TERMS:
        hits = [paragraph.pid for paragraph in paragraphs if term in paragraph.text]
        shown = ", ".join(f"`{pid}`" for pid in hits[:80])
        if len(hits) > 80:
            shown += f", ... ({len(hits)} total)"
        lines.append(f"| {term} | {shown or '未直接命中，需 full-source 检索邻域'} |")
    (out_dir / "00-term-index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>").strip()


def write_table_index(out_dir: Path, tables: list[Table], source_docx: Path, source_sha: str) -> None:
    lines = [
        "# CrossFrame Max v6 Table Index",
        "",
        "This index preserves Word table structure separately from paragraph-level full-source coverage.",
        "Table files do not replace `source_paragraph` reads; they preserve row/cell relations that plain paragraph extraction flattens.",
        "",
        f"Source docx: `{source_docx}`",
        f"Source SHA256: `{source_sha}`",
        f"Extracted table count: `{len(tables)}`",
        "",
        "## Tables",
        "",
        "| table | source paragraph range | paragraph ids | rows | columns | file |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for table in tables:
        source_range = (
            f"`{table.source_range[0]}`-`{table.source_range[1]}`"
            if table.source_range
            else "`EMPTY`"
        )
        column_count = max((len(row) for row in table.rows), default=0)
        paragraph_count = len(table.paragraph_ids)
        lines.append(
            f"| `{table.tid}` | {source_range} | `{paragraph_count}` | `{len(table.rows)}` | `{column_count}` | `tables/{table.tid}.md` |"
        )
    lines.extend(
        [
            "",
            "## Runtime Rule",
            "",
            "- Use table files when a source paragraph belongs to a Word table or when row/cell relations affect meaning.",
            "- Cite both the table id and the original source paragraph ids in final artifacts.",
            "- Full-source exhaustive pass is still measured by `P0001`-`P3273`; table files are structure-preservation companions.",
        ]
    )
    (out_dir / "00-table-index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_tables(out_dir: Path, tables: list[Table], source_docx: Path, source_sha: str) -> None:
    tables_dir = out_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    for table in tables:
        source_range = (
            f"`{table.source_range[0]}`-`{table.source_range[1]}`"
            if table.source_range
            else "`EMPTY`"
        )
        column_count = max((len(row) for row in table.rows), default=0)
        lines = [
            f"# CrossFrame Max v6 Table {table.tid}",
            "",
            f"Source docx: `{source_docx}`",
            f"Source SHA256: `{source_sha}`",
            f"Table id: `{table.tid}`",
            f"Source paragraph range: {source_range}",
            f"Source paragraph ids: {', '.join(f'`{pid}`' for pid in table.paragraph_ids) or '`EMPTY`'}",
            f"Row count: `{len(table.rows)}`",
            f"Column count: `{column_count}`",
            "",
            "This file preserves the Word table row/cell structure. It is a structure companion to the paragraph-level full-source files.",
            "",
            "## Markdown Table",
            "",
        ]
        if column_count:
            header = [f"column {i}" for i in range(1, column_count + 1)]
            lines.append("| " + " | ".join(header) + " |")
            lines.append("| " + " | ".join("---" for _ in header) + " |")
            for row in table.rows:
                padded = row + [""] * (column_count - len(row))
                lines.append("| " + " | ".join(markdown_cell(cell) for cell in padded) + " |")
        lines.extend(["", "## Cell Source Paragraph Ids", ""])
        for row_index, row in enumerate(table.cell_paragraph_ids, start=1):
            for column_index, cell_ids in enumerate(row, start=1):
                shown = ", ".join(f"`{pid}`" for pid in cell_ids) or "`EMPTY`"
                lines.append(f"- R{row_index}C{column_index}: {shown}")
        (tables_dir / f"{table.tid}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_source_manifest(
    max_root: Path,
    source_docx: Path,
    source_sha: str,
    paragraphs: list[Paragraph],
    total_chars: int,
    total_non_ws: int,
    table_count: int,
) -> None:
    raw_paragraphs = len(paragraphs) + len(EXCLUDED_SOURCE_IDS)
    manifest = {
        "framework_version": "v6.0",
        "source_sha256": source_sha,
        "raw_paragraphs": raw_paragraphs,
        "included_paragraphs": len(paragraphs),
        "expected_included_paragraphs": EXPECTED_INCLUDED_PARAGRAPHS,
        "excluded_source_ids": sorted(EXCLUDED_SOURCE_IDS),
        "revision_meta_range": ["P0003", "P0029"],
        "text_chars": total_chars,
        "non_whitespace_chars": total_non_ws,
        "table_count": table_count,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_docx_metadata_path": str(source_docx),
        "source_path_note": "original local path is metadata only, not validation key",
    }
    (max_root / "references" / "source_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def generate(repo: Path, source_docx: Path) -> None:
    source_docx = source_docx.resolve()
    max_root = repo / "skills" / "crossframe-max"
    out_dir = max_root / "references" / "v6-full-source"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    paragraphs = extract_paragraphs(source_docx)
    tables = extract_tables(source_docx)
    if len(paragraphs) != EXPECTED_INCLUDED_PARAGRAPHS:
        raise RuntimeError(f"expected {EXPECTED_INCLUDED_PARAGRAPHS} paragraphs, got {len(paragraphs)}")
    ranges = section_ranges(paragraphs)
    source_sha = sha256(source_docx)
    total_chars = sum(len(p.text) for p in paragraphs)
    total_non_ws = sum(sum(1 for ch in p.text if not ch.isspace()) for p in paragraphs)

    for section, section_paragraphs in ranges:
        write_section(out_dir, section, section_paragraphs, source_docx, source_sha)
    write_index(out_dir, ranges, source_docx, source_sha, total_chars, total_non_ws)
    write_heading_index(out_dir, paragraphs)
    write_term_index(out_dir, paragraphs)
    write_table_index(out_dir, tables, source_docx, source_sha)
    write_tables(out_dir, tables, source_docx, source_sha)
    write_source_manifest(max_root, source_docx, source_sha, paragraphs, total_chars, total_non_ws, len(tables))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the full v6 source knowledge base for crossframe-max.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    parser.add_argument("--source-docx", default=str(DEFAULT_SOURCE), help="Path to the v6 source docx.")
    args = parser.parse_args()
    generate(Path(args.repo).resolve(), Path(args.source_docx))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
