---
name: notemap-content
description: Write the content of NoteMaps notes (main_map/**/<node>/<node>.md) as study notes in a book-like knowledge base that take a reader from absolute novice to the highest professional standard in the note's own subject, with print-safe Mermaid diagrams and SVG figures. Use whenever asked to "fill in", "write", "populate", "rewrite", "create content for" or "add content to" any node, label (e.g. 1.1.1.A.2), title or .md file of a map under main_map/ or derived_maps/.
---

# NoteMaps Content Authoring

The map is **not a roadmap**. It is a **book**: every node is a chapter or
section of a complete guide and knowledge base, written as **study notes**.
A note is judged by one test:

> *Could someone who knows nothing about this subject read this one file and
> come out with mastery of it — the understanding of a researcher, the skill of
> an expert practitioner, and the judgement of a seasoned professional — and
> could they revise from it quickly by skimming?*

This file is tool-agnostic. Claude Code, OpenCode, GitHub Copilot, Cursor or any
other coding agent can follow it. Run all commands from the repository root
(`NoteMaps/`, the folder that contains `source_json/` and `main_map/`).

---

## 0. Quick start — what to do when asked to write a node

A typical request: *"Use skills/notemap-content/SKILL.md and write 1.1.1.A.2"*,
or *"… write A.2 to A.12"*, or *"… write `.../B.6. Forgetting and the Forgetting Curve.md`"*,
or *"… fill in the Working Memory subtopic"*.

1. **Locate the node(s).**
   ```bash
   python scripts/find_node.py 1.1.1.A.2            # full dotted label
   python scripts/find_node.py "forgetting curve"   # words from the title
   python scripts/find_node.py "1.1.1 A" --todo      # every empty note in a subtree
   ```
   It prints the real title, the kind (map / pillar / section / topic /
   subtopic / leaf), the note path, whether it is already written, the
   ancestors, the **siblings** (stay off their subjects) and the **children**
   (for parent chapters), plus the figure filename prefix.
   - A range such as "A.2 to A.12" means each of those labels.
   - If a query is ambiguous, show the matches and ask which one is meant.
2. **Read the reference notes** (§2) — at least the one of the same kind as
   the node being written. They are the approved standard for format, depth,
   tone and figures. Match them.
3. **If the note is already written**, do not overwrite it unless the request
   says to rewrite it; ask first.
4. **Research** the subject (§9).
5. **Plan** the note: the core questions it must answer, the section headings
   (named after ideas), which studies, examples and a case study to use, and
   which visuals (§8). Check the sibling list so the note does not duplicate
   their core subjects.
6. **Write** the note into the existing `.md` (§4–§7) and create its figures in
   the same node folder.
7. **Inspect every SVG** as a PNG, in colour and greyscale, and fix layout
   problems (§8.3).
8. **Validate**: `python scripts/validate_notes.py "<note path>" --render`
   (§10). Fix every error; fix warnings unless there is a genuine reason.
9. **Self-review** against the definition of done (§11).
10. **Report** briefly to the user (§12).

---

## 1. Absolute rules

1. **Write about the subject, never about the map or the document.** Never
   mention the map, pillars, sections, topics, subtopics, notes, "this note",
   "the next note", learning paths, reading time, difficulty levels, badges,
   printing, colour coding, how diagrams are styled or how to read figures.
   No sentence may exist only to describe the document itself.
2. **The novice-to-mastery progression is built into the writing, not
   labelled.** No "Level 1 / Novice / Expert" headings, no ladder tables, no
   badges. Headings name *ideas*; the content climbs from first principles to
   the frontier (§5).
3. **Self-contained.** Everything the reader needs is inside the file.
   - Allowed: researchers' names, dates, studies, experiments, theories, laws,
     organisations, events, book titles — **as long as the note itself explains
     what they found or argued**.
   - Forbidden: anything that sends the reader elsewhere — URLs, reading lists,
     "further reading", "see chapter X", "watch this talk", recommendations to
     read a book or article, links to other notes, wikilinks, `#anchor` links.
   - The only link syntax allowed is an embedded local figure: `![...](fig-....svg)`.
