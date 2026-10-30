#!/usr/bin/env python3
"""
Convert a worksheet pack written in plain markdown to .docx files.

Harness-agnostic export for the english-worksheet skill: any AI coding agent
that can run a shell command can call this.

Usage:
    python3 md_to_docx.py input.md output.docx          one file, worksheets on separate pages
    python3 md_to_docx.py input.md output_dir/ --split  one .docx per worksheet

Worksheets are separated by a line containing only `<!-- worksheet -->`.
Anything before the first marker is an overview/cover section (a plan table, how to
use the pack). In --split mode it is written as 00-overview.docx if it has content.
`<!-- pagebreak -->` forces a page break inside a worksheet.

Supports everything md_to_docx.py in english-tutoring supports (# / ## / ### headings,
**bold**, *italic*, bullets, numbered lists that restart at 1, markdown tables,
> notes, links flattened to plain text), plus:
    :::box ... :::     a light gray one-cell box (for "Remember" tips and word banks)

Output is black text only, like the other english-teaching exports.

Requires: pip install python-docx
"""

import re
import sys

try:
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
except ImportError:
    print(
        "python-docx is required. Install it with: pip install python-docx",
        file=sys.stderr,
    )
    sys.exit(1)

INLINE_PATTERN = re.compile(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*.+?\*)")


def add_inline_runs(paragraph, text, italic_default=False, color=None):
    """Split text on **bold**/*italic*/***bold italic*** markers and add runs."""
    pos = 0
    for match in INLINE_PATTERN.finditer(text):
        if match.start() > pos:
            run = paragraph.add_run(text[pos : match.start()])
            run.italic = italic_default
            if color:
                run.font.color.rgb = color

        token = match.group(0)
        if token.startswith("***") and token.endswith("***"):
            run = paragraph.add_run(token[3:-3])
            run.bold = True
            run.italic = True
        elif token.startswith("**") and token.endswith("**"):
            run = paragraph.add_run(token[2:-2])
            run.bold = True
            run.italic = italic_default
        else:
            run = paragraph.add_run(token[1:-1])
            run.italic = True

        if color:
            run.font.color.rgb = color
        pos = match.end()

    if pos < len(text):
        run = paragraph.add_run(text[pos:])
        run.italic = italic_default
        if color:
            run.font.color.rgb = color


def _numbering_element(doc):
    return doc.part.numbering_part.numbering_definitions._numbering


def _get_or_create_decimal_abstract_num(doc):
    """Return the abstractNumId of a simple decimal list definition, creating it once."""
    numbering = _numbering_element(doc)
    cached_id = getattr(doc, "_lesson_abstract_num_id", None)
    if cached_id is not None:
        return cached_id

    existing_ids = [
        int(el.get(qn("w:abstractNumId")))
        for el in numbering.findall(qn("w:abstractNum"))
    ]
    abstract_id = max(existing_ids, default=-1) + 1

    abstract_num = OxmlElement("w:abstractNum")
    abstract_num.set(qn("w:abstractNumId"), str(abstract_id))

    lvl = OxmlElement("w:lvl")
    lvl.set(qn("w:ilvl"), "0")

    start = OxmlElement("w:start")
    start.set(qn("w:val"), "1")
    lvl.append(start)

    num_fmt = OxmlElement("w:numFmt")
    num_fmt.set(qn("w:val"), "decimal")
    lvl.append(num_fmt)

    lvl_text = OxmlElement("w:lvlText")
    lvl_text.set(qn("w:val"), "%1.")
    lvl.append(lvl_text)

    lvl_jc = OxmlElement("w:lvlJc")
    lvl_jc.set(qn("w:val"), "left")
    lvl.append(lvl_jc)

    p_pr = OxmlElement("w:pPr")
    ind = OxmlElement("w:ind")
    ind.set(qn("w:left"), "720")
    ind.set(qn("w:hanging"), "360")
    p_pr.append(ind)
    lvl.append(p_pr)

    abstract_num.append(lvl)
    numbering.insert(0, abstract_num)

    doc._lesson_abstract_num_id = abstract_id
    return abstract_id


