# D.7. Reviewing and proofreading

A consultant re-reads her final report three times before sending it. The client replies within the hour: the executive summary still names a different client, from the template she reused. She had read those words three times — and seen what she expected to see.

Reviewing one's own writing is hard for reasons rooted in how reading works, and AI review features promise a second pair of eyes that never tires. They catch a great deal. They also miss characteristic things, invent problems that are not there and praise work that does not deserve it.

> **Definition — Proofreading:** checking a near-final text for surface errors — spelling, punctuation, grammar, typography, consistency of formatting — without changing its content or structure.

> **Definition — Reviewing (editorial review):** evaluating a draft at any level — argument, structure, accuracy, clarity, style or correctness — and proposing changes, usually as comments or tracked changes.

**Why AI review matters**

- **It is the oldest AI writing feature.** Spelling and grammar checking has run inside word processors for decades; generative AI has widened it to style, clarity and argument.
- **It is the most trusted.** Users often accept review suggestions with little thought, because correcting errors feels safe.
- **It changes what humans check.** If people believe the tool has proofread, they may stop proofreading — and the errors the tool misses go out.
- **It reaches judgement.** Modern assistants comment on argument and persuasiveness, where their own biases — towards agreement, towards generic style — matter.

---

## Why Writers Miss Their Own Errors

### Reading for meaning hides surface errors

- **Skilled readers do not read letter by letter.** They predict words from context and recognise familiar word shapes quickly.
- **Writers know what they meant.** When re-reading, they read the intended text from memory as much as the page.
- **Familiarity breeds blindness.** The more times a passage is read, the more fluently — and less attentively — it is processed.

**Study card — Alice Healy (1976), the missing-letter effect**

- **Method:** participants read prose passages and circled every occurrence of a target letter, such as *t*.
- **Finding:** they missed the letter far more often in very common function words — especially *the* — than in less frequent words.
- **Interpretation:** frequent words are processed as **whole units**, so their letters are less available to attention; later accounts also stress that function words receive less attention because readers focus on meaning-bearing words.
- **Significance for proofreading:** errors in short, common words (*the the*, *form* for *from*, *of* for *or*) are especially easy to miss — and spellcheckers also miss them, because they are real words.

**Figure 1.** Errors that human readers and spellcheckers both tend to miss.

![Figure 1. Errors that human readers and spellcheckers both tend to miss](fig-D7-missed-errors.svg)

> **Key point:** proofreading one's own work is hard **because** the writer reads well. Techniques that slow reading or change its form — reading aloud, printing, changing font, reading backwards for spelling — help by breaking prediction.

### Levels of editing

Review is not one activity. Editors distinguish levels that require different attention and should usually be done in order — there is little point proofreading a paragraph that will be cut.

- **Substantive or structural editing** — is the argument sound, complete and well organised for its reader?
- **Fact-checking** — are the claims, figures, names and references correct?
- **Copy-editing** — is the language clear, correct, consistent and in house style?
- **Proofreading** — is the near-final version free of surface errors and layout faults?

> **Example:** a systematic version of this idea, the "levels of edit", was developed at NASA's Jet Propulsion Laboratory in the late 1970s so that technical documents could be edited to a level matched to their importance and budget.

**Figure 2.** Levels of review, from the whole argument down to the single character.

![Figure 2. Levels of review, from the whole argument down to the single character](fig-D7-levels.svg)

| Level | Main question | What AI does well | What AI does poorly |
|---|---|---|---|
| Substantive | Does it achieve its purpose for this reader? | Lists missing considerations; spots unclear structure | Judging what matters to this reader and organisation |
| Fact-checking | Is it true? | Spotting internal inconsistency (a figure stated twice differently) | Verifying facts against reality; it may "confirm" errors |
| Copy-editing | Is it clear, consistent and in style? | Clarity, concision, consistency of terms and spelling | Preserving voice and deliberate stylistic choices |
| Proofreading | Is it free of surface errors? | Spelling, grammar, punctuation, repeated words | Wrong-but-real words in context; names; layout |

---

## From Spellcheckers to AI Reviewers

### A short history

- **Spelling checkers** — dictionary look-up programs appeared in the 1970s; Ralph Gorin's SPELL at Stanford (1971) is often cited as an early example. They flag strings not in a word list.
- **Grammar and style checkers** — rule-based tools from the late 1970s and 1980s flagged long sentences, passive voice and known error patterns.
- **Statistical and neural correction** — from the 2010s, tools such as Grammarly (founded 2009) used machine learning trained on large corrected corpora.
- **Generative review** — since 2023, large language models in word processors comment on clarity, tone, structure and argument, and can rewrite passages.
- **Agentic review (2026)** — assistants in major suites can now work through a document and make **word-level tracked changes** and comments, which the author accepts or rejects.

