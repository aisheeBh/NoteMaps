---
name: notemap-audit
description: Audit a NoteMaps knowledge map for currency (missing latest/trending/emerging topics, verified by web search) and for redundancy (duplicated or overlapping nodes), and report findings without modifying anything. Use whenever asked to "check if the map is up to date", "find what's missing", "find redundancies/duplicates", "review the map", or to review coverage of any map under main_map/ or derived_maps/.
---

# NoteMaps Map Audit

Read-only review of a NoteMaps taxonomy. Produces a **report**, never an edit.

## The one rule that overrides everything

**Never add, edit, rename, move, renumber, or delete any node — in `source_json/`, `main_map/`, or `derived_maps/` — unless the repo owner has explicitly approved that specific change in the current conversation.**

The owner's standing instruction is: *additions, removals and edits only happen with my approval.* An audit ends with a written report of proposed changes. Wait for an explicit go-ahead before touching anything. "The map should not have redundancies" is a statement of the target state, **not** permission to start deleting.

If you believe a change is obviously correct, still propose it and stop.

## What this repo actually is

```
NoteMaps/
├── source_json/<Map_Name>.json   <- SOURCE OF TRUTH. Edits belong here.
├── scripts/build_tree_map.py     <- generator: JSON -> one folder per node, each holding <node>.md
├── main_map/<Map Name>/          <- GENERATED. Do not hand-edit.
├── derived_maps/                 <- generated variants
├── docs/
└── skills/                       <- you are here
```

Two facts that change how you work:

1. **Structure is defined by titles, not by note bodies.** Most `.md` files are still empty, but notes are progressively being written (see `skills/notemap-content`). For coverage audits, "content" still means the *node title*: a coverage gap is a missing title, not a missing paragraph. Grep **paths and filenames**, not file contents.
2. **`main_map/` is a build artifact.** `build_tree_map.py` walks the JSON (`{"title": str, "children": [...]}`) and mirrors it to folders. It is additive-only — it creates missing files and never deletes, so stale folders survive a rebuild. Any approved change goes into the JSON first, then regenerate.

### Taxonomy shape

6 levels, fixed vocabulary:

| Depth | Name     | Label form            | Example                                 |
|-------|----------|-----------------------|-----------------------------------------|
| 0     | Map      | plain                 | `Professional Career Development`       |
| 1     | Pillar   | `N.`                  | `3. Career Domains`                     |
| 2     | Section  | `N.N.`                | `3.2. Artificial Intelligence & Data`   |
| 3     | Topic    | `N.N.N.`              | `3.2.13. LLM Engineering & RAG Systems` |
| 4     | Subtopic | `A.`–`L.`             | `C. RAG Architecture & Design`          |
| 5     | Note     | `A.1.`–`A.12.`        | `C.4. Chunking Strategies`              |

**Every node — parent or leaf — is a folder** named after its title, holding `<title>.md` (and any `fig-*.svg` figures). A leaf note therefore lives at `.../<Subtopic>/<Leaf>/<Leaf>.md`. When counting Subtopics with `find -type d`, leaf folders now appear at the next depth down.

**Branching factor is NOT a rule.** A node has as many children as its subject actually needs — no more, no less. There is no target of 12, or 20, or 6. Twelve happens to be the *most common* width (889 of 934 Topics), but that is an observation about this map, not a standard it must meet. Sections legitimately range from 6 to 28 Topics.

Never report a node as defective merely for being 8-wide, 13-wide, or 6-wide, and never pad a node to hit a number. Width is a **symptom to look at, not a metric to conform to.** The only real question is editorial: *does this node cover its subject?* An 8-subtopic Topic that fully covers its subject is correct and finished. A 12-subtopic Topic that misses half its field is not.

Because the tree is so regular, child counts still make a **fast triage filter** — they cheaply surface candidates worth a human read. Note count follows `1 + 13n` for an n-subtopic Topic:

| subtopics | `.md` in Topic |      | subtopics | `.md` in Topic |
|-----------|----------------|------|-----------|----------------|
| 1         | 14             |      | 12        | 157            |
| 2         | 27             |      | 13        | 170            |
| 8         | 105            |      | 14        | 183            |

Use it to *find* things to inspect — a 2-subtopic Topic covering a broad subject probably is thin — then judge each on coverage and say why in those terms. "Only 2 of the ~10 things this subject needs" is a finding. "Not 12" is not.

### Pointer stubs are intentional — do not report them as gaps

