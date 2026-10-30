# english-worksheet

**Personalized homework worksheets for one English learner, as Word files.** It builds a picture of the student first, then writes exactly as many worksheets as you ask for, aimed at what that student actually gets wrong.

## What it does

1. **Builds a student profile** from data you already have (an english-tutoring record, lesson transcripts, a written analysis, old handouts, notes) or from a short interview. Recurring errors are quoted with their evidence so you can check them.
2. **Asks how many worksheets you want**, then proposes a plan (title, focus, exercise types, minutes) for you to approve.
3. **Writes the worksheets** in simple English, using the student's own work and interests. Each one starts with a short, clear grammar or language focus, then activities the student types into the same file.
4. **Exports `.docx`**: one combined file, or one file per worksheet, plus a separate answer key with notes for you.
5. **Remembers the student**, so the next pack builds on the last.

Black text only, no em dashes, and nothing in the student's pages mentions a tutor or teacher.

## Install

### Claude Code

```
claude plugin marketplace add ratherlegit/english-worksheet
claude plugin install english-worksheet@english-worksheet
```

Then ask in plain English, for example *"Make 5 worksheets for my student Maria from this lesson analysis."* Or invoke it with `/english-worksheet:english-worksheet`.

### Claude.ai or the Claude Desktop app

Add the marketplace `ratherlegit/english-worksheet` under Settings, then Plugins, then install `english-worksheet`.

### Other agents (Codex, Cursor, Aider, Windsurf, Gemini CLI)

These read `AGENTS.md` automatically. Clone the repo, open it, and ask for worksheets. For `.docx` export, run `pip install python-docx`.

## Records

Profiles and worksheet logs are saved to `~/eng-teaching-records/worksheets/<student>.md`, outside the repo so updates never touch them. If you also use english-tutoring, its record for the same student is read (never changed) to reuse level, interests, and the vocabulary log.

## Versions

Pre-1.0 while it is tested on real students. See git tags.

- `0.2.0`: every worksheet opens with a Grammar Focus or Language Focus box (clear rule, provided table, varied examples, a short text in real use, common mistakes). Worksheets are designed for typing in Word or Google Docs: blue answer cells next to each item and blue write boxes. No "write all the forms" tasks and no circling or underlining.
- `0.1.0`: first release.

## Tests

```
python3 tests/validate_skill.py
```

## License

MIT