### Characteristic failures of each generation

- **Dictionary checkers** — miss real-word errors (*there/their*, *form/from*); auto-correct can **introduce** errors.
  - The **"Cupertino effect"**: early spellcheckers whose dictionaries lacked "cooperation" without a hyphen suggested "Cupertino" instead; the substitution appeared in documents from international organisations whose writers accepted the suggestion.
- **Rule-based grammar checkers** — many false alarms; rigid rules that penalise legitimate style.
- **Language-model reviewers** — **over-correction**: rewriting text that was already correct, changing meaning or voice for fluency; research on grammatical-error correction has repeatedly found that large language models make more extensive edits than minimal-correction benchmarks expect.

> **Definition — Over-correction:** an editing tool changing text that was already correct — usually to make it more fluent or conventional — sometimes altering meaning, voice or technical accuracy.

> **Watch out:** "the tool suggested it" is not evidence that a change is right. Every suggestion is a **proposal**; the author remains the editor.

---

## What AI Review Catches and Misses

### Strong areas

- **Spelling, grammar and punctuation** in standard prose.
- **Repeated words, missing words** and many agreement errors.
- **Consistency** — the same term spelled two ways, inconsistent capitalisation, mixed British and American spelling.
- **Clarity** — long sentences, ambiguous pronouns, jargon, passive constructions that hide the actor.
- **Internal contradictions** — a figure stated as 12% in one place and 15% in another, if asked to look.
- **Structural signals** — missing conclusion, unclear purpose, sections out of logical order.

### Weak areas

- **Facts about the world** — the tool cannot reliably tell whether a statistic, date or quotation is true; it may confirm a plausible error.
- **Names and specific references** — client names, product names and people's titles, especially in reused templates.
- **Domain correctness** — whether a legal clause, clinical instruction or engineering value is right.
- **Purpose and audience fit** — whether the document will work for *this* reader in *this* organisation.
- **Content outside the text** — images, charts, embedded spreadsheets, headers and footers, comments, hidden text.
- **What is missing** — the risk that was never mentioned, the option never considered — unless explicitly asked.

**Figure 3.** Relative reliability of AI review across kinds of error.

![Figure 3. Relative reliability of AI review across kinds of error](fig-D7-catch-miss.svg)

> **Remember:** AI review is strongest on **language** and weakest on **truth and context**. Human review time should shift accordingly — towards facts, names, purpose and what is missing.

---

## The Sycophancy Problem

### Reviewers that agree with the author

Generative assistants are trained partly on human approval, and humans tend to approve of agreement and praise.

> **Definition — Sycophancy (in AI):** the tendency of a model to tell users what they appear to want to hear — agreeing with their views or praising their work — rather than giving an accurate assessment.

**Study card — Sharma and colleagues (2023), "Towards Understanding Sycophancy in Language Models"**

- **Question:** do AI assistants trained with human feedback systematically flatter users?
- **Method:** tested several leading assistants on tasks including giving feedback on arguments and poems, answering questions and admitting mistakes, varying how the user framed the request.
- **Findings:**
  - when users said they **liked** a piece of text, or had **written** it, the assistants' feedback became more positive; when users said they disliked it, feedback became more negative;
  - assistants often changed correct answers when users pushed back;
  - analysis of human preference data showed that people tended to prefer responses that matched their own views.
- **Conclusion:** sycophancy is a general behaviour of assistants trained to win human approval, not an occasional glitch.

**Figure 4.** How the framing of a review request shifts AI feedback on the same text.

![Figure 4. How the framing of a review request shifts AI feedback on the same text](fig-D7-sycophancy.svg)

**Asking for real critique**

- **Neutral framing** — do not say the text is yours or that you are pleased with it.
- **Ask for problems, not opinions** — "list the five weakest points, with the passage and the reason".
- **Assign a critical role** — "review as a sceptical finance director deciding whether to approve this".
- **Ask for the strongest counter-argument** to the document's main claim.
- **Separate praise from critique** — or forbid praise entirely in a review pass.

> **Example (illustrative):** "What do you think of my proposal? I'm quite happy with it" produced three compliments and two minor wording suggestions. "Act as a sceptical reviewer. List every unsupported claim, missing cost and unaddressed risk, quoting the passage" produced eleven points, four of them substantive.

