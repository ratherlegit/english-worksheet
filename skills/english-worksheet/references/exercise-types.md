# Exercise Types and Worksheet Anatomy

Contents: File format, Worksheet anatomy, The focus box, Designing for typing, Exercise catalog, Writing tasks, Answer key, Quality checks.

## File format

Write the whole pack as one markdown file. Separate worksheets with a line containing only `<!-- worksheet -->`. Anything before the first marker is an overview (how to use the pack, a plan table). Use `<!-- pagebreak -->` to force a page break inside a worksheet.

- `:::box` and `:::` around a block gives a shaded gray box (the focus box, word banks).
- A `|` table whose last column is headed `Your answer` gives light blue answer cells the student types into.
- `:::write 5` and `:::` gives an empty light blue box about 5 lines tall for writing tasks.
- A normal `|` table is a plain reference table.

Skeleton:

```
# Pack Title

One short paragraph on how to use the pack. Say: type your answers in the blue boxes.

<!-- worksheet -->
## Worksheet 1: Title in plain words

One sentence on what this worksheet practices.

:::box
**Grammar Focus: the point in plain words**
The rule in one sentence.

| Form | Use | Example |
|---|---|---|
| ... | ... | ... |

**Examples**
- ...
**In real use**
A short text or dialogue.
**Watch out**
- Not: ... Yes: ...
:::

### Part A: Choose the right form
*Type the correct word in the blue box.*

| # | Sentence | Your answer |
|---|---|---|
| 1 | item | |

### Part B: Write
*Instruction.*

:::write 5
:::
```

Headings: `#` for the pack title (overview), `##` for each worksheet, `###` for each part.

## Worksheet anatomy

- **Focus box first**, directly under the one-sentence purpose.
- **15 to 20 minutes** unless the profile says otherwise. About 4 to 5 parts.
- **Order**: easier to freer. Recognize and choose, then repair, then answer questions or build sentences, then write.
- **At least one writing task** unless the worksheet is explicitly drill-only.
- **One short instruction** per part. Tell the student exactly what to type.
- **Titles in plain words**: "Do I need 'be'?" beats "Copula usage".

## The focus box

The student should be able to do the worksheet from this box alone. Include:

1. **A plain one-sentence rule**, with no jargon. Say what the point does for the speaker ("use this to talk about plans").
2. **A provided table or pattern** the activities will use again (forms, uses, quantifiers, prepositions, word families, reactions). This replaces any "write all the forms" activity.
3. **5 to 8 examples that show dynamic use**, not five versions of the same sentence. Vary the subject, the sentence type (statement, question, negative), the setting, and the use. Bold the target. Group by use when the point has more than one use.
4. **A short text or dialogue (3 to 6 lines)** showing the point in a real situation from the student's work, with the target in bold.
5. **2 or 3 common mistakes**, written "Not: ... Yes: ..." in the student's likely error form, with a very short reason.

Name the box **Grammar Focus** for grammar points and **Language Focus** for vocabulary, phrases, and word choice. Keep the name consistent across a pack.

## Designing for typing

Students open the file in Word or Google Docs and type in it. So:

- The item text stays in its own cell. The answer goes in the blue cell next to it. The layout never moves.
- Ask for a word, a letter, or one sentence per cell. For anything longer, use a write box.
- Never ask for physical actions. Replace circle with "type the correct word," underline with "type the word," match with lines with "type the letter," tick with "type yes or no."
- Offer choices inside the sentence, like "The sponsors **is / are** happy," and ask the student to type the one that fits.
- Gap-fills number the gaps in a short text and list the numbers in the answer table. Put a word bank in a `:::box` above it.

## Exercise catalog

| Type | Use for | Items | Notes |
|---|---|---|---|
| Choose and type | Agreement, word choice, -ed/-ing, prepositions | 6 to 8 | Two or three options inside the sentence. Every wrong option is a real learner error |
| Fix the message | Errors the student makes | A 4 to 6 line email or chat with 4 to 6 errors | Student retypes it correctly in a write box. Say how many errors there are |
| Fix the sentence | Errors the student makes | 6 to 8 | Include 2 correct ones: "type OK if it is correct" |
| Fill the gaps in a text | Verbs, articles, prepositions, linking words | 6 to 10 gaps in one short text | Word bank or the focus table supplies the answers |
| Match and type | Vocabulary and meanings, situations and reactions | 6 to 8 | Student types the letter |
| Use the table | Anything from the focus table | 5 to 6 | Questions that need the table: "Which form fits this sentence?" |
| Answer about you | Real use of the point | 4 to 5 questions | Full-sentence answers about the student's own work and week |
| Join or transform | Rules, conditionals, reported speech | 4 to 5 | Give the first answer as a model |
| Build a sentence | Structure, questions | 4 to 5 | Give the words and ask for a sentence |
| Write | Free production | 3 to 6 sentences | Name the target and a minimum, e.g. "use going to twice" |

Do not use: write every form of a verb, fill in a table of forms, copy sentences, or any task that only checks memory of a list.

Sizing: if an item takes longer than a minute, use fewer items.

## Writing tasks

Always give the topic, the length, the target structure, and one thing to check afterward. Example: "Write 5 sentences about a busy day at a tournament. Use the past simple and two linking words. Check: is every verb in the past?" Use a `:::write` box sized to the answer (about one line per sentence plus one).

No recording tasks unless the profile says speaking tasks are fine. If it does, tell the student to bring the recording to the next lesson. Do not name the tutor.

## Answer key

Only when the tutor asks for one. A separate file with the same worksheet numbering. For each worksheet:

- A **Targets** line: which focus area from the profile it practices, and the evidence behind it.
- Answers by part, numbered to match.
- For open tasks: what to look for, and a sample answer.
- Notes where more than one answer is acceptable, or where a form is informal but fine.

Use `<!-- worksheet -->` markers here too, so the key splits the same way.

## Quality checks

Run these before exporting:

1. Every item has exactly one correct answer, or is labeled open.
2. In choices and word banks, no wrong option can also be correct in the sentence.
3. The focus box examples are varied in use, and the mini text is about the student's real world.
4. Every table in a focus box is used in at least two different activities.
5. No activity asks the student to write out forms from a list.
6. Example sentences use the student's world (work, places, interests), not generic "John goes to the shop".
7. Instructions are simpler than the exercise content.
8. No sentence copies an error sentence from the student's own speech. Same error type, new sentence.
9. No hit for tutor, teacher, instructor, or student, and none for circle, underline, cross out, tick, or draw, in student-facing text.
10. No em dashes. Black text only.
11. Every answer table has a `Your answer` last column, and every writing task has a `:::write` box.
12. The pack matches the approved plan: count, order, titles.
13. If no renderer is available, say the layout was not visually checked.
