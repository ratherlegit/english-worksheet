"""Structure and rule checks for the english-worksheet plugin. Stdlib only (the exporter tests need python-docx and skip without it)."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "english-worksheet"
SKILL_MD = SKILL_DIR / "SKILL.md"
REFS = SKILL_DIR / "references"
SCRIPT = SKILL_DIR / "scripts" / "md_to_docx.py"
EM_DASH = "—"

SAMPLE = """# Sample Pack

Overview text.

| Day | Worksheet |
|---|---|
| 1 | Be |

<!-- worksheet -->
## Worksheet 1: Do I need be?

:::box
**Remember**
- I am busy.
- She works.
:::

### Part A: Fix it
*Fix each sentence.*

1. I working now.
2. She very busy.

<!-- worksheet -->
## Worksheet 2: Past tense

1. went
2. bought
"""


def read(path):
    return Path(path).read_text(encoding="utf-8")


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def have_docx():
    try:
        import docx  # noqa: F401
        return True
    except ImportError:
        return False


class StructureTests(unittest.TestCase):
    def test_frontmatter(self):
        fm = frontmatter(read(SKILL_MD))
        self.assertEqual(fm.get("name"), "english-worksheet")
        self.assertGreater(len(fm.get("description", "")), 100)
        self.assertEqual(set(fm), {"name", "description"})

    def test_skill_md_is_lean(self):
        self.assertLess(len(read(SKILL_MD).splitlines()), 500)

    def test_referenced_files_exist(self):
        for ref in re.findall(r"`(references/[\w.-]+)`", read(SKILL_MD)):
            self.assertTrue((SKILL_DIR / ref).exists(), ref)
        for ref in REFS.glob("*.md"):
            self.assertIn(f"references/{ref.name}", read(SKILL_MD), f"{ref.name} not linked from SKILL.md")

    def test_no_em_dashes(self):
        for path in [SKILL_MD, ROOT / "README.md", ROOT / "AGENTS.md", *REFS.glob("*.md")]:
            self.assertNotIn(EM_DASH, read(path), str(path))

    def test_versions_match(self):
        plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
        market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
        self.assertEqual(plugin["version"], market["version"])
        self.assertRegex(plugin["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(plugin["name"], "english-worksheet")

    def test_no_student_data_committed(self):
        for path in ROOT.rglob("*"):
            if path.is_file() and ".git" not in path.parts and path.suffix in {".md", ".json", ".py"}:
                self.assertNotIn("jay" + "den", read(path).lower(), str(path))


@unittest.skipUnless(have_docx(), "python-docx not installed")
class ExporterTests(unittest.TestCase):
    def run_script(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)

    def test_single_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "pack.md"
            src.write_text(SAMPLE, encoding="utf-8")
            out = Path(tmp) / "pack.docx"
            result = self.run_script(str(src), str(out))
            self.assertEqual(result.returncode, 0, result.stderr)
            xml = zipfile.ZipFile(out).read("word/document.xml").decode()
            self.assertEqual(xml.count('w:type="page"'), 2)  # one break before each worksheet
            self.assertIn("F2F2F2", xml)  # the box is shaded

    def test_split(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "pack.md"
            src.write_text(SAMPLE, encoding="utf-8")
            out = Path(tmp) / "out"
            result = self.run_script(str(src), str(out), "--split")
            self.assertEqual(result.returncode, 0, result.stderr)
            names = sorted(p.name for p in out.glob("*.docx"))
            self.assertEqual(names, ["00-overview.docx", "01-worksheet-1-do-i-need-be.docx", "02-worksheet-2-past-tense.docx"])
            for p in out.glob("*.docx"):
                xml = zipfile.ZipFile(p).read("word/document.xml").decode()
                self.assertNotIn('w:type="page"', xml)  # no stray break in a one-worksheet file

    def test_usage_error(self):
        self.assertNotEqual(self.run_script().returncode, 0)


if __name__ == "__main__":
    unittest.main()
