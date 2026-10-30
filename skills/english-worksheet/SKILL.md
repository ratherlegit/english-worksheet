---
name: english-worksheet
description: Creates personalized English homework worksheets and answer keys for a single ESL/EFL learner, built from a student profile. The profile comes from existing data (an english-tutoring record, lesson transcripts, a written analysis, old handouts, tutor notes) or from a short interview with the tutor. The tutor chooses how many worksheets, and gets either one combined .docx or one .docx per worksheet. Use when the user asks for worksheets, homework, practice exercises, drills, or a practice pack for an English learner, e.g. "make homework for Maria based on this analysis" or "I need 5 worksheets on articles and past tense for my student". For lesson plans use english-tutoring (one student) or english-classroom (a group).
---

# English Worksheets

Build homework worksheets that target what one learner actually gets wrong, then export them as Word files. The profile is the product: a worksheet pack is only as good as the evidence about the student behind it. Adapt to what the tutor asks for. Do not force steps they have already answered.

## Step 0: Find the student

Look for the student by name before asking anything.

1. `~/eng-teaching-records/worksheets/<name-slug>.md` (lowercase, hyphens). This skill's own file: profile, focus areas, worksheet log. If it exists, load it, skip Step 1, and ask only whether anything changed since last time.
2. `~/eng-teaching-records/<name-slug>.md`, the english-tutoring record. Read-only. Import level, interests, goal, location, English variety, vocabulary log, and grammar already covered. Never write to this file.

Create `~/eng-teaching-records/worksheets/` if it does not exist. Records live outside the skill folder on purpose, so they survive updates.

## Step 1: Build the student profile

Ask how the tutor wants to build it, offering these as options:

- **Ingest existing data**: a student record, transcripts, a written analysis, old worksheets or handouts, notes, a folder. Accept file paths, folders, or pasted text.
- **Answer interview questions**.
- **Both**: ingest first, then interview only for the gaps.

**Ingesting.** Read every file fully, then follow `references/student-profile.md` ("Ingesting data") to extract: profile fields, recurring error patterns with quoted evidence, strengths, vocabulary and grammar already taught, and the student's own stated goals and weaknesses. Show the extracted profile in one compact block, then ask the tutor to confirm or correct it. Interview only for missing fields.

**Interviewing.** Offer a **detailed** interview (one question at a time, the default) or a **light** one (four bundled prompts). Use the question set in `references/student-profile.md` ("Interview"). The most important answer is the focus areas: what this student keeps getting wrong, in the tutor's own words. If the tutor cannot say, offer to look at a sample of the student's writing or speech and analyze it.

Save or update the profile file (format in `references/student-profile.md`) once the tutor confirms it.

## Step 2: Plan the worksheets

Ask these, one at a time, never suggesting a default number:

1. **How many worksheets do you want?** The tutor suggests the number.
2. **One combined file, or one file per worksheet?** Both can include an overview page.
3. **Answer key?** Default yes, as a separate file the student never sees.
4. Only if not already known: minutes per worksheet (default 15 to 20) and whether speaking or recording tasks are welcome.

Then propose a plan as a table and wait for approval before writing anything:

| # | Title | Focus (from the profile) | Exercise types | Minutes |
|---|---|---|---|---|

Rules for the plan:
- Order by priority: the most frequent and most noticeable errors first, then the less frequent ones. Within a pack, move from simple to complex where there is a natural order.
- If the tutor wants more worksheets than there are distinct focus areas, split by skill (grammar, vocabulary, speaking, pronunciation, writing, listening) and add review worksheets. If fewer, cover the top priorities and say plainly what was left out.
- One main focus per worksheet. Two small related points can share one.
- Vary exercise types across the pack (see `references/exercise-types.md`).
- Never schedule a point the profile marks as mastered or excluded. Treat a point with only one weak piece of evidence as "check first" and say so.

## Step 3: Write the worksheets

Write the whole pack as one markdown file following `references/exercise-types.md` (worksheet anatomy, exercise catalog, answer key format). Apply these rules to every worksheet:

- **Open with a focus box** (Grammar Focus on grammar worksheets, Language Focus on vocabulary and phrase worksheets). It explains the point the whole worksheet is built on: the rule in one plain sentence, a provided table or pattern, 5 to 8 examples that show the point used in different ways (statements, questions, negatives, different subjects, different work situations), a short text or dialogue showing it in real use, and 2 or 3 common mistakes with the fix. Make it clear enough that the student could do the worksheet from the box alone.
- **Provide the forms, never ask the student to produce them in a list.** Do not ask the student to write out every form of a verb or fill in a table of forms. Put the table in the focus box, then make the student use it in different ways across the activities: choose the right form in a message, repair a short text, answer questions about their own work, build a sentence from a prompt, write a short paragraph.
- **Design for typing.** Students work on a computer in the same Word or Google Docs file. They will not circle, underline, cross out, tick, or draw. Give each item a "Your answer" cell to type in (a table whose last column is headed `Your answer`) and use a `:::write` box for writing tasks. Ask the student to type a word, a letter, or a sentence. Never write "circle," "underline," or "draw a line."

Apply these rules to every student-facing line:

- Address the student in the second person. Write in simple English matched to the CEFR level, and simpler than the exercise content. Short instructions beat clever ones.
- **Never mention the tutor, teacher, instructor, or "the student".** For recordings, write "bring it to your next lesson", not "send it to your tutor".
- Personalize: use the student's work, interests, location, and real situations in the example sentences. Do not copy the student's own error sentences verbatim as exercise items. Write fresh sentences with the same error type.
- Every exercise item has exactly one correct answer, unless it is labeled open. Check gap-fills and multiple choice so a distractor cannot also truthfully complete the sentence.
- Do not mark acceptable informal English as wrong. If a form is understandable but less usual, say so in the answer key.
- Never reuse a vocabulary word the profile lists as taught, unless the worksheet is reviewing it.
- No em dashes anywhere. No small label lines above headings.

Before building, scan the student-facing text for the words *tutor*, *teacher*, *instructor*, and *student* (case-insensitive), and for *circle*, *underline*, *cross out*, *tick*, and *draw*, and rewrite every hit. Do this every time.

## Step 4: Build the files

Ask where to save if the tutor has not said; default to `~/Downloads/<student-slug>-worksheets/`. Run the bundled exporter from the skill folder (needs `pip install python-docx`):

- **Combined file**: `python3 scripts/md_to_docx.py pack.md out/pack.docx`
- **One file per worksheet**: `python3 scripts/md_to_docx.py pack.md out/ --split`
- The answer key is a separate markdown file exported the same way, never merged into the student's file.

If there is no shell access, say so plainly and give clean markdown to paste instead. If rendering is available (LibreOffice), look at the pages. On macOS without it, `qlmanage -t -s 1400 -o <dir> file.docx` makes a first-page preview, but it ignores table widths and page breaks, so it only confirms fonts, borders, and shading. If nothing can render the file, tell the tutor the layout was not visually checked.

## Step 5: Update the record

Append to the Worksheet Log in the student's worksheet profile: date, titles, focus areas covered, and the vocabulary used. Add new "already practiced" vocabulary. Offer to adjust the plan after the tutor has seen how the student did, and fold any new errors back into the Focus Areas table.

## Reference files

- `references/student-profile.md`: how to ingest data, the interview question set, and the profile file format. Read in Step 1.
- `references/exercise-types.md`: worksheet anatomy, exercise catalog with sizing, speaking tasks, answer key format, and quality checks. Read in Steps 2 and 3.
