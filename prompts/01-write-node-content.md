# 01. Write the content of a node

Use this to fill in one empty note, or every empty note under a node. Replace the part in angle brackets with a node label (`1.6.2`, `1.6.2.A`, `1.6.2.A.3`), a title, or a path.

```text
Use the NoteMaps repo at C:\abh_pers_od_tfr\NoteMaps\NoteMaps.

Read skills/notemap-content/SKILL.md completely and follow it as the binding standard. Also read its two reference notes end to end:
- leaf reference: main_map/Professional Career Development/1. Universal Foundations/1.1. Learning Foundation/1.1.1. Learning Science & Cognition/A. Learning How to Learn/A.1. What is Learning-/A.1. What is Learning-.md
- parent reference: main_map/Professional Career Development/Professional Career Development.md

Write the content for this node and everything under it that is still empty: <NODE LABEL, TITLE OR PATH>

Rules to keep in mind:
- Run `python scripts/find_node.py "<node>"` first. It gives the real title, the path, whether the note is already written, the figure prefix, and its siblings and children.
- Do not overwrite a note that is already written without asking me.
- Study-notes format: bullets are the primary form, with few tables and no checklists. Use the Definition, Key point, Remember, Mnemonic, Watch out, Example, Formula and In practice boxes. Include at least one case study and one worked example, 5-8 numbered figures (Mermaid and SVG, readable in black and white), British spelling, and the closing sections Summary, Self-Check, Answer Key and Glossary.
- Leaves run about 4,500-5,500 words and parent chapters 4,500-6,000.
- A parent chapter teaches the umbrella subject itself and mentions each child in a sentence or two at most. It never lists the children.
- No talk about the map, levels, printing or links to other notes.
- Anything made up (invented people, organisations, cases or numbers) must say "(illustrative)" in its heading, or "Illustrative figures" under a table. Real, documented events keep plain headings. Name study authors only when verified.
- Web-search for facts. Write nothing about studies or numbers you cannot verify.
- Stay off the subjects of sibling notes (one sentence at most).
- Keep the machine load low. Validate without --render while drafting, preview SVGs in one batch, and run `python scripts/validate_notes.py "<folder>" --render` once at the end. Fix every error and warning.
- For several notes, use at most 3 writing agents at a time.
- Do not run git commands, push, or touch derived_maps/ unless I ask.

When finished, report the notes written with word and figure counts, the validation result, anything you wrote from memory that I should check, and any contested points you flagged.
```

If the node is also in a derived map, add this line at the end: "Then sync the derived map as described in section 13 of the skill." Or use prompt 03 afterwards.