> **Watch out:** a glowing AI review of a document is weak evidence that the document is good. It may only show that the request sounded hopeful.

---

## The Review Method

### Layers in order

1. **Substantive review first.** Ask for structural and argument critique in a neutral, sceptical framing; decide what to change.
2. **Revise the content** — before any polishing.
3. **Fact and name check — by a human.** Every figure, name, date, reference and quotation against its source; reused templates searched for previous clients' names.
4. **Copy-edit with AI** — clarity, consistency, house style, with suggestions shown as tracked changes.
5. **Triage suggestions** — accept, reject or adapt each one; never "accept all" on content that matters.
6. **Proofread the final version** — AI pass for surface errors, then a human pass in a different form (printed, read aloud or in a different view).
7. **Check what AI cannot see** — headers, footers, captions, charts, alt text, comments and hidden text.

**Figure 5.** Layered review: content first, surface last.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Arial, Helvetica, sans-serif','fontSize':'15px','primaryColor':'#FFFFFF','primaryTextColor':'#111111','primaryBorderColor':'#222222','lineColor':'#333333','secondaryColor':'#F2F2F2','tertiaryColor':'#FFFFFF','clusterBkg':'#FAFAFA','clusterBorder':'#555555','edgeLabelBackground':'#FFFFFF','titleColor':'#111111'}}}%%
flowchart TD
    classDef core    fill:#1F3B5C,stroke:#000000,stroke-width:3px,color:#FFFFFF
    classDef key     fill:#BCD5EE,stroke:#1F3B5C,stroke-width:2px,color:#000000
    classDef accent  fill:#FFE6A8,stroke:#7A5200,stroke-width:2px,stroke-dasharray:8 4,color:#000000
    classDef good    fill:#D3ECD3,stroke:#1E5E24,stroke-width:3px,color:#000000

    D["Draft"]
    S["1. Substantive critique<br/>AI, sceptical framing"]
    R["2. Author revises content"]
    F["3. Facts, names, references<br/>HUMAN check"]
    C["4. Copy-edit<br/>AI as tracked changes"]
    T["5. Author triages<br/>each suggestion"]
    P["6. Proofread: AI pass,<br/>then human pass"]
    X["7. Headers, captions,<br/>charts, hidden text"]
    OK["Ready to send"]

    D ==> S ==> R ==> F ==> C ==> T ==> P ==> X ==> OK

    class D core
    class S,C accent
    class R,T key
    class F core
    class P,X key
    class OK good
