# Exercise Types and Worksheet Anatomy

Contents: File format, Worksheet anatomy, Exercise catalog, Speaking and recording tasks, Answer key, Quality checks.

## File format

Write the whole pack as one markdown file. Separate worksheets with a line containing only `<!-- worksheet -->`. Anything before the first marker is an overview (how to use the pack, a plan table). Use `<!-- pagebreak -->` to force a page break inside a worksheet. Use `:::box` and `:::` around a tip or word bank to get a shaded box. Use `|` tables for matching and completion tasks. Use `___` for blanks and a row of underscores for writing lines.

Skeleton:

```
# Homework Pack 1

One short paragraph on how to use the pack.

<!-- worksheet -->
## Worksheet 1: Title in plain words

One sentence on what this worksheet practices.

:::box
**Remember**
- rule or tip
- rule or tip
:::

### Part A: Fix the sentence
*Instruction in one short sentence.*

1. item
2. item

### Part B: ...
```

Headings: `#` for the pack title (overview), `##` for each worksheet, `###` for each part.

## Worksheet anatomy

- **Length**: 15 to 20 minutes unless the profile says otherwise. About 3 to 4 parts.
- **Order**: controlled to freer. Recognize (circle, match), then produce with support (fix, gap-fill, transform), then produce freely (write, speak).
- **A short Remember box** when a rule helps: two to four lines, with examples, in simple words.
- **One-sentence purpose** under the title, written to the student.
- **At least one production task** (writing or speaking) unless the worksheet is explicitly drill-only.
- **Instructions**: one short sentence per part. Tell the student exactly what to write.
- **Titles in plain words**: "Do I need 'be'?" beats "Copula usage".

## Exercise catalog

| Type | Use for | Items | Notes |
|---|---|---|---|
| Fix the sentence | Errors the student produces | 8 to 10 | Include 2 correct sentences marked "write OK" so the student cannot assume every sentence is wrong |
| Circle the correct word | Agreement, word choice, -ed/-ing | 6 to 8 | Two or three options; every wrong option is a real learner error |
| Gap-fill with word bank | Vocabulary, articles, prepositions | 8 | One more word than gaps is fine; each gap has one correct answer |
| Match | Vocabulary and meanings, phrases and situations | 8 to 11 | Put the table on the page; students write letters |
| Complete the table | Word families, verb forms | 6 rows | Give one cell per row |
| Transform | Tense change, active to passive, direct to reported | 5 to 6 | Give a start for the first item |
| Error hunt | Short paragraph with 4 to 6 errors | 1 paragraph | State how many errors there are |
| Put in order | Sentence structure, questions | 5 to 6 | Scrambled words give one valid sentence |
| Guided writing | Free production with a target | 3 to 5 sentences | Name the target structure and a minimum, e.g. "use is or are at least three times" |
| Retell | Narrative tense | 1 story | Same story told twice (past, then present) |
| Record yourself | Fluency, pronunciation, fillers | 1 to 2 minutes | See below |
| Self-check | Closing a pronunciation or fluency worksheet | 3 to 4 lines | Yes / Not yet table |

Sizing: if an item type takes longer than a minute each, use fewer items.

## Speaking and recording tasks

Always give: the topic or question, the length, the structure to use, and one thing to check afterwards. Example: "Record 2 minutes: tell me about a problem you solved at work. Use first, then, after that. Listen again and write down three verbs in the wrong tense." Tell the student to bring the recording to their next lesson. Do not name the tutor.

For filler words or pronunciation, include a counting table so progress is visible across attempts.

Only include recording tasks if the profile says speaking tasks are fine.

## Answer key

A separate file with the same worksheet numbering. For each worksheet:

- A **Targets** line: which focus area from the profile it practices, and the evidence behind it.
- Answers by part, numbered to match.
- For open tasks: what to listen or look for, and a sample answer.
- Notes where more than one answer is acceptable, or where a form is informal but fine.
- Any item that depends on evidence the tutor should double check.

Use `<!-- worksheet -->` markers here too, so the key splits the same way.

## Quality checks

Run these before exporting:

1. Every item has exactly one correct answer, or is labeled open.
2. In multiple choice and word banks, no wrong option can also be correct in the sentence.
3. Example sentences use the student's real world (work, places, interests), not generic "John goes to the shop".
4. Reading level of instructions is below the exercise content.
5. No sentence copies an error sentence from the student's own speech. Same error type, new sentence.
6. No hit for tutor, teacher, instructor, or student in student-facing text.
7. No em dashes. Black text only.
8. Item numbers in the answer key match the worksheet.
9. The pack matches the approved plan: count, order, titles.
10. Layout: if no renderer is available, say it was not visually checked.