Some Topics exist only to cross-reference a canonical Topic elsewhere. They carry **one** Subtopic (~14 `.md`) and their title ends in `— Overview`, `— Navigation Overview`, or `— Strategic Overview`. They are a deliberate navigation device. Flag them only if a stub has drifted into full depth, or if a stub points nowhere.

## Running an audit

Work from a generated path index — it is far faster than walking 140k files repeatedly. Use `rg`/`grep` on the index, not on the filesystem.

```bash
MAP="main_map/Professional Career Development"
SP="${TMPDIR:-/tmp}/notemap-audit"; mkdir -p "$SP"

find "$MAP" -name '*.md' | sed "s|^$MAP/||"            > "$SP/paths.txt"
find "$MAP" -mindepth 2 -maxdepth 2 -type d            > "$SP/L3.txt"   # Topics
find "$MAP" -mindepth 3 -maxdepth 3 -type d            > "$SP/L4.txt"   # Subtopics
cat "$SP/L3.txt" "$SP/L4.txt" | tr 'A-Z' 'a-z'         > "$SP/nodes_lc.txt"
tr 'A-Z' 'a-z' < "$SP/paths.txt"                       > "$SP/paths_lc.txt"
```

PowerShell equivalent, if Bash is unavailable:

```powershell
$Map = "main_map\Professional Career Development"
$sp  = Join-Path $env:TEMP "notemap-audit"; New-Item -ItemType Directory -Force $sp | Out-Null
Get-ChildItem $Map -Recurse -Filter *.md | % FullName | Set-Content "$sp\paths.txt" -Encoding utf8
```

Count nodes per Topic in a single pass. Do **not** loop `find` per directory — it takes minutes *and* it silently corrupts results:

```bash
awk -F/ 'NF>=4 {c[$1"/"$2"/"$3]++} END {for (k in c) print c[k]"\t"k}' "$SP/paths.txt" \
  | sort -n > "$SP/topic_sizes.tsv"
head -40 "$SP/topic_sizes.tsv"     # smallest Topics first — candidates to READ, not defects
```

Read the small ones and judge their coverage. Do not diff them against 157.

**The em-dash trap — this has already produced a wrong audit.** 37 Topic titles contain a literal em-dash (`—`, UTF-8 `e2 80 94`), mostly the `— Overview` pointer stubs. A `while IFS= read -r d; do ... done < list` loop over those paths mis-handles the multibyte sequence under this environment's locale and **emits duplicate rows**, which silently inflated the pointer-stub count from 16 to 30 and dropped three Topics entirely. The single-pass `awk` above is immune. Prefer it always.

**Verify any count against the JSON before reporting it.** The source file is small enough to parse directly and is the authority:

```bash
python -c "
import json; from collections import Counter
d=json.load(open('source_json/Professional_Career_Development.json',encoding='utf-8'))[0]
c=Counter()
def w(n,dep):
    ch=n.get('children') or []
    if dep==3: c[len(ch)]+=1
    for x in ch: w(x,dep+1)
w(d,0); print(dict(sorted(c.items())), 'total topics:', sum(c.values()))"
```

Current map: `{1: 16, 2: 1, 8: 24, 12: 889, 13: 3, 14: 1}`, 934 Topics. This is a *description of the map as it stands*, not a spec — use it to confirm your pipeline is reading the tree correctly. If a filesystem count disagrees with the JSON, **the JSON is right and your shell pipeline is broken.**

### Part 1 — Currency check

Goal: name what a current practitioner would expect to find and does not. Start at the **foundation** layer (Pillar 1) and walk upward — a stale foundation matters more than a stale leaf.

> **Web search is mandatory for this part. Do not audit currency from model knowledge alone.**
>
> Your training cutoff is behind today's date, and this map is explicitly about *latest, trending and emerging* material — exactly the window your knowledge is weakest in. A currency audit done from memory will miss real gaps and will mis-rank the ones it finds. A previous audit of this map ran without search and missed eight significant items, including two that external sources rank in the year's top ten.
>
> If web access is unavailable, say so plainly in the report and label the currency findings **unverified** — do not present them as a completed currency check.

Method:

1. Read the Topic layer in full, one Pillar at a time (`awk -F/ '$1 ~ /^3\./ {print $3}' "$SP/L3.txt"`). 934 Topics is readable; 131k notes is not.
2. For each Section, write down from your own knowledge what the current state of that field includes — tools, standards, roles, practices that are live right now. Do this *before* searching, so the map does not anchor you.
3. **Now search the web** to correct and extend that list. Cover, at minimum:
   - an industry-analyst trend list for the current year (e.g. Gartner's top strategic technology trends)
   - a labour-market source on in-demand skills and emerging roles (e.g. WEF Future of Jobs)
   - a practitioner or hiring source per major Section you are auditing — AI engineering, data engineering, security, software engineering, and whichever domains the map covers
   - the regulatory calendar for anything with a compliance deadline, since enforcement dates move faster than curricula
   
   Search for **roles and job titles**, not just technologies — a new job title is the strongest evidence that a field has become a real career node. Prefer primary and dated sources; note the date of anything you cite.
4. Reconcile the two lists. Items you predicted *and* the web confirms are high-confidence. Items the web raised that you missed are the ones most worth reporting — flag them as such. Items you predicted that the web does not corroborate deserve a second look before you propose them.
5. Test every surviving candidate against the index. Distinguish three outcomes, because they call for different recommendations:
   - **structurally present** — has its own Topic or Subtopic node (`grep -icE "(^|[^a-z])term" "$SP/nodes_lc.txt"`)
   - **buried** — appears only in deep note titles (`"$SP/paths_lc.txt"` hits but no node hit). Often the right fix is promotion, not addition.
   - **absent** — no hits anywhere.
6. Judge *significance*, not novelty. A genuine gap is something a practitioner is expected to know. Vendor churn and short-lived hype are not gaps — this map is structural and expensive to rebuild, so the bar for a new node is "will still matter in two years." Search tells you what is loud right now; it does not tell you what is durable. That judgement is still yours.
7. Cite your sources in the report as markdown links, so the owner can check the basis for each proposal.

Search traps, all of which have produced false results here:

- `grep -c "rag"` matches *sto**rag**e*, *ave**rag**e*. `grep -c "lora"` matches *exp**lora**tory*, *col**labora**tion*. Always anchor: `grep -icE "(^|[^a-z])rag([^a-z]|$)"`.
- A trailing word-boundary kills plurals — `vector database([^a-z]|$)` misses the real node `Vector Databases & Embeddings`. Prefer a leading boundary only: `(^|[^a-z])vector database`.
- `/` is illegal in Windows filenames and `sanitize()` rewrites it to `-`. Search `I-O`, not `I/O`; `CI-CD`, not `CI/CD`; `No-Code - Low-Code`, not `No-Code / Low-Code`.
- `?` and `:` are also rewritten to `-`, so a node titled `What is AI?` is on disk as `What is Artificial Intelligence-`.
- Node titles use a real em-dash (`—`), not a hyphen. `grep 'Salary Negotiation - Overview'` finds nothing; the node is `Salary Negotiation — Overview`. See the em-dash trap above.

### Part 2 — Redundancy check

Three kinds, in rising order of how hard they are to see:

**a. Numbering collisions** — two siblings sharing a number. Always a defect.

```bash
awk -F/ '{print $NF}' "$SP/L3.txt" | sed 's/\. .*//' | sort | uniq -d
```

**b. Title duplication** — the same name in two places.

```bash
# identical Topic titles anywhere in the map
awk -F/ '{t=$NF; sub(/^[0-9.]+\. /,"",t); print t}' "$SP/L3.txt" | sort | uniq -c | awk '$1>1'

# Subtopic titles reused across *different* Sections
awk -F/ '{s=$NF; sub(/^[A-Z]+\. /,"",s); print s"|"$(NF-2)}' "$SP/L4.txt" \
  | sort -u | awk -F'|' '{print $1}' | uniq -d
```

Repetition *within* one domain is usually legitimate — `Performance Optimization` under both Python and Java is correct. Repetition *across* Sections is the signal worth chasing.

**c. Scope overlap** — different titles, same territory. This is the dominant failure mode and no regex finds it. Detect it by comparing the Subtopic sets of two Topics you suspect:

```bash
diff <(ls -1 "$MAP/<topic A>" | grep -v '\.md$' | sed 's/^[A-Z]*\. //') \
     <(ls -1 "$MAP/<topic B>" | grep -v '\.md$' | sed 's/^[A-Z]*\. //')
```

Near-duplicate Topics rarely share wording; they share *shape* — both run Foundations → techniques → tooling → production → career, beat for beat. Read the two lists side by side and judge. Then check `topic_sizes.tsv` to tell the two cases apart: two Topics both built to full depth is real duplication; one full Topic against a 14-note stub is a canonical Topic plus its pointer, which is fine.

High-yield places to look, because they recur in career taxonomies:
- a capability that is both a Section of its own *and* a Topic inside a neighbouring Section
- a skill taught once as a foundation (Pillar 1) and again as a professional skill (Pillar 4) and again as a career activity (Pillar 5)
- a specialisation split across a "classical" Section and a newer dedicated Section

For each overlap, name which copy should be **canonical** and why — but propose, do not merge.

## Reporting

Deliver in the chat. Do not write findings into the map, and do not create report files unless asked.

Structure the report as:

1. **Verdict** — one line on how current the map is overall.
2. **Additions proposed** — grouped by Pillar, foundation layer first. Give each as a placed node: exact parent path, proposed label and number, and one line on why it matters. Separate *promotions* (already present but buried) from genuinely *new* nodes — they are different asks. Mark which items web search corroborated and which came only from your own judgement; the owner should be able to see the difference.
3. **Redundancies found** — collisions first, then title duplicates, then scope overlaps. For each: both paths, note counts, evidence, and a recommended canonical.
4. **Thin or malformed nodes** — Topics whose coverage falls short of their own subject (argued as coverage, never as "not 12"), numbering collisions, and stubs whose titles don't declare themselves. Call intentional pointer stubs intentional.
5. **Sources** — markdown links for every external claim, so each proposal can be checked.
6. **Awaiting approval** — restate that nothing was changed.

Quantify. "15 Subtopic titles are duplicated across Sections in Pillar 2" is actionable; "there is some redundancy" is not.

## If changes are approved

Only after an explicit go-ahead, and only for the nodes approved.

### Tooling that already exists

Use it rather than hand-editing JSON or writing one-off shell:

| Script | Purpose |
|---|---|
| `scripts/_mapkit.py` | load/save, `find`, `rename`, `retitle_body`, `add_topic`, `add_subtopic`, `drop_subtopic`, `stub`, `reletter`, `counts` |
| `scripts/validate_map.py` | label scheme, numbering collisions, duplicate siblings, orphan depths |
| `scripts/check_alignment.py` | proves `main_map/` is an exact mirror of the JSON |
| `scripts/build_tree_map.py` | the generator |

Write changes as a declarative changeset script (`scripts/apply_NN_*.py`) rather than editing JSON by hand — it is reviewable, re-runnable against the backup, and self-documenting.

### Procedure

1. **Back up first:** `cp source_json/<Map>.json source_json/<Map>.json.bak`. Every step below is re-runnable from that backup.
2. Edit the JSON — never the folders.
3. Keep the *labelling* scheme: `N.N.N.` at depth 3, letters `A.`, `B.`, … at depth 4, `A.1.`, `A.2.`, … at depth 5. Letter sequences run past `L.` when a node needs more children — that is allowed. Give a node the number of children its subject requires; do not pad and do not refuse an extra one.
4. Renumbering a sibling cascades through every descendant label. Treat any renumber as a separate approval. Removing a subtopic requires re-lettering its siblings — `mk.drop_subtopic` does this for you.
5. **Prefer stubbing to deleting.** For a redundant topic, collapse it to the map's own pointer-stub idiom (`mk.stub`) instead of removing it: the title gains `— Overview`, the children become a single `A. Overview` whose notes summarise the canonical topic and end in `Full depth covered in Section X.Y`. Navigation from the non-canonical location survives and the duplicated depth disappears. Outright deletion is a separate, heavier decision.
6. Run `python scripts/validate_map.py`. **Do not regenerate until it reports 0 errors.**
7. Regenerate. The generator is **additive-only** — it never deletes, so renames and stubs leave stale folders behind and an in-place rebuild will silently leave the map wrong. A clean rebuild is required:
   ```bash
   find main_map -name '*.md' -size +0 | wc -l   # if NOT 0, notes have content - DO NOT rm -rf
   rm -rf main_map && python scripts/build_tree_map.py   # only when the count above is 0
   ```
   Never run `rm -rf` on that check returning anything but 0. **Notes now have content**, so in practice the step is: run `build_tree_map.py` (additive), then remove only the specific stale folders that `check_alignment.py` reports as EXTRA — after confirming each one holds no written note.
8. Run `python scripts/check_alignment.py`. It must print `ALIGNED` with zero missing and zero extra on both sides. This is the real proof the two representations agree; file counts matching is not sufficient on its own.
9. Re-run the Part 2 redundancy queries to confirm the duplicates you targeted are gone, and spot-check that what remains is facet-level naming (the same word as an aspect of genuinely different subjects, e.g. "Performance Engineering" under Full Stack, SRE and HPC) rather than duplicated depth. Do not chase facet-level overlap — renaming those makes the map worse.
10. Report before/after node counts by depth, and say plainly what was stubbed versus what was deleted.