4. **Minimal overlap.** Stay on this node's subject. When a neighbouring idea is
   needed, explain it in a sentence or two — without saying where it is covered.
5. **Truthfulness.** Never invent statistics, effect sizes, studies, quotes or
   dates. If a number is not certain, state the finding qualitatively. Mark
   contested or failed-to-replicate findings as such where they appear.
   Misconceptions are corrected where they naturally arise (in **Watch out**
   boxes) — never in a separate myths section.
6. **Structure belongs to the JSON.** Never create, rename, move or delete a
   node folder or `.md` file. The only files you may add are figures
   (`fig-*.svg`) inside the folder of the note that uses them.
7. **Never run a clean rebuild of `main_map/`** — notes have content.
   `python scripts/build_tree_map.py` on its own is additive and safe.

---

## 2. Reference notes (the approved standard)

The repository owner approved these two notes as exactly the required format.
**Read the matching one before writing, and imitate it.**

| Kind being written | Reference note |
|---|---|
| **Leaf** (`A.1.`-style) | `main_map/Professional Career Development/1. Universal Foundations/1.1. Learning Foundation/1.1.1. Learning Science & Cognition/A. Learning How to Learn/A.1. What is Learning-/A.1. What is Learning-.md` |
| **Parent** (map root, pillar, section, topic, subtopic) | `main_map/Professional Career Development/Professional Career Development.md` |

What to copy from them:

- Opening: a 2–4 sentence concrete hook, then a **Definition** box — no summary
  box, no badges.
- Bullet-dominated body (~300 bullets), only ~5 comparison tables plus the
  Glossary.
- Boxes, study cards, mnemonics, worked examples and case studies in the forms
  shown in §6.
- 5–8 numbered figures, mixing Mermaid diagrams and SVG figures.
- Closing sections: Summary → Self-Check → Answer Key → Glossary.

---

## 3. Repository and tools

```
NoteMaps/
├── source_json/<Map>.json      <- node titles: the source of truth for structure and exact wording
├── main_map/<Map>/             <- one FOLDER per node, leaf or not
│     <node>/<node>.md                the note (write here)
│     <node>/fig-*.svg                the note's figures (create here)
│     <node>/<child>/...              child nodes
├── research_archive/           <- earlier drafts and verified findings: reuse facts, never the style
├── scripts/find_node.py        <- locate nodes, see siblings/children/status, list empty notes
├── scripts/validate_notes.py   <- check written notes (--render also draws every Mermaid diagram)
├── tools/                      <- Mermaid CLI + headless browser (run `npm install` here once)
│     svg_preview.mjs                 render an SVG to PNG (optionally greyscale) for inspection
└── skills/notemap-content/     <- this file
```

**Labels:** Map (plain) · Pillar `N.` · Section `N.N.` · Topic `N.N.N.` ·
Subtopic `A.` · Leaf `A.1.`. Full dotted labels join them: `1.1.1.A.12`.

**Filenames are sanitised** (`? : / \ * < > | "` → `-`), so the file
`A.1. What is Learning-.md` holds the note whose **H1 is the real title**
`# A.1. What is Learning?`. `find_node.py` prints the real title.

**One-time tool setup** (needs Node.js; skip if `tools/node_modules` exists):

```bash
cd tools && npm install && cd ..
```

---

## 4. What each kind of note is

| Node | The note is | How it treats children |
|---|---|---|
| **Leaf** | A complete treatment of one concept, from zero to mastery | — |
| **Subtopic, Topic, Section, Pillar** | A substantive chapter on the *umbrella subject itself*: definition and scope, origins and history, methods, central frameworks, how its parts interact, landmark debates, the state of the field, professional use | Each child's subject gets **one or two sentences at most**, woven into the argument. **Never** list, enumerate, preview or describe the children or the structure |
| **Map root** | A chapter on the whole professional: what professional capability is, how it is built, valued, directed and sustained, and what distinguishes the very best | As above |

