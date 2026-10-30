# Student Profile

Contents: Ingesting data, Interview, Prioritizing focus areas, Profile file format.

## Ingesting data

Accepted sources: an english-tutoring record, lesson transcripts or recordings' transcripts, a written analysis or summary, old worksheets and handouts, tutor notes, a coursebook unit. Read each source in full before extracting anything.

Extract:

| Field | Where to look |
|---|---|
| Name, pronouns, level, location, interests, goal, English variety | Records, summaries, tutor notes |
| Recurring errors | Analyses, tutor notes, and the student's own lines in transcripts |
| Strengths | Analyses, transcripts |
| Student's own stated weaknesses and goals | Transcripts (the student often names them) |
| Vocabulary and grammar already taught | Vocabulary logs, old handouts, coursebook units |
| Practical preferences | Session length, homework time, tone, simplicity of instructions |

**If the only source is a raw transcript**, do the analysis first:
- Use only the student's lines. Speaker labels from automatic transcription are often wrong on short replies, so trust patterns, not single lines.
- A pattern counts if it appears at least twice, or once and clearly characteristic. Mark single instances as "check first".
- Automatic transcription tends to smooth over grammar and mishear words. Do not build an exercise on a mistake that might be a transcription error.
- Quote the evidence for every pattern. The tutor must be able to check it.
- Do not guess pronunciation from text. Note pronunciation items as low confidence unless the student or tutor raised them.

**If a written analysis already exists**, use it as the starting point, but spot-check at least two of its claims against the raw evidence when the evidence is available.

After extraction, show the profile in one compact block (see format below) and ask the tutor to confirm or correct. Ask interview questions only for fields still empty.

## Interview

**Detailed** (default): one question per turn, in this order. **Light**: bundle into four prompts: (1) name, pronouns, level; (2) location, interests, work; (3) goal, error patterns, what is already covered; (4) packaging and practical preferences.

1. **Name** (free text, never suggest names).
2. **Pronouns** (he/him, she/her, they/them). Use them consistently.
3. **Level**: CEFR if known, or "not sure". If unsure, ask what the student can and cannot do and estimate.
4. **Location and first language**: city and country. Use it quietly to anticipate likely first-language interference. Do not lecture the tutor about linguistics.
5. **Interests, work, and daily situations**: material for example sentences.
6. **Goal**: exam, work, travel, immigration, fluency.
7. **Focus areas**: "What does this student keep getting wrong?" Take the tutor's words. Ask for example sentences if they have them. This is the most valuable answer.
8. **Already mastered or already covered**: grammar and vocabulary to skip or only recycle.
9. **English variety**: American (default) or British.
10. **Practical preferences**: minutes per worksheet, how many days of homework, whether recordings or speaking tasks are fine, whether instructions should be extra simple, anything to avoid.
11. **Prior documents**: ask whether there are old worksheets, handouts, or notes to read. "No, they are new to me" ends the interview.

## Prioritizing focus areas

Rank each error pattern by: how often it appears, how much it gets in the way of being understood or sounding confident, and how teachable it is with practice on paper. A suggested order for most intermediate learners, adjusting to the evidence:

1. Core verb accuracy: missing "be", subject-verb agreement, tense choice and consistency.
2. Noun phrase: countable and uncountable nouns, articles, possessive 's, quantifiers, word forms.
3. Verb patterns: verb + preposition, verb + infinitive or gerund.
4. Sentence structure: questions, conditionals, relative clauses, reported speech, linking words.
5. Speaking habits and fluency: fillers, set phrases, reactions. Run alongside the others, not after them.
6. Vocabulary for the student's work or goal.
7. Pronunciation, only with evidence beyond a transcript.

Be honest about uncertainty. A point with strong, repeated evidence outranks one that "usually" appears for learners with the same first language.

## Profile file format

Save to `~/eng-teaching-records/worksheets/<name-slug>.md`:

```
# Worksheet Profile: <Name>

## Profile
- Pronouns:
- Level:
- Location / first language:
- Interests / work:
- Goal:
- English variety: American (default) or British
- Minutes per worksheet:
- Speaking tasks OK: yes/no
- Instruction style: standard / extra simple
- Exclusions:

## Sources
- <file or description, date>

## Focus Areas
| Priority | Pattern | Evidence (quoted) | Confidence | Status |
|---|---|---|---|---|
| 1 | Missing "be" | "My boss very busy today" | High (3 sessions) | Not yet practiced |

## Strengths
- ...

## Already Covered
- Grammar: ...
- Vocabulary: ...

## Worksheet Log
### 2026-10-30: Pack 1 (9 worksheets)
- Worksheets: ...
- Focus areas practiced: ...
- Vocabulary used: ...
```

Update Status to "Practiced <date>" after a pack is delivered. Add new evidence rather than overwriting old evidence.