def start_new_numbered_list(doc):
    """Create a fresh numbering definition (restarting at 1) and return its numId."""
    numbering = _numbering_element(doc)
    abstract_id = _get_or_create_decimal_abstract_num(doc)

    existing_num_ids = [
        int(el.get(qn("w:numId"))) for el in numbering.findall(qn("w:num"))
    ]
    num_id = max(existing_num_ids, default=0) + 1

    num = OxmlElement("w:num")
    num.set(qn("w:numId"), str(num_id))
    abstract_num_id = OxmlElement("w:abstractNumId")
    abstract_num_id.set(qn("w:val"), str(abstract_id))
    num.append(abstract_num_id)
    numbering.append(num)

    return num_id


def apply_numbering(paragraph, num_id):
    """Attach a numId to a paragraph so it belongs to a specific (restarted) list."""
    p_pr = paragraph._p.get_or_add_pPr()
    num_pr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), "0")
    num_id_el = OxmlElement("w:numId")
    num_id_el.set(qn("w:val"), str(num_id))
    num_pr.append(ilvl)
    num_pr.append(num_id_el)
    p_pr.append(num_pr)


def shade_cell(cell, fill="F2F2F2"):
    """Fill a table cell with a light gray background (text stays black)."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def add_box(doc, box_lines):
    """Render the lines of a :::box block as a shaded one-cell table."""
    table = doc.add_table(rows=1, cols=1)
    table.style = "Table Grid"
    cell = table.rows[0].cells[0]
    shade_cell(cell)
    first = True
    for raw in box_lines:
        text = raw.strip()
        if not text:
            continue
        p = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        if text.startswith("- ") or text.startswith("* "):
            text = "\u2022 " + text[2:].strip()
        add_inline_runs(p, text)
    doc.add_paragraph()


def add_page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


TABLE_SEPARATOR_PATTERN = re.compile(r"^\|?[\s:|-]+\|?$")


def parse_table_row(line):
    """Split a `| a | b |` row into cell strings, dropping the outer empty cells."""
    cells = line.strip().strip("|").split("|")
    return [c.strip() for c in cells]


def force_black_text(doc):
    """Make every text style black. Word's default template colors Title and
    Heading styles blue (and draws a blue rule under the Title); exports must be
    black text only. Works at the XML level so theme colors, table styles and
    unused styles can't leak color back in."""
    styles_el = doc.styles.element
    for color in styles_el.iter(qn("w:color")):
        for attr in list(color.attrib):
            del color.attrib[attr]
        color.set(qn("w:val"), "000000")
    for border in list(styles_el.iter(qn("w:pBdr"))):
        border.getparent().remove(border)
    black = RGBColor(0, 0, 0)
    for style in doc.styles:
        font = getattr(style, "font", None)
        if font is not None:
            font.color.rgb = black


LINK_PATTERN = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def strip_links(text):
    """Turn [label](url) into plain label text so nothing renders as a blue link."""
    return LINK_PATTERN.sub(r"\1", text)


def verify_black(output_path):
    """Fail loudly if the saved file contains any color other than black/auto,
    or any hyperlink (which Word renders blue and underlined)."""
    import zipfile

    problems = []
    with zipfile.ZipFile(output_path) as z:
        for name in ("word/document.xml", "word/styles.xml"):
            xml = z.read(name).decode("utf-8")
            for val in set(re.findall(r'<w:color [^>]*w:val="([^"]+)"', xml)):
                if val.lower() not in ("000000", "auto"):
                    problems.append(f"{name}: color {val}")
            if "<w:hyperlink" in xml:
                problems.append(f"{name}: hyperlink")
    if problems:
        print("Non-black formatting found: " + "; ".join(problems), file=sys.stderr)
        sys.exit(1)