---

## 5. How a note teaches (implicit progression)

The reader climbs without being told they are climbing. Cover, in roughly this
order, using headings that name ideas:

1. **From nothing** — plain-language hook with everyday and workplace
   instances; the core definition.
2. **Vocabulary and core model** — terms defined at first use; the central
   model or framework built step by step.
3. **Working understanding** — how it plays out: worked examples, methods,
   procedures, before/after comparisons.
4. **Depth** — mechanisms, competing theories, landmark and recent studies,
   strength and limits of the evidence, boundary conditions, replication status.
5. **Professional mastery** — how experts, organisations and industry use it:
   design decisions, measurement, trade-offs at scale, failure modes, ethics,
   the AI-era picture; at least one realistic **case study**.
6. **Frontier** — an `## Open Questions` section: what is unresolved and why.

**Length:** whatever the concept needs — typically 4,000–6,500 words for a leaf
and 5,000–7,000 for a parent chapter, excluding diagram code. Do not pad; do
not truncate.

---

## 6. Format: study notes

### 6.1 Body form

- **Bullet points are the primary form.** Nested bullets with **bold lead
  words** carry most content: definitions of parts, lists, steps, causes,
  examples (`*e.g.* ...` sub-bullets), studies, case studies.
- Each section may open with a **1–3 line** framing sentence. Use a short
  paragraph (≤ ~4 lines) only where a mechanism or argument genuinely needs
  connected explanation. **No paragraph over ~90 words.**
- **Tables are the exception**: only for a genuine side-by-side comparison of
  two or more things across two or more attributes (e.g. learning vs
  performance; routine vs adaptive expertise; a worked numerical example).
  Never a table for a simple list, timeline, study, case study or
  "term – explanation" listing. Aim for about **five tables per note** plus the
  Glossary.
- **No checklists** (`- [ ]`). No in-text "try this" exercises.
- Numbered lists for procedures and ordered steps.
- Bold the key words so the note can be revised by skimming.

### 6.2 Boxes

Blockquotes with a bold label (no emoji):

| Box | Form | Use |
|---|---|---|
| Definition | `> **Definition — Term:** ...` | every core term, at first use |
| Key point | `> **Key point:** ...` | the one thing to keep from a section |
| Remember | `> **Remember:** ...` | a compact rule or short list to memorise |
| Mnemonic | `> **Mnemonic — NAME:** ...` | a memory aid for a list, where natural |
| Watch out | `> **Watch out:** ...` | a misconception, trap or contested claim |
| Example | `> **Example:** ...` | a short concrete illustration |
| Formula | `> **Formula:** ...` | any calculation, with a worked number |
| In practice | `> **In practice:** ...` | how professionals apply it |

### 6.3 Standard patterns

**Study card** (every important study):

```markdown
**Study card — Tolman and Honzik (1930)**

- **Design:** three groups of rats ran a complex maze daily.
  - Group 1 — rewarded every day.
  - ...
- **Results:** ...
- **Conclusion:** ...
```

**Case study** (at least one per note):

```markdown
### Case study: <short title>

- **Situation:** ...
- **Problem:** ...
- **Diagnosis / Actions:** numbered or nested bullets
- **Result:** ...
- **Side effects / caveats:** (if any)
- **Lesson:** ...
```

**Worked example:** a short situation line, then numbered steps or a small
comparison table, then the conclusion and a **Watch out** if a common error
lurks.

### 6.4 Skeleton

```markdown
# <Label> <Real Title>

<2–4 sentence concrete hook>

> **Definition — <Core term>:** ...

**Why it matters**

- ...

---

## <Idea-named section>
### <Sub-idea>
...

---

## Open Questions

- **<Question>?**
  - <why it is open>

---

## Summary

- <tight recap bullets with bold key terms>

---

## Self-Check

1. <8–15 questions, from basic recall to expert judgement and scenario analysis>

### Answer Key

1. <model answers that explain the reasoning>

---

## Glossary

| Term | Meaning |
|---|---|
| <alphabetical> | <one-line meaning> |
```

