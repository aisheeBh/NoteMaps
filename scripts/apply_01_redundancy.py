"""Stage 1 - resolve redundancies, fix the numbering collision, normalise
stub titles. Collapses duplicate depth into the map's own pointer-stub idiom
rather than deleting, so navigation from the non-canonical location survives.
"""
import sys
sys.path.insert(0, "scripts")
import _mapkit as mk

data = mk.load()
r = mk.root(data)
log = []

# ---------------------------------------------------------------- collision
old, new = mk.rename(r, "3.4.13. Operations Management",
                     "3.4.16. Operations Management & Business Process Excellence")
log.append(f"RENUMBER  {old}  ->  {new}")
mk.find(r, "3.4. ")["children"].sort(key=lambda c: mk._numkey(c["title"]))

# ------------------------------------------------- section-title clean-ups
for pre, new_title in [
    ("3.3. ", "3.3. Cloud & Infrastructure Engineering"),
    ("3.9. ", "3.9. Developer Relations & Technical Communication"),
]:
    old, new = mk.rename(r, pre, new_title)
    log.append(f"RENAME    {old}  ->  {new}")

# ------------------------------------------------------- topic-level edits
for pre, new_body in [
    ("3.4.3.",  "Project Management"),
    ("3.1.8.",  "Embedded Systems Development"),
    ("3.1.12.", "Software Delivery & Release Engineering"),
    ("3.5.11.", "Design Systems & Component Libraries"),
    ("1.3.3.",  "Business & Corporate Finance"),
    ("4.5.5.",  "Organizational Knowledge Management"),
    ("3.2.14.", "Prompt & Context Engineering"),
]:
    old, new = mk.retitle_body(r, pre, new_body)
    log.append(f"RETITLE   {old}  ->  {new}")

# ------------------------------- stubs that exist but don't declare themselves
for pre, new_body, canon in [
    ("1.5.2.", "Workplace Writing", "4.14. "),
    ("1.5.3.", "Presenting at Work", "4.13. "),
    ("4.5.3.", "Design Thinking", "4.2.3."),
]:
    t = mk.stub(r, pre, new_body, canon)
    log.append(f"STUBTITLE {pre} -> {t}")

# ------------------------------------------------------ redundancy -> stubs
# (prefix, new body text, canonical prefix, label shown in the pointer note)
STUBS = [
    # identical titles in two places
    ("3.3.12.",  "Digital Forensics & Incident Response", "3.13.9.", "3.13.9"),
    ("5.4.9.",   "Salary Negotiation & Offer Evaluation",  "5.13.9.", "5.13.9"),
    ("5.1.10.",  "Career Risk Management",                 "5.8.9.",  "5.8.9"),
    ("4.3.12.",  "Strategic Leadership",                   "4.1.6.",  "4.1.6"),
    ("4.8.5.",   "Networking & Relationship Building",     "5.3.9.",  "5.3.9"),
    ("4.15.6.",  "Networking & Relationship Building",     "5.3.9.",  "5.3.9"),
    ("4.11.10.", "Networking for Career Growth",           "5.3.9.",  "5.3.9"),
    ("1.5.6.",   "Leadership Communication",               "4.1.11.", "4.1.11"),
    ("5.7.5.",   "Cross-Cultural Communication",           "4.12.2.", "4.12.2"),
    ("4.8.4.",   "Community Building",                     "3.9.8.",  "3.9.8"),
    # a whole section shadowed by one topic elsewhere
    ("3.7.8.",   "Robotics Engineering",                   "3.28. ",  "3.28"),
    ("3.7.7.",   "Computational Biology & Bioinformatics", "3.27. ",  "3.27"),
    ("3.5.10.",  "AR, VR & XR Design",                     "3.18. ",  "3.18"),
    ("3.9.2.",   "Developer Experience",                   "3.15. ",  "3.15"),
    ("3.3.9.",   "Cybersecurity Engineering",              "3.13. ",  "3.13"),
    ("3.3.11.",  "Governance, Risk & Compliance",          "3.13. ",  "3.13"),
    # scope overlap, same altitude
    ("3.3.10.",  "Cloud Security",                         "3.13.3.", "3.13.3"),
    ("3.23.9.",  "Performance Engineering",                "3.1.16.", "3.1.16"),
    ("3.14.8.",  "Data Privacy Engineering",               "3.13.8.", "3.13.8"),
    ("3.9.10.",  "Developer Advocacy",                     "3.9.1.",  "3.9.1"),
    ("3.9.7.",   "Technical Evangelism",                   "3.9.1.",  "3.9.1"),
    ("3.9.9.",   "Open Source Programs",                   "3.21.10.", "3.21.10"),
    ("3.4.5.",   "Solution Architecture",                  "3.8.3.",  "3.8.3"),
    ("3.8.8.",   "Pre-Sales Engineering",                  "3.8.9.",  "3.8.9"),
    ("2.6.11.",  "Assembly Language Programming",          "2.13.4.", "2.13.4"),
    ("1.7.7.",   "Economic Concepts",                      "1.3.2.",  "1.3.2"),
    ("4.4.2.",   "Time Management & Productivity",         "1.1.6.",  "1.1.6"),
    ("4.7.6.",   "Personal Knowledge Management",          "1.1.6.",  "1.1.6"),
    ("4.2.2.",   "Creative Thinking",                      "4.5.1.",  "4.5.1"),
    ("4.11.3.",  "Personal Branding Essentials",           "5.3.1.",  "5.3.1"),
    ("4.11.9.",  "Career Transitions & Pivots",            "5.8. ",   "5.8"),
    ("4.8.7.",   "Public Speaking & Thought Leadership",   "4.13. ",  "4.13"),
    ("5.3.8.",   "Public Speaking & Professional Communication", "4.13. ", "4.13"),
]
for pre, b, canon, ref in STUBS:
    t = mk.stub(r, pre, b, canon, ref)
    log.append(f"STUB      {pre:9s} -> {t}   (canonical {ref})")

# ------------------------------- duplicated subtopics inside one section group
for topic, sub, keep in [
    ("1.1.2.", "Note-Taking Systems",          "1.1.6.B"),
    ("1.1.3.", "Mental Models",                "1.1.5.K"),
    ("1.1.4.", "Personal Knowledge Management", "1.1.6.C"),
]:
    t = mk.drop_subtopic(r, topic, sub)
    log.append(f"DROPSUB   {sub!r} from {t}  (canonical {keep})")

mk.save(data)
print("\n".join(log))
print(f"\nStage 1 complete: {len(log)} operations")
print("node counts by depth:", mk.counts(data))
