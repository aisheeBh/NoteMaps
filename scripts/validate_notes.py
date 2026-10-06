"""Validate written NoteMaps notes against skills/notemap-content/SKILL.md.

Usage:
    python scripts/validate_notes.py <folder-or-file> [--mmdc PATH] [--allow-empty]

Every node is a folder holding <title>.md plus its fig-*.svg figures.
Checks each non-empty .md under the path (empty notes are skipped unless
--allow-empty is NOT given and the path is a single file):
  * single H1 starting with the node label
  * required closing sections: Summary, Self-Check (with Answer Key), Glossary
  * no meta-language about the map, levels, reading, printing or diagram styling
  * no URLs, wikilinks, note links, anchors or look-it-up pointers
  * Mermaid: init header with base theme, no pie charts
  * figures: same-folder fig-*.svg, well-formed, white background, no
    foreignObject/script/external resources
  * no <details>, no emoji
  * American spellings (warning)
With --mmdc every Mermaid block is rendered by the Mermaid CLI (with timeout).
Exit code 1 if any ERROR was found.
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding="utf-8")

REQUIRED_H2 = ["Summary", "Self-Check", "Glossary"]
REQUIRED_H3 = ["Answer Key"]

# Sentences that talk about the document instead of the subject.
META_PATTERNS = [
    (r"^#+\s*Level\s*\d", "level heading"),
    (r"\bLearning Ladder\b", "learning-ladder device"),
    (r"\b(NOVICE|FOUNDATIONS|PRACTITIONER|EXPERT / PRO)\b\s*\]", "level badge"),
    (r"\*\*\[(NOVICE|FOUNDATIONS|PRACTITIONER|ADVANCED|EXPERT)", "level badge"),
    (r"\bReading time\b", "reading time"),
    (r"\bLevel span\b", "level span"),
    (r"\bBuilds on:", "prerequisite badge"),
    (r"\bHow to read it\b", "diagram-reading instruction"),
    (r"\b(black[- ]and[- ]white|greyscale|grayscale|colour print|color print|printout|print-safe)\b", "print talk"),
    (r"\b(dashed|dotted|thick|solid)[- ](border|arrow|line)s?\b[^.\n]{0,40}\b(mean|means|mark|marks|show|shows|indicate|indicates)\b", "diagram-convention talk"),
    (r"\bthis (note|subtopic|topic|section of the map|map|pillar)\b", "talk about the document"),
    (r"\b(the|this) (next|previous|following|preceding) note\b", "pointer to another note"),
    (r"\b(sub)?topic [A-Z]\b|\bnotes? [A-Z]\.\d+\b|\b[A-Z]\.\d+\b(?= (covers|explains|discusses))", "pointer to another note"),
    (r"\b(see|covered in|discussed in|explained in|refer to) (section|chapter|note|subtopic|topic|pillar)\b", "cross-reference"),
    (r"\b(further reading|recommended reading|reading list|suggested reading|watch the (talk|video))\b", "look-it-up pointer"),
]

US_SPELLINGS = re.compile(
    r"\b(organiz\w*|behavior\w*|colors?\b|colored|center(s|ed)?\b|analyz\w*|optimiz\w*|"
    r"recogniz\w*|realiz\w*|prioritiz\w*|summariz\w*|minimiz\w*|maximiz\w*|emphasiz\w*|"
    r"utiliz\w*|favor\w*|honor\w*|labor\b|modeling|modeled|labeled|labeling|traveling|"
    r"defense|catalog\b|gray\b|memoriz\w*|categoriz\w*|conceptualiz\w*|generaliz\w*|"
    r"specializ\w*|standardiz\w*|visualiz\w*|characteriz\w*|internaliz\w*|criticiz\w*|"
    r"apologiz\w*|familiariz\w*|mobiliz\w*|stabiliz\w*|hypothesiz\w*|theoriz\w*)",
    re.I)

LEAF_RE = re.compile(r"^[A-Z]+\.\d+\. ")
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000026FF\U00002700-\U000027BF\U0001F000-\U0001F2FF]")
MERMAID_RE = re.compile(r"```mermaid\s*\n(.*?)```", re.S)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\([^)]*\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]*)\)")


def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check_svg(svg_path, errs):
    name = os.path.basename(svg_path)
    try:
        root = ET.parse(svg_path).getroot()
    except ET.ParseError as e:
        errs.append(f"SVG not well-formed: {name}: {e}")
        return
    raw = open(svg_path, encoding="utf-8").read()
    if "viewBox" not in root.attrib:
        errs.append(f"SVG missing viewBox: {name}")
    if re.search(r"<(\w+:)?(foreignObject|script)\b", raw):
        errs.append(f"SVG uses foreignObject/script: {name}")
    if re.search(r'href="(https?:|//)', raw) or "@import" in raw:
        errs.append(f"SVG has external resource: {name}")
    if not re.search(r'<rect[^>]*(width="100%"[^>]*height="100%"[^>]*fill="#(?i:fff|ffffff)"|fill="#(?i:fff|ffffff)"[^>]*width="100%")', raw):
        errs.append(f"SVG lacks full white background rect: {name}")


def _mmdc(mmdc, src, out, timeout=300):
    # mmdc's headless browser can hang on a loaded machine after writing its
    # output; never let that block validation forever.
    try:
        return subprocess.run([mmdc, "-i", src, "-o", out, "-q"], capture_output=True,
                              text=True, encoding="utf-8", errors="replace",
                              shell=os.name == "nt", timeout=timeout)
    except subprocess.TimeoutExpired:
        stem = os.path.splitext(os.path.basename(out))[0]
        ok = os.path.exists(out) or any(f.startswith(stem) for f in os.listdir(os.path.dirname(out)))
        return subprocess.CompletedProcess([], 0 if ok else 1, "", "" if ok else "Error: mmdc timed out")


def run_mmdc(mmdc, blocks, errs):
    with tempfile.TemporaryDirectory() as td:
        md = os.path.join(td, "all.md")
        with open(md, "w", encoding="utf-8") as f:
            f.write("\n\n".join(f"```mermaid\n{b}```" for b in blocks))
        r = _mmdc(mmdc, md, os.path.join(td, "out.md"), timeout=600)
        bad = []
        for i in range(1, len(blocks) + 1):
            p = os.path.join(td, f"out-{i}.svg")
            if not os.path.exists(p) or "Syntax error" in open(p, encoding="utf-8", errors="replace").read():
                bad.append(i)
        if r.returncode == 0 and not bad:
            return
        for i in bad or range(1, len(blocks) + 1):
            errs.append(f"Mermaid block {i} failed to render")


def check_file(path, args):
    errs, warns = [], []
    kind = "leaf" if LEAF_RE.match(os.path.basename(path)) else "parent"
    text = open(path, encoding="utf-8").read()
    if not text.strip():
        if not args.allow_empty:
            errs.append("empty file")
        return kind, errs, warns

    folder = os.path.basename(os.path.dirname(path))
    if folder != os.path.basename(path)[:-3]:
        errs.append("note is not inside its own node folder")

    prose = strip_code(text)
    h1 = re.findall(r"^# (.+)$", prose, re.M)
    if len(h1) != 1:
        errs.append(f"expected exactly one H1, found {len(h1)}")
    else:
        label = os.path.basename(path)[:-3].split(" ")[0]
        if re.match(r"^([A-Z]+\.|\d)", label) and not h1[0].startswith(label):
            errs.append(f"H1 '{h1[0]}' does not start with label '{label}'")

    h2 = [h.strip() for h in re.findall(r"^## (.+)$", prose, re.M)]
    h3 = [h.strip() for h in re.findall(r"^### (.+)$", prose, re.M)]
    for req in REQUIRED_H2:
        if req not in h2:
            errs.append(f"missing closing section '## {req}'")
    for req in REQUIRED_H3:
        if req not in h3:
            errs.append(f"missing '### {req}'")
    tail = [h for h in h2 if h in REQUIRED_H2]
    if tail and tail != [h for h in REQUIRED_H2 if h in tail]:
        errs.append("closing sections out of order (Summary, Self-Check, Glossary)")
    if h2 and h2[-1] != "Glossary":
        errs.append("Glossary must be the last section")

    for pat, what in META_PATTERNS:
        m = re.search(pat, text, re.M | re.I)
        if m:
            errs.append(f"meta-language ({what}): '{m.group(0)[:60]}'")

    # Study-notes format: flag essay-style paragraphs.
    paras = [p for p in re.split(r"\n\s*\n", prose)
             if p.strip() and not re.match(r"\s*([#>|\-*!]|\d+\.)", p.strip())]
    long_paras = [p for p in paras if len(re.findall(r"\w+", p)) > 90]
    if long_paras:
        warns.append(f"{len(long_paras)} paragraph(s) over 90 words - convert to points/tables: "
                     f"'{long_paras[0].strip()[:60]}...'")
    lines = [l for l in prose.splitlines() if l.strip()]
    structured = [l for l in lines if re.match(r"\s*([-*|>]|\d+\.)", l)]
    if lines and len(structured) / len(lines) < 0.6:
        warns.append(f"only {100 * len(structured) // len(lines)}% of lines are bullets/tables/boxes "
                     "(study notes should be mostly structured)")

    if re.search(r"^\s*[-*] \[[ xX]\]", prose, re.M):
        errs.append("contains a checklist (- [ ]); use bullets instead")
    body = prose.split("\n## Glossary")[0]
    t_rows = len(re.findall(r"^\s*\|", body, re.M))
    bullets = len(re.findall(r"^\s*([-*]|\d+\.) ", body, re.M))
    if t_rows > 0 and t_rows > 0.5 * bullets:
        warns.append(f"table-heavy: {t_rows} table rows vs {bullets} bullets outside the glossary "
                     "(bullets should dominate; tables only for real comparisons)")

    words = len(re.findall(r"\w+", prose))
    if kind == "leaf" and words < 2500:
        warns.append(f"only {words} words - is the subject really this small?")

    blocks = MERMAID_RE.findall(text)
    n_svg = len(IMG_RE.findall(prose))
    if not blocks and not n_svg:
        warns.append("no diagrams or figures")
    for i, b in enumerate(blocks, 1):
        first = b.strip().splitlines()[0] if b.strip() else ""
        if not first.startswith("%%{init:"):
            errs.append(f"Mermaid block {i}: first line must be the %%{{init ...}}%% header")
        elif "'theme':'base'" not in first.replace(" ", "") and '"theme":"base"' not in first.replace(" ", ""):
            errs.append(f"Mermaid block {i}: init must set theme base")
        if re.search(r"^\s*pie\b", b, re.M):
            errs.append(f"Mermaid block {i}: pie charts are not print-safe")

    if re.search(r"https?://|www\.", prose):
        errs.append("contains a URL")
    if "[[" in prose:
        errs.append("contains a wikilink")
    m = LINK_RE.search(prose)
    if m:
        errs.append(f"contains a markdown link: {m.group(0)[:80]}")
    if re.search(r"<details", text, re.I):
        errs.append("contains <details>")
    m = EMOJI_RE.search(text)
    if m:
        errs.append(f"contains emoji: {m.group(0)!r}")
    if re.search(r"^#+\s*(References|Sources|Further Reading|Bibliography|Myths)\b", prose, re.M | re.I):
        errs.append("contains a references/sources/myths section")

    caps = re.findall(r"^\*\*Figure (\d+)\.\*\*", prose, re.M)
    if caps and [int(c) for c in caps] != list(range(1, len(caps) + 1)):
        errs.append(f"figure numbers not sequential from 1: {caps}")
    if len(caps) < len(blocks) + n_svg:
        warns.append(f"{len(blocks) + n_svg} visuals but {len(caps)} '**Figure N.**' captions")

    for src in IMG_RE.findall(prose):
        src = src.strip().strip("<>")
        if "/" in src or "\\" in src or not re.match(r"^fig-[\w.-]+\.svg$", src):
            errs.append(f"image must be a same-folder fig-*.svg: {src}")
            continue
        p = os.path.join(os.path.dirname(path), src)
        if not os.path.exists(p):
            errs.append(f"image not found: {src}")
        else:
            check_svg(p, errs)

    # Prose only (Mermaid/CSS uses 'color'); proper nouns keep their own spelling.
    us_text = re.sub(r"(World Health Organization|Center for Creative Leadership|"
                     r"International Labor|Organization for Economic|Centers for Disease)",
                     "", prose)
    us = sorted({m.group(0).lower() for m in US_SPELLINGS.finditer(us_text)})
    if us:
        warns.append(f"American spellings: {', '.join(us[:12])}")

    if args.mmdc and blocks:
        run_mmdc(args.mmdc, blocks, errs)
    return kind, errs, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--mmdc", default=os.environ.get("MMDC"))
    ap.add_argument("--allow-empty", action="store_true",
                    help="when given a single file, accept it being empty")
    ap.add_argument("--render", action="store_true",
                    help="render Mermaid with the repo's tools/ install (run `npm install` in tools/ once)")
    args = ap.parse_args()
    if args.render and not args.mmdc:
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cand = os.path.join(here, "tools", "node_modules", ".bin", "mmdc.cmd" if os.name == "nt" else "mmdc")
        if not os.path.exists(cand):
            sys.exit(f"--render: {cand} not found. Run `npm install` inside tools/ first.")
        args.mmdc = cand

    if os.path.isfile(args.target):
        files = [args.target]
    else:
        files = []
        for root, _, fs in os.walk(args.target):
            for f in fs:
                p = os.path.join(root, f)
                if f.endswith(".md") and os.path.getsize(p) > 0:
                    files.append(p)
        args.allow_empty = True
    files.sort()

    n_err = n_warn = 0
    for f in files:
        kind, errs, warns = check_file(f, args)
        if errs or warns:
            shown = os.path.relpath(f, args.target) if os.path.isdir(args.target) else f
            print(f"\n[{kind}] {shown}")
            for e in errs:
                print(f"  ERROR  {e}")
            for w in warns:
                print(f"  warn   {w}")
        n_err += len(errs)
        n_warn += len(warns)
    print(f"\nChecked {len(files)} written notes: {n_err} errors, {n_warn} warnings")
    print("PASS" if n_err == 0 else "FAIL")
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