def convert_lines(lines, output_path):
    doc = Document()
    force_black_text(doc)
    current_list_num_id = None  # tracks the active numbered list, so a new list restarts at 1
    wrote_content = False

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith(":::box"):
            i += 1
            box_lines = []
            while i < n and lines[i].strip() != ":::":
                box_lines.append(lines[i])
                i += 1
            add_box(doc, box_lines)
            current_list_num_id = None
            i += 1
            continue

        if stripped in (WORKSHEET_MARKER, PAGEBREAK_MARKER):
            if wrote_content or stripped == PAGEBREAK_MARKER:
                add_page_break(doc)
            current_list_num_id = None
            i += 1
            continue

        wrote_content = True
        is_numbered_item = bool(re.match(r"^\d+\.\s", stripped))
        if not is_numbered_item:
            current_list_num_id = None  # any non-numbered-item line ends the current list

        is_table_start = (
            stripped.startswith("|")
            and i + 1 < n
            and TABLE_SEPARATOR_PATTERN.match(lines[i + 1].strip())
        )

        if is_table_start:
            header_cells = parse_table_row(stripped)
            i += 2  # skip header + separator row
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(parse_table_row(lines[i].strip()))
                i += 1

            table = doc.add_table(rows=1, cols=len(header_cells))
            table.style = "Table Grid"
            for cell, text in zip(table.rows[0].cells, header_cells):
                add_inline_runs(cell.paragraphs[0], text)
                for run in cell.paragraphs[0].runs:
                    run.bold = True

            for row_cells in rows:
                row = table.add_row()
                for cell, text in zip(row.cells, row_cells):
                    add_inline_runs(cell.paragraphs[0], text)

            doc.add_paragraph()
            continue

        if stripped.startswith("### "):
            doc.add_heading(stripped[4:].strip(), level=2)
        elif stripped.startswith("## "):
            doc.add_heading(stripped[3:].strip(), level=1)
        elif stripped.startswith("# "):
            doc.add_heading(stripped[2:].strip(), level=0)
        elif stripped.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            add_inline_runs(p, stripped[2:].strip(), italic_default=True)
        elif stripped.startswith("- ") or stripped.startswith("* "):
            p = doc.add_paragraph(style="List Bullet")
            add_inline_runs(p, stripped[2:].strip())
        elif is_numbered_item:
            if current_list_num_id is None:
                current_list_num_id = start_new_numbered_list(doc)
            p = doc.add_paragraph(style="List Number")
            add_inline_runs(p, re.sub(r"^\d+\.\s", "", stripped))
            apply_numbering(p, current_list_num_id)
        elif stripped == "---":
            doc.add_paragraph().add_run("").add_break()
        else:
            p = doc.add_paragraph()
            add_inline_runs(p, stripped)

        i += 1

    doc.save(output_path)
    verify_black(output_path)


WORKSHEET_MARKER = "<!-- worksheet -->"
PAGEBREAK_MARKER = "<!-- pagebreak -->"


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60] or "worksheet"


def split_sections(lines):
    """Return (preamble_lines, [worksheet_lines, ...]) split on the worksheet marker."""
    sections = [[]]
    for line in lines:
        if line.strip() == WORKSHEET_MARKER:
            sections.append([])
        else:
            sections[-1].append(line)
    return sections[0], sections[1:]


def first_heading(section):
    for line in section:
        m = re.match(r"^#{1,3}\s+(.*)", line.strip())
        if m:
            return m.group(1)
    return "worksheet"


def convert(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = strip_links(f.read()).splitlines()
    convert_lines(lines, output_path)


def convert_split(input_path, output_dir):
    import os

    with open(input_path, "r", encoding="utf-8") as f:
        lines = strip_links(f.read()).splitlines()
    preamble, sheets = split_sections(lines)
    os.makedirs(output_dir, exist_ok=True)
    written = []
    if any(l.strip() for l in preamble):
        path = os.path.join(output_dir, "00-overview.docx")
        convert_lines(preamble, path)
        written.append(path)
    for number, section in enumerate(sheets, start=1):
        path = os.path.join(output_dir, f"{number:02d}-{slugify(first_heading(section))}.docx")
        convert_lines(section, path)
        written.append(path)
    return written


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--split"]
    split = "--split" in sys.argv[1:]
    if len(args) != 2:
        print(
            "Usage: python3 md_to_docx.py input.md output.docx\n"
            "       python3 md_to_docx.py input.md output_dir/ --split",
            file=sys.stderr,
        )
        sys.exit(1)
    if split:
        for path in convert_split(args[0], args[1]):
            print(f"Wrote {path}")
    else:
        convert(args[0], args[1])
        print(f"Wrote {args[1]}")