Use `---` between major sections. The four closing headings must be exactly
`## Summary`, `## Self-Check`, `### Answer Key`, `## Glossary`, in that order,
with the Glossary last.

---

## 7. Style

- **Formal textbook voice**, third person ("the learner", "a practitioner").
- **British / Indian English**: organisation, behaviour, recognise, analyse,
  centre, colour, modelling, programme (but computer *program*), practise
  (verb) / practice (noun). Proper nouns keep their own spelling (World Health
  Organization).
- Examples from everyday life **and** professional work (software, data,
  consulting, management, finance, healthcare, sales, law, design).
- No emoji. No HTML except `<br/>` inside Mermaid labels. No `<details>`.
- One H1 (the real title); then H2 and H3; never skip a level.

---

## 8. Figures and diagrams

Use visuals wherever they genuinely explain: processes, models, comparisons,
curves, matrices, cycles, decision flows. A note usually has **5–8**. Each gets
a numbered caption about its **content** directly above it:

```markdown
**Figure 2.** Performance during training compared with learning measured later.

![Figure 2. Performance during training compared with learning measured later](fig-A1-learning-vs-performance.svg)
```

- Numbering restarts at 1 in each note and must be sequential.
- **Never** write captions or sentences about the visual conventions ("dashed
  lines mean…", "readable in black and white"). The conventions below are
  instructions for you; design so the meaning is clear from the labels.

### 8.1 Mermaid — print-safe palette

Every diagram must stay readable when printed in black and white: meaning is
carried by **labels, shape, border style and position**; colour only
reinforces. Start every diagram with this exact init line and the classes it
uses:

````markdown
```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Arial, Helvetica, sans-serif','fontSize':'15px','primaryColor':'#FFFFFF','primaryTextColor':'#111111','primaryBorderColor':'#222222','lineColor':'#333333','secondaryColor':'#F2F2F2','tertiaryColor':'#FFFFFF','clusterBkg':'#FAFAFA','clusterBorder':'#555555','edgeLabelBackground':'#FFFFFF','titleColor':'#111111'}}}%%
flowchart TD
    classDef core    fill:#1F3B5C,stroke:#000000,stroke-width:3px,color:#FFFFFF
    classDef key     fill:#BCD5EE,stroke:#1F3B5C,stroke-width:2px,color:#000000
    classDef detail  fill:#FFFFFF,stroke:#333333,stroke-width:1.5px,color:#000000
    classDef accent  fill:#FFE6A8,stroke:#7A5200,stroke-width:2px,stroke-dasharray:8 4,color:#000000
    classDef good    fill:#D3ECD3,stroke:#1E5E24,stroke-width:3px,color:#000000
    classDef caution fill:#F6CACA,stroke:#8B0000,stroke-width:2.5px,stroke-dasharray:3 3,color:#000000
    classDef muted   fill:#E6E6E6,stroke:#666666,stroke-width:1px,stroke-dasharray:2 4,color:#222222
```
````

| Class | Grey-scale signature | Typical use |
|---|---|---|
| `core` | dark fill, white text, thick border | the central concept |
| `key` | light-mid fill, solid border | main components |
| `detail` | white, thin border | details, examples |
| `accent` | very light, long-dash border | techniques, highlights |
| `good` | very light, thick solid border | outcomes, correct practice |
| `caution` | light, dotted border | risks, errors (say so in the label) |
| `muted` | grey, sparse dots | background, optional |

- **Edges:** `==>` main path; `-->` leads to; `-.->` influence or feedback;
  label non-obvious edges (`A -- "causes" --> B`).
- **Layout:** ≤ 15 nodes; prefer `flowchart TD`; labels ≤ ~6 words per line
  (`<br/>` to break); `subgraph`s with titles for groups.
- **Allowed types:** `flowchart`, `sequenceDiagram`, `stateDiagram-v2`,
  `quadrantChart` (alternate `#FFFFFF`/`#F2F2F2` quadrant fills, black points),
  `timeline` and `mindmap` (set `cScale0`… to the light tints and
  `cScaleLabel0`… to `#000000`). **Never `pie`.** Avoid `gitGraph`,
  `xychart-beta`, `block-beta`.
- **Syntax safety:** alphanumeric node ids (never `end`, `graph`, `style`,
  `class`); quote every label `N1["Text (detail)"]`; no `"`, `;`, `{}`, `[]` or
  raw `<` `>` inside labels; apply classes with `class N1,N2 key`; keep the
  init on one line.

### 8.2 SVG figures

Use SVG where shape carries meaning: curves, layered models, spectrums, 2×2
matrices, annotated schematics, before/after bars.

- **File:** in the note's own folder, named with the prefix `find_node.py`
  prints, e.g. `fig-A1-savings.svg`, `fig-0-task-framework.svg`.
- **Canvas:** `viewBox="0 0 960 540"` (or up to `0 0 960 720`),
  `width="100%"`, no fixed height; `font-family="Arial, Helvetica, sans-serif"`.
- **First children:** `<rect width="100%" height="100%" fill="#FFFFFF"/>`,
  `<title>`, `<desc>`.
- **Text:** real `<text>` only; body ≥ 14px, headings 20–24px, fill `#111111`;
  nothing below 13px. Put text over patterns on a white backing `<rect>`.
- **Distinguish without colour:** series by line style (solid / dashed
  `10 6` / dotted `2 4`) **and** direct labels next to the lines; areas by
  pattern + tint. Reusable `<defs>`:
  ```xml
  <defs>
    <pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <rect width="8" height="8" fill="#BCD5EE"/><line x1="0" y1="0" x2="0" y2="8" stroke="#1F3B5C" stroke-width="1.5"/>
    </pattern>
    <pattern id="dots" width="10" height="10" patternUnits="userSpaceOnUse">
      <rect width="10" height="10" fill="#FFE6A8"/><circle cx="5" cy="5" r="1.6" fill="#7A5200"/>
    </pattern>
    <pattern id="cross" width="10" height="10" patternUnits="userSpaceOnUse">
      <rect width="10" height="10" fill="#D3ECD3"/><path d="M0 5H10M5 0V10" stroke="#1E5E24" stroke-width="1"/>
    </pattern>
    <pattern id="lines" width="10" height="10" patternUnits="userSpaceOnUse">
      <rect width="10" height="10" fill="#F6CACA"/><path d="M0 5H10" stroke="#8B0000" stroke-width="1"/>
    </pattern>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0L10 5L0 10z" fill="#222222"/>
    </marker>
  </defs>
  ```
- **Forbidden:** `<foreignObject>`, `<script>`, external images, web fonts,
  `@import`, colour-only legends.
- **Hygiene:** ≥ 24px margins; escape `&` as `&amp;`; must parse as XML.
- **Honesty:** schematic curves say so in the figure's small print
  ("Schematic; not plotted from a single dataset") — that is content.
- Generating figures with a small Python script is fine when there are curves
  or computed coordinates; keep the script outside `main_map/`.

### 8.3 Inspect every SVG

```bash
node tools/svg_preview.mjs "<node folder>/fig-A1-savings.svg" preview.png
node tools/svg_preview.mjs "<node folder>/fig-A1-savings.svg" preview-grey.png grey
```

Open both PNGs (write them outside `main_map/`) and fix overlaps, clipped or
cramped text, labels not clearly attached to their lines, and anything that
becomes indistinguishable in grey. Re-render after every fix.

---

## 9. Research

- **With web search:** research before writing — canonical theory; the latest
  evidence (search with the current and previous year plus "meta-analysis",
  "systematic review", "replication"); applied and industry practice; recent
  developments such as generative AI. Prefer primary, dated, reputable sources.
  Searches may be budgeted per session — front-load the important ones.
- **Without web search:** write from well-established knowledge and from
  `research_archive/` (facts only — never copy its old style), applying rule
  1.5 strictly.
- Sources never appear in the note as things to look up (rule 1.3); describe
  what they found instead.

---

## 10. Validation

```bash
python scripts/validate_notes.py "<note path or folder>" --render
```

- `--render` draws every Mermaid diagram with `tools/` (needs the one-time
  `npm install`); without it only the structural checks run. A custom Mermaid
  CLI can be passed with `--mmdc <path>`.
- On a folder it checks every **written** note beneath it and skips empty ones.
- **Errors (must fix):** missing or out-of-order closing sections; H1 not
  starting with the label; note not in its own folder; meta-language (levels,
  ladders, badges, "this note", map talk, print or diagram-convention talk,
  cross-references, look-it-up pointers); URLs, wikilinks, note links;
  checklists; references/sources/myths sections; `<details>`; emoji; Mermaid
  without the init header or using `pie`; missing, malformed or non-white SVGs;
  non-sequential figure numbers; diagrams that fail to render.
- **Warnings (fix unless there is a real reason):** paragraphs over 90 words;
  less than 60% structured lines; too many table rows relative to bullets;
  missing figure captions; American spellings; short leaf notes.

---

## 11. Definition of done

A note is finished only when all of these hold:

- [ ] Validator passes with `--render` and no unexplained warnings.
- [ ] A complete beginner could follow the opening sections with no prior knowledge.
- [ ] A senior expert would find specific mechanisms, evidence, design decisions
      and recent findings — not generic advice.
- [ ] Every core term has a Definition box at first use; every important study has a study card.
- [ ] At least one case study and one worked example.
- [ ] Bullets dominate; only genuine comparisons are tables; no checklists.
- [ ] Nothing refers to the map, the document, other notes or outside material to look up.
- [ ] No overlap beyond a sentence or two with any sibling listed by `find_node.py`.
- [ ] Every number, date and study is one you are confident of; contested claims are flagged.
- [ ] Every SVG has been viewed in colour and greyscale.
- [ ] British spelling throughout.

(This checklist is for the author. Notes themselves never contain checklists.)

---

## 12. Reporting back

Keep it short:

- which notes were written (as clickable paths), with word and figure counts;
- the validation result;
- anything written from memory rather than verified by search, and any
  contested points you flagged;
- anything you were unsure about, phrased as a question.

---

## 13. Derived maps

A derived map (e.g. `derived_maps/Gen AI & LLMs/`, defined by
`source_json/Gen_AI_and_LLMs.json`) is a learning path built **only from
main-map nodes**: renumbered titles, identical title text, and note content
and figures that are **exact copies** of the main map.

- **Never write or edit content inside `derived_maps/`.** Write the main-map
  note, then re-sync:
  ```bash
  python scripts/sync_derived_map.py source_json/Gen_AI_and_LLMs.json "derived_maps/Gen AI & LLMs"
  ```
  The script copies notes and `fig-*.svg` files byte-for-byte, removes
  anything stale and prints `IDENTICAL TO MAIN MAP` when done. Run it after
  every batch of main-map writing, for every derived map.
- Each derived JSON node has a `source` field (main-map title path); the
  generator script (e.g. `scripts/derive_gen_ai_and_llms.py`) is the place to
  change a derived map's selection or order.
- If a derived map needs a node the main map lacks, add it to the **main**
  JSON first (only where it genuinely belongs there), regenerate `main_map`,
  then regenerate the derived map.
- Validate content in `main_map/`, not in the derived copy: copied notes keep
  their main-map H1 labels by design.
- To find what to write next for a derived map, list its empty notes in learning order:
  `python scripts/sync_derived_map.py <json> <dest> --todo` (prints each empty note with the main-map file to write).

## 14. Writing many notes

- Work one **subtopic** at a time (its leaves first, then its parent chapter),
  so vocabulary and figures stay consistent and overlap is easy to control.
- If parallel agents are used: **at most ~4 at once** (each launches a headless
  browser for checks); give each agent this file, its exact node labels, and the
  rule that it writes only inside its own node folders.
- Run `find_node.py "<subtree>" --todo` to see what remains.
