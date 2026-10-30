# english-worksheet

ESL/EFL homework-worksheet agent. This file follows the [AGENTS.md](https://agents.md) convention, read automatically by OpenAI Codex, Cursor, Aider, Windsurf, Gemini CLI, and other coding-agent harnesses.

Follow `skills/english-worksheet/SKILL.md` in full. It reads its own `references/` folder from this repo.

- **Records** live in `~/eng-teaching-records/worksheets/`. The english-tutoring record at `~/eng-teaching-records/<name>.md` may be read, never written. Record folders live outside the repo on purpose so they survive updates (create them if missing).
- **Exporting to .docx** works on any harness with shell access: run `skills/english-worksheet/scripts/md_to_docx.py` (requires `pip install python-docx`). In a chat-only harness with no code execution, say so plainly and give clean, paste-ready markdown instead.
- **Claude Code**: install as a plugin (see `README.md`).
