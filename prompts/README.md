# Prompts

Copy-and-paste prompts for starting a new Claude Code session on this repository. Open the file you need, fill in the `<...>` placeholders, and paste the text inside the code block as your first message.

| File | Use it to |
|---|---|
| `01-write-node-content.md` | Write the content for one node, or a whole subtree, of the main map |
| `02-create-derived-map-structure.md` | Design a new derived map (folders and JSON only, no content), adding missing nodes to the main map first |
| `03-copy-content-to-derived-map.md` | Copy finished main-map notes into a derived map, exactly |
| `04-add-nodes-to-main-map.md` | Add new nodes to the main map (without content) |
| `05-write-many-nodes.md` | Write a large batch of notes with parallel agents, without hanging the laptop |
| `06-progress-report.md` | See what is written, what is empty and what to do next |
| `07-label-illustrative-material.md` | Mark made-up material in existing notes as illustrative |
| `08-verify-facts.md` | Check facts that a writer took from memory |
| `09-extend-short-notes.md` | Bring notes that are under the length target up to it |
| `10-validate-and-repair.md` | Run the checks on notes and fix whatever they report |
| `11-commit-and-push.md` | Commit and push finished work (only when you say so) |

## Repository facts the prompts rely on

- The structure of each map lives in `source_json/<Map>.json`. The folders under `main_map/` or `derived_maps/` mirror it, one folder per node, each holding `<title>.md` and its `fig-*.svg` files.
- The main map is generated from `source_json/Professional_Career_Development.json`. A derived map is generated from its own JSON file in `source_json/` and holds only exact copies of main-map notes.
- Derived maps live on their own branch (for example `derived/gen-ai-and-llms`), not on `main`. The branch is usually worked on through a separate git worktree, so the main checkout is never switched while writers are busy.
- The authoring standard is `skills/notemap-content/SKILL.md`. Every content prompt points to it.
- Never run a script in `scripts/` with `--help` to read its usage. Several of them have no help option and run immediately. Read the top of the file instead.

## Standing rules every prompt repeats

- Ask a question rather than assume.
- Never push unless you say so.
- Never delete `main_map`.
- Never edit `derived_maps/` by hand.
- Keep at most three writing agents running at once, to keep the laptop responsive.
