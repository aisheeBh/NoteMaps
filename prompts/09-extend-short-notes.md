# 09. Extend notes that are under the length target

Use this on notes that came out shorter than about 4,500 words (leaves) or 4,500 words (chapters). It adds genuine depth, not padding.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps. Read skills/notemap-content/SKILL.md completely, plus the leaf reference note A.1 "What is Learning-" it names.

These notes are under the length target: <NOTE PATHS OR NODE LABELS>. Bring each up to about 4,500-5,000 words of prose (excluding diagram code).

Rules:
- Add real depth that the subject needs: a further worked example, a second case study, a method or mechanism explained step by step, a study card, a Watch out box on a common misconception, or an extra figure. Do not repeat what the note already says and do not pad.
- Keep the note's existing structure, headings, figure numbering and closing sections (Summary, Self-Check, Answer Key, Glossary). Insert new material in the right place and renumber later figures and any in-text figure mentions so numbering stays sequential. Update the Summary, Self-Check, Answer Key and Glossary if the new material adds to them.
- Stay off the subjects of sibling notes (run python scripts/find_node.py "<node>" to see them).
- New made-up material must be labelled "(illustrative)". Name study authors only when verified by search; otherwise describe the study by institution or year.
- Validate without --render while drafting, then run python scripts/validate_notes.py "<folder>" --render once at the end. Fix every error and warning.
- Use at most 3 agents at a time. Do not run git commands and do not touch derived_maps/.

Report, per note: the word count before and after, what was added, and any facts taken from memory.
```