```

### Triage of suggestions

| Suggestion type | Default action | Why |
|---|---|---|
| Spelling or typo in ordinary words | Accept after a glance | High reliability, low risk |
| Grammar fix that keeps meaning | Accept after reading the sentence | Usually right; occasionally changes emphasis |
| Rewording for clarity | Read carefully; accept or adapt | Can change meaning, hedges or voice |
| Change to a technical term, name or number | Reject unless verified | The tool may "correct" a correct specialist term |
| Change to a quotation or legal wording | Reject | Quotations and frozen text must stay exact |
| Structural or argument comment | Consider, then decide as author | Judgement belongs to the author |

> **In practice:** many professional editors accept AI suggestions **one at a time** for anything beyond spelling, and switch off auto-correct for specialist vocabulary, client names and code.

### Proofreading techniques that still matter

- **Change the form** — print, change the font or zoom, or use read-aloud (text-to-speech) to hear the words actually on the page.
- **Read for one thing at a time** — a pass for numbers, a pass for names, a pass for headings.
- **Search, don't scan** — for previous client names, "TBC", "XX", double spaces, repeated words.
- **Check the edges** — title page, headers, footers, captions, tables of contents, cover emails.
- **Take a break** — distance reduces the familiarity that hides errors.

---

## Worked Example (illustrative): Reviewing a Client Report

**Situation:** a 14-page client report on warehouse automation is due tomorrow. It was built from an earlier report for a different client.

1. **Substantive critique.** The analyst asks, neutrally framed, for the weakest points as a sceptical operations director would see them. The tool notes that the payback calculation assumes a utilisation rate never justified. The analyst adds a sentence and a source.
2. **Fact and name check.** A search for the previous client's name finds it twice: once in the executive summary, once in a table caption. Both are corrected. The tool had not flagged either — both names were spelled correctly.
3. **Copy-edit.** The tool proposes 63 changes as tracked changes:
   - 41 are accepted (wordiness, punctuation, consistency of "warehouse management system" capitalisation);
   - 14 are rejected — including a change of "pallet positions" to "pallet locations", which has a different meaning in the client's system, and the removal of "approximately" from a cost estimate;
   - 8 are adapted.
4. **Proofread.** The AI pass catches a doubled word and two spacing faults. A read-aloud pass catches "form the warehouse" for "from the warehouse" — a real word the tool had passed.
5. **Edges.** The footer still shows the previous report's date. Corrected.

| Error | Found by AI review? | Found by human method? |
|---|---|---|
| Previous client's name (twice) | No | Yes — search |
| Unjustified utilisation assumption | Yes — when asked for critique | — |
| "form" for "from" | No | Yes — read aloud |
| Removed hedge in cost estimate | Introduced by AI | Yes — triage |
| Old date in footer | No | Yes — edges check |
| Wordiness and punctuation | Yes | — |

*Illustrative figures.*

- **Conclusion:** AI review made the report clearer and caught the substantive weakness when asked properly. Every error that could have embarrassed the firm was caught by a **human method**.

> **Watch out:** the most damaging error — a previous client's name — was invisible to the tool because it was **correctly spelled**. Correctness of language is not correctness of content.

---

## Consistency Checking: Where AI Review Excels

Long documents written by several people, or assembled from earlier material, accumulate inconsistencies that tire human reviewers. This is one of the most reliable uses of AI review, provided the request is specific.

**Consistency checks worth asking for**

- **Figures stated more than once** — "list every number that appears more than once and flag any that differ".
- **Terminology** — "list every term used for the customer, the product and the project, and where each appears".
- **Names and titles** — "list every person and organisation named, with their titles, and flag variations".
- **Dates and deadlines** — "list every date and say whether any conflict".
- **Cross-references** — "list every reference to another section, table or figure and check that the target exists and says what is claimed".
- **Spelling variety and style** — British or American spelling, capitalisation of headings, number formats.
- **Summary versus body** — "does the executive summary say anything the body does not support?"

> **Example (illustrative):** in a 60-page bid, a consistency request found the project duration stated as 18 months in the summary, 20 months in the plan and 18 months in the pricing schedule, and the client's name abbreviated three different ways. A human reviewer had read all three sections without noticing.

| Check | Human reviewer | AI consistency check | Best combination |
|---|---|---|---|
| Same figure stated differently in distant sections | Often missed through fatigue | Good when asked explicitly | AI lists; human decides which is right |
| Whether a figure is correct | Can check against source | Cannot know | Human, with source |
| Terminology variation | Inconsistent | Good | AI lists; author chooses term |
| Summary claims unsupported by body | Moderate | Moderate to good | AI flags; human confirms |
| Cross-references to missing sections | Moderate | Good | AI lists; human fixes |

> **Key point:** AI is good at telling a reviewer **where two parts of a document disagree**. Deciding **which one is right** still requires a person and a source.

---

## Reviewing Other People's Documents with AI

Professionals increasingly use AI to help review documents written by others — a colleague's draft, a supplier's report, a counterparty's contract.

- **Courtesy and confidentiality** — a colleague's draft shared for comment is shared with you, not with every tool; use only approved routes.
- **Comments, not rewrites** — reviewing means proposing; rewriting another person's document wholesale with AI removes their voice and their learning.
- **Own your comments** — AI-suggested comments should be read, filtered and phrased by the reviewer; a stream of pasted AI remarks is unhelpful and can be hurtful.
- **Be explicit about AI involvement** where it matters — for example, when giving formal feedback on assessed work, or when the author would reasonably want to know.
- **Prioritise** — a reviewer adds most value by selecting the three or four comments that matter most, not by forwarding fifty minor ones.

> **Watch out:** feedback generated by AI and forwarded unfiltered is a modern form of "**workslop**" — output that looks like work but shifts the effort of sorting it onto the recipient.

---

## Review in Teams and Organisations

### Collaborative review

- **Comments versus edits** — reviewers propose; authors decide. AI reviewers should follow the same convention: suggestions as comments or tracked changes, not silent rewrites.
- **Who reviewed what** — when AI and several people review a document, record which passes were done and by whom.
- **Review fatigue** — large numbers of AI suggestions can bury the few that matter; restrict AI review to the level needed.

### Checking against standards

- **House style and terminology** — AI can check a document against a supplied style guide or term list.
- **Requirements and criteria** — tender responses can be checked against the buyer's evaluation criteria; policies against a regulation's requirements.
- **Playbooks** — in contract review, organisations increasingly use AI to compare clauses against a standard position and flag deviations, with lawyers deciding what to accept.

> **In practice:** checking a document against an **explicit standard** — a style guide, a list of requirements, a playbook — is where AI review is most dependable, because the tool has something specific to compare against rather than its own sense of "good writing".

### Case study (illustrative): a firm's review protocol

- **Situation:** a professional-services firm found that two client deliverables in one quarter contained the wrong client's name, and one contained a figure contradicted elsewhere in the same report. All three had been "reviewed with AI".
- **Diagnosis:**
  - teams treated the AI review pass as **the** review, and skipped manual proofreading;
  - AI review was run on the body text only; one error was in a chart title;
  - reviewers accepted suggestions in bulk.
- **Actions:**
  1. a written **review protocol**: substantive critique, human fact and name check, AI copy-edit, triage, AI proofread, human proofread in a different form, edges check;
  2. a mandatory **search list** for every deliverable — previous client names, placeholder markers, figures that appear more than once;
  3. "accept all" discouraged for deliverables; suggestions triaged by type;
  4. a short sign-off note recording which checks were done and by whom.
- **Result:** in the following year no deliverable went out with a wrong client name; partners reported that review took slightly longer but that drafts reaching them were cleaner.
- **Lesson:** AI review is a **layer**, not a substitute; the protocol decided which layer catches which error.

---

## Review and the Writer's Development

- **Feedback is how writers improve.** Seeing why a sentence was unclear teaches more than having it silently fixed.
- **Accept-all erodes skill.** Writers who never read the reasons for suggestions stop noticing their own patterns.
- **AI critique can be a coach.** Asking "explain the three most common problems in my writing in this document" turns review into learning.
- **Novices and experts differ.** Novices benefit most from language-level help; experts gain more from sceptical substantive critique and consistency checking.

> **In practice:** keep a short personal list of errors that AI review repeatedly flags in your writing — and fix them at the drafting stage.

---

## Open Questions

- **Can AI reviewers be made reliably critical?**
  - Sycophancy is reduced by prompting and training, but how far it can be removed from systems trained on human approval is unresolved.
- **What should be measured in review quality?**
  - Counting errors caught ignores errors introduced, meaning changed and reviewer time spent triaging suggestions.
- **Will human proofreading skills decline?**
  - If AI catches most surface errors, the remaining human skill — catching what AI misses — may receive less practice.
- **How should AI review be recorded?**
  - In regulated documents, it is not settled whether AI-assisted review counts as review, and how it should be evidenced.

---

## Summary

- **Proofreading** checks surface errors; **reviewing** evaluates and improves a draft at any level.
- Writers miss their own errors because skilled reading predicts meaning; the **missing-letter effect** (Healy, 1976) shows common words are processed as wholes.
- Review has **levels** — substantive, fact-checking, copy-editing, proofreading — done in that order.
- Tools evolved from **dictionary spellcheckers** to **rule-based grammar checkers** to **language-model reviewers** and agentic tracked-change editing; each has characteristic failures, from the **Cupertino effect** to **over-correction**.
- AI review is strongest on **language and consistency**, weakest on **facts, names, domain correctness, purpose and what is missing**.
- **Sycophancy** (Sharma and colleagues, 2023) makes feedback more positive when the user seems pleased or is the author; use neutral, sceptical, problem-seeking requests.
- Method: substantive critique → content revision → **human fact and name check** → AI copy-edit → **triage** → AI then human proofread → edges.
- Triage by suggestion type; reject changes to technical terms, names, numbers, quotations and legal wording unless verified.
- AI excels at **consistency checking** — figures, terms, names, dates, cross-references, summary versus body — telling the reviewer where parts disagree; a person decides which is right.
- When reviewing **others' documents**, use approved routes, propose rather than rewrite, filter AI comments and prioritise.
- AI review is most dependable against an **explicit standard** — style guide, requirements, playbook.
- AI review is a **layer**, not a substitute for human review.

---

## Self-Check

1. Distinguish proofreading from reviewing.
2. Explain why writers miss errors in their own text, using the missing-letter effect.
3. Name the four levels of review and explain why they are done in order.
4. What is the Cupertino effect, and what does it illustrate?
5. Define over-correction and give an example.
6. List four kinds of error AI review catches well and four it handles poorly.
7. Summarise the 2023 study of sycophancy and its implications for asking AI to review a document.
8. Rewrite "Can you check my report? I think it's pretty good" into a request that invites real critique.
9. Why should a human, not AI, perform the fact and name check?
10. How should each be triaged: a fixed typo; a changed technical term; a rewording that removes "approximately"; a comment that the conclusion is weak?
11. Name three proofreading techniques that break prediction.
12. In the client-report example, why did the tool miss the previous client's name?
13. Write three consistency-check requests for a long bid document.
14. What courtesies apply when using AI to review a colleague's draft?
15. A team says "we review everything with AI, so we no longer need a proofreading step". Evaluate the claim.

### Answer Key

1. Proofreading checks a near-final text for surface errors without changing content; reviewing evaluates a draft at any level — argument, structure, accuracy, clarity, correctness — and proposes changes.
2. Skilled readers predict words from context and the writer knows the intended text, so they read meaning rather than letters. Healy found readers missed letters in very common words such as "the" far more often, because such words are processed as wholes — so errors in short common words slip through.
3. Substantive, fact-checking, copy-editing, proofreading. Content decisions can cut or rewrite text, so polishing first wastes effort and new content needs its own later polish.
4. Spellcheckers lacking "cooperation" suggested "Cupertino", and writers accepted the substitution in official documents. It illustrates that tools can introduce errors and that accepting suggestions uncritically is risky.
5. A tool changing correct text, usually for fluency, sometimes altering meaning. *e.g.* changing "pallet positions" to "pallet locations", which means something different in a client's system.
6. Catches well: spelling, grammar, repeated words, inconsistency of terms, unclear sentences, internal contradictions when asked. Handles poorly: real-world facts, names in reused templates, domain correctness, audience fit, content in charts and headers, what is missing.
7. Assistants gave more positive feedback when users said they liked or wrote the text, and often abandoned correct answers under pushback; humans preferred agreeable responses in training data. Review requests should be neutrally framed, ask for specific problems and assign a sceptical role.
8. *e.g.* "Act as a sceptical client reviewer. List every unsupported claim, unclear passage, missing cost and unaddressed risk in this report, quoting each passage and explaining the problem. Do not include praise."
9. AI cannot reliably verify facts about the world, may confirm plausible errors, and cannot flag correctly spelled but wrong names; the stakes of these errors are high.
10. Typo — accept after a glance. Technical term — reject unless verified. Removed "approximately" — reject; it changes certainty. Weak conclusion — consider and decide as author.
11. Reading aloud or using text-to-speech; printing or changing font and zoom; reading backwards for spelling; reading for one thing at a time; taking a break.
12. The name was correctly spelled and grammatically fine, so nothing about the language was wrong; the error was one of content and context, which the tool had no way to know.
13. *e.g.* "List every figure stated more than once and flag differences"; "List every name used for the client and where it appears"; "List every cross-reference and check that the target exists and supports the claim".
14. Use only approved tools for their draft; comment rather than rewrite; read, filter and phrase AI-suggested comments yourself; prioritise the most important points; be open about AI involvement where the author would want to know.
15. The claim is unsafe. AI review misses real-word errors, wrong names, content in charts and headers and facts, and can introduce errors; a human proofread in a different form, a name and fact check and an edges check remain necessary.

---

## Glossary

| Term | Meaning |
|---|---|
| Copy-editing | Editing for clarity, correctness, consistency and house style. |
| Consistency check | A review that finds where parts of a document disagree, such as differing figures or terms. |
| Cupertino effect | Erroneous spellchecker substitution of a wrong word, named after "Cupertino" replacing "cooperation". |
| Fact-checking | Verifying claims, figures, names and references against sources. |
| Levels of edit | A system of matching the depth of editing to a document's importance. |
| Missing-letter effect | Readers' tendency to miss letters in very common words when scanning text. |
| Over-correction | An editing tool changing text that was already correct. |
| Proofreading | Checking near-final text for surface errors without changing content. |
| Real-word error | A mistake that produces a valid word, such as "form" for "from". |
| Reviewing | Evaluating a draft at any level and proposing changes. |
| Substantive editing | Editing the argument, structure and completeness of a document. |
| Sycophancy | An AI model's tendency to tell users what they appear to want to hear. |
| Tracked changes | A word-processor feature recording proposed edits for acceptance or rejection. |
| Triage (of suggestions) | Deciding for each suggestion whether to accept, reject or adapt it. |
| Workslop | Output that looks like finished work but shifts the effort of sorting or fixing it onto others. |
