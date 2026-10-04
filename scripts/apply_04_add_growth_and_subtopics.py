"""Stage 2c - Pillar 4/5 topics, subtopic-level additions, and the
completion of the under-built 1.2.6 topic."""
import sys
sys.path.insert(0, "scripts")
import _mapkit as mk

data = mk.load()
r = mk.root(data)
log = []
T = []

# ---------------------------------------------------------------- 4.10.13
T.append(("4.10. ", "4.10.13", "Working With AI Agents", [
 ("From Using Tools to Delegating Work", [
  "The shift from tool to delegate", "What delegation actually requires",
  "Deciding what is safe to delegate", "Tasks that must stay human",
  "Delegation as a management skill", "Trust calibrated to track record",
  "Starting small and widening scope", "Reversibility as a delegation test",
  "Cost of a bad delegation", "Delegation in regulated work",
  "Personal delegation boundaries", "Building a delegation habit"]),
 ("Briefing an Agent Well", [
  "Stating the outcome you want", "Supplying necessary background",
  "Defining constraints and non-goals", "Success criteria up front",
  "Providing reference examples", "Naming the audience for output",
  "Specifying format and length", "Flagging sensitive material",
  "Setting checkpoints in long tasks", "Clarifying ambiguity before starting",
  "Reusable briefing templates", "Briefing mistakes that waste time"]),
 ("Oversight & Review Practices", [
  "Deciding the right level of review", "Reviewing process versus output",
  "Verifying facts and sources", "Detecting confident errors",
  "Sampling when volume is high", "Second-opinion checks",
  "Knowing your own blind spots", "Reviewing work outside your expertise",
  "Time budgeting for review", "When review costs more than doing",
  "Documenting what you checked", "Building a personal review routine"]),
 ("Accountability & Ownership", [
  "You remain accountable for the output", "Explaining work you did not write",
  "Standing behind delegated decisions", "Disclosure norms at work",
  "Attribution and honesty", "Professional obligations and AI",
  "Liability considerations", "Client and customer expectations",
  "Regulated professions and AI use", "Handling an error that reached others",
  "Apology and correction practice", "Accountability conversations with managers"]),
 ("Designing Agent Workflows", [
  "Mapping a task before automating", "Choosing the automation boundary",
  "Human checkpoints in a workflow", "Handoffs between people and agents",
  "Error handling and fallback paths", "Keeping workflows observable",
  "Versioning your workflows", "Documenting a workflow for others",
  "Testing a workflow before relying on it", "Measuring workflow reliability",
  "Simplifying over-engineered workflows", "Retiring a workflow"]),
 ("Managing Multiple Agents", [
  "Running parallel agent tasks", "Avoiding conflicting work",
  "Coordinating agent outputs", "Context switching costs for you",
  "Tracking what each agent is doing", "Consolidating results",
  "When parallelism stops helping", "Queueing versus parallel execution",
  "Cost of running many agents", "Attention as the real bottleneck",
  "Tooling for multi-agent oversight", "Keeping yourself in control"]),
 ("Risk, Safety & Boundaries", [
  "Setting hard limits for agents", "Actions requiring explicit approval",
  "Financial and legal action safeguards", "Agents and external communication",
  "Data an agent should never access", "Prompt injection awareness",
  "Agents acting on untrusted input", "Recognising manipulated behaviour",
  "Incident response when an agent errs", "Reporting obligations",
  "Insurance and professional risk", "A personal agent risk policy"]),
 ("Quality & Judgement", [
  "Defining good enough for a task", "Where agent output plateaus",
  "Taste and judgement as your edge", "Avoiding regression to generic output",
  "Preserving your voice and standards", "Knowing the domain well enough to judge",
  "Benchmarking agent work against your own", "Recognising diminishing returns",
  "When to take over entirely", "Raising the bar over time",
  "Quality conversations with stakeholders", "Protecting craft standards"]),
 ("Skill Retention & Growth", [
  "Risk of skill atrophy", "Deliberate practice without assistance",
  "Keeping core skills sharp", "Learning through reviewing agent work",
  "Choosing what to stay expert in", "Depth versus breadth decisions",
  "Teaching skills you still perform", "Staying able to work unassisted",
  "Mentoring juniors in an agent era", "Recognising dependence creeping in",
  "Periodic unassisted work", "A personal skills maintenance plan"]),
 ("Team & Organisational Practice", [
  "Agreeing team norms for agent use", "Shared workflows and templates",
  "Visibility into who delegated what", "Avoiding duplicated agent work",
  "Onboarding colleagues to agent practice", "Handling colleague scepticism",
  "Policy compliance in teams", "Procurement and approved tooling",
  "Measuring team-level impact", "Avoiding automation theatre",
  "Redistributing freed-up capacity", "Leading a team that uses agents"]),
 ("Cost, Time & Value", [
  "Measuring time actually saved", "Hidden costs of review and rework",
  "Subscription and usage economics", "Opportunity cost of learning tools",
  "Tasks where agents lose money", "Value beyond speed",
  "Quality-adjusted productivity", "Reporting value to leadership",
  "Avoiding inflated productivity claims", "Reallocating saved time well",
  "Sustainable pace with agents", "Deciding what to keep paying for"]),
 ("Building Your Operating Model", [
  "Auditing your current workload", "Choosing first delegation candidates",
  "Setting your autonomy ladder", "Writing your own agent guidelines",
  "Reviewing and adjusting quarterly", "Keeping a decision log",
  "Sharing what works with peers", "Preparing for more capable agents",
  "Guarding against overreliance", "Maintaining professional identity",
  "Your personal operating principles", "The next three things to try"]),
]))

# ---------------------------------------------------------------- 5.13.13
T.append(("5.13. ", "5.13.13", "AI in Interviews & Assessments", [
 ("How Hiring Has Changed", [
  "AI across the modern hiring funnel", "What employers automate first",
  "Entry-level hiring under pressure", "Volume of applications and its effects",
  "Employer expectations of AI fluency", "Shift toward demonstrated skill",
  "Shorter and more frequent assessments", "What has not changed in hiring",
  "Regional and sector differences", "Reading a modern job posting",
  "Realistic expectations for candidates", "Preparing for the current market"]),
 ("AI Screening & Application Review", [
  "How AI screening tools work", "Resume parsing and structured extraction",
  "Keyword and semantic matching", "Ranking and shortlisting logic",
  "Knockout questions and filters", "Writing applications that parse cleanly",
  "Avoiding formatting that breaks parsers", "Tailoring without keyword stuffing",
  "Detecting and avoiding gimmicks", "Application volume strategy",
  "Following up after screening", "Common screening myths"]),
 ("Asynchronous & Recorded Interviews", [
  "One-way video interview formats", "Automated scoring of responses",
  "Preparing for recorded answers", "Camera, lighting and audio setup",
  "Structuring an answer without a listener", "Time limits and retakes",
  "Managing nerves without an interviewer", "Practising delivery",
  "Accessibility accommodations", "Questioning unfair formats",
  "Evidence on validity of these formats", "Deciding whether to participate"]),
 ("AI-Proctored Assessments", [
  "How remote proctoring works", "Behavioural and environment monitoring",
  "Flagging and false positives", "Privacy implications of proctoring",
  "Preparing your environment", "Technical setup and testing",
  "Accommodation requests", "Challenging an unfair flag",
  "Regulatory scrutiny of proctoring", "Alternatives you can request",
  "Candidate rights", "Reducing proctoring stress"]),
 ("Take-Home Tasks in the AI Era", [
  "Why take-homes changed", "Stated rules on AI assistance",
  "AI-permitted versus AI-prohibited tasks", "Disclosing tool use honestly",
  "Showing your process, not just output", "Scoping effort appropriately",
  "Unpaid work concerns", "Quality bar expectations now",
  "Documenting decisions and trade-offs", "Preparing to defend your submission",
  "Turnaround time expectations", "Declining unreasonable tasks"]),
 ("Live Technical Interviews", [
  "AI-assisted versus unassisted formats", "Pair-programming with an assistant",
  "Interviews that test review skill", "Debugging AI-generated code live",
  "Explaining code you did not write", "Whiteboard and fundamentals questions",
  "System design under AI assumptions", "Communicating reasoning aloud",
  "Handling unfamiliar problems", "Asking clarifying questions",
  "Recovering from a stall", "Practising for both formats"]),
 ("Demonstrating Judgement Over Output", [
  "Why judgement is the new signal", "Explaining why, not just what",
  "Showing trade-off reasoning", "Discussing alternatives rejected",
  "Admitting uncertainty credibly", "Evidence of independent thinking",
  "Depth questions interviewers now ask", "Avoiding memorised answers",
  "Demonstrating domain understanding", "Showing how you verify work",
  "Talking about failures honestly", "Preparing judgement stories"]),
 ("Honesty, Ethics & Disclosure", [
  "Reading the employer's AI policy", "When using AI is cheating",
  "Disclosing assistance proactively", "Misrepresentation risks",
  "Detection tools and their limits", "False accusations and how to respond",
  "Integrity as a long-term asset", "Consequences of discovered deception",
  "Grey areas and how to handle them", "Asking the employer directly",
  "Your own ethical line", "Reputation beyond a single hire"]),
 ("Fairness, Bias & Your Rights", [
  "Bias in automated hiring tools", "Audit requirements in some jurisdictions",
  "Right to explanation of decisions", "Right to human review",
  "Disability accommodations in AI assessments", "Data protection in recruitment",
  "What employers may retain about you", "Questioning an automated rejection",
  "Documenting unfair treatment", "Regulatory complaints routes",
  "Choosing employers by hiring practice", "Advocating for better processes"]),
 ("Preparing With AI Tools", [
  "Mock interviews with an AI partner", "Generating practice questions",
  "Getting feedback on your answers", "Researching companies efficiently",
  "Preparing role-specific material", "Rehearsing salary conversations",
  "Avoiding over-polished unnatural answers", "Keeping your authentic voice",
  "Identifying your real weak spots", "Building a preparation schedule",
  "Tracking preparation progress", "When preparation tools mislead"]),
 ("Standing Out in a Saturated Market", [
  "Why volume applying stopped working", "Targeted applications that land",
  "Referrals and warm introductions", "Public work as evidence",
  "Contributing in relevant communities", "Niche positioning",
  "Direct outreach that works", "Portfolio over promises",
  "Following up without pestering", "Handling long silence and rejection",
  "Maintaining momentum and morale", "A focused search strategy"]),
 ("After the Interview", [
  "Debriefing your own performance", "Thank-you and follow-up messages",
  "Asking for feedback usefully", "Interpreting automated rejections",
  "Negotiating in an AI-screened process", "Evaluating an offer properly",
  "Keeping relationships warm", "Reapplying later effectively",
  "Learning from each loop", "Tracking your pipeline",
  "Deciding when to change approach", "Closing out a search well"]),
]))

# ----------------------------------------------------------------- 5.4.13
T.append(("5.4. ", "5.4.13", "Skills-Based Hiring & Assessment", [
 ("The Shift to Skills-Based Hiring", [
  "What skills-based hiring means", "Why employers moved this way",
  "Degree requirements being dropped", "Evidence behind the shift",
  "Where credentials still dominate", "Sector differences in adoption",
  "Implications for career changers", "Implications for self-taught professionals",
  "Gap between policy and practice", "Reading employer signals",
  "Limits of the skills-based claim", "Positioning yourself accordingly"]),
 ("Identifying Your Skills Honestly", [
  "Separating skills from job titles", "Hard, soft and domain skills",
  "Evidence for each claimed skill", "Proficiency levels and honesty",
  "Skills you have but cannot prove", "Skills you claim but cannot demonstrate",
  "Transferable skills from other fields", "Skills that have become obsolete",
  "Getting external calibration", "Self-assessment traps",
  "Building a personal skills inventory", "Updating it over time"]),
 ("Skills Taxonomies & Frameworks", [
  "Why taxonomies matter to employers", "Common public skills frameworks",
  "Employer internal skills models", "Mapping your skills to a taxonomy",
  "Standard terminology to use", "Skill adjacency and clusters",
  "Levels and progression definitions", "Using frameworks for gap analysis",
  "Limits of rigid taxonomies", "Industry-specific frameworks",
  "Translating across frameworks", "Choosing language employers recognise"]),
 ("Evidence & Proof of Skill", [
  "What counts as credible evidence", "Work samples and artefacts",
  "Public contributions and repositories", "Case studies of your work",
  "Metrics and outcomes you influenced", "References who can speak specifically",
  "Certifications as partial evidence", "Assessment scores and badges",
  "Evidence for confidential work", "Keeping evidence current",
  "Organising an evidence portfolio", "Presenting evidence concisely"]),
 ("Skills Assessments & Tests", [
  "Types of assessment employers use", "Technical skill tests",
  "Situational judgement tests", "Work sample simulations",
  "Cognitive and aptitude tests", "Personality and behavioural inventories",
  "Preparing without over-preparing", "Test anxiety management",
  "Accommodations and accessibility", "Validity of common assessments",
  "Interpreting your results", "When to question an assessment"]),
 ("Micro-Credentials & Badges", [
  "What micro-credentials signal", "Which issuers carry weight",
  "Stackable credential pathways", "Verifying a digital badge",
  "Cost versus signal value", "Employer recognition in practice",
  "Avoiding credential collecting", "Credentials versus demonstrated work",
  "Open badge standards", "Displaying credentials effectively",
  "Expiry and renewal", "Choosing credentials strategically"]),
 ("Writing Skills-Forward Applications", [
  "Leading with capability, not chronology", "Skills-based resume structures",
  "Evidence statements that land", "Quantifying contribution honestly",
  "Tailoring to a skills-based posting", "Handling non-linear career paths",
  "Explaining gaps through skills", "Cover letters focused on capability",
  "Profile summaries that work", "Keywords without stuffing",
  "Formats that survive parsing", "Common application mistakes"]),
 ("Interviewing on Skills", [
  "Structured skills-based interviews", "Competency question patterns",
  "Evidence-led answer structure", "Describing how, not just what",
  "Demonstrating skill live", "Discussing skills you are still building",
  "Handling questions outside your skill set", "Avoiding overclaiming",
  "Asking about skill expectations", "Clarifying the real role requirements",
  "Following up with evidence", "Post-interview skill demonstrations"]),
 ("Closing Skill Gaps Deliberately", [
  "Prioritising gaps that matter", "Fastest credible routes to a skill",
  "Projects that build and prove skill", "Volunteering and contribution routes",
  "Finding feedback on new skills", "Avoiding tutorial-only learning",
  "Setting a realistic timeline", "Measuring genuine progress",
  "Knowing when a skill is job-ready", "Documenting the journey",
  "Avoiding gap-filling for its own sake", "Balancing depth and breadth"]),
 ("Internal Mobility & Skills", [
  "Internal talent marketplaces", "Making your skills visible internally",
  "Skills data in HR systems", "Applying for internal moves",
  "Lateral moves to build skills", "Stretch assignments and projects",
  "Advocating for development budget", "Internal mentors and sponsors",
  "Navigating manager resistance", "Internal versus external moves",
  "Timing an internal transition", "Building an internal reputation"]),
 ("Fairness & Limits of Skills-Based Hiring", [
  "Bias in skills assessment", "Access inequities in proving skill",
  "Unpaid assessment burden", "Skills washing by employers",
  "Over-reliance on test scores", "Credential bias persisting quietly",
  "Candidates disadvantaged by format", "Challenging unfair processes",
  "Employer accountability", "Evidence on what predicts performance",
  "Advocating for better practice", "Choosing fair employers"]),
 ("Building a Skills Strategy", [
  "Aligning skills to career direction", "Market demand research",
  "Durable versus perishable skills", "Investing in rare skill combinations",
  "Reviewing your inventory regularly", "Pruning skills you will not maintain",
  "Planning the next skill to add", "Budgeting time and money",
  "Tracking market signals", "Building proof as you learn",
  "Communicating your skill narrative", "A twelve-month skills plan"]),
]))

for sec, num, title, subs in T:
    log.append("ADD TOPIC " + mk.add_topic(r, sec, num, title, subs))

# ------------------------------------------------------- subtopic additions
SUBS = [
 ("3.2.10.", "Agent Interoperability Protocols (MCP, A2A)", [
  "Why agents need open protocols", "Model Context Protocol overview",
  "MCP servers, clients and transports", "Exposing tools and resources via MCP",
  "Agent2Agent protocol overview", "Agent cards and capability discovery",
  "Delegation between agents", "Authentication across protocol boundaries",
  "Protocol versioning and compatibility", "Governance gaps in current protocols",
  "Building an MCP server", "Choosing protocols for an architecture"]),
 ("3.2.10.", "Agent Security & Sandboxing", [
  "Threat model for autonomous agents", "Prompt injection via tools and content",
  "Confused deputy problems", "Tool permission scoping",
  "Sandboxed execution environments", "Filesystem and network isolation",
  "Credential handling for agents", "Approval gates for risky actions",
  "Rate and spend limits", "Audit logging of agent actions",
  "Detecting compromised agent behaviour", "Incident response for agent systems"]),
 ("3.2.14.", "Context Engineering Fundamentals", [
  "What context engineering is", "Why it superseded prompt tuning",
  "Anatomy of a context payload", "Retrieval system design",
  "Chunking and reranking decisions", "Tool catalog design and deduplication",
  "Instruction layering and precedence", "Few-shot examples as context",
  "Measuring context effectiveness", "Common context failure modes",
  "Context engineering versus fine-tuning", "Building a context strategy"]),
 ("3.2.14.", "Context Budgeting & State Management", [
  "Token budgets as a design constraint", "Deciding what earns context space",
  "Summarisation and compaction strategies", "When to drop versus persist",
  "Short-term and long-term memory design", "Session and cross-session state",
  "Memory retrieval and relevance", "Avoiding context pollution",
  "Context rot over long sessions", "Cost and latency of large contexts",
  "Evaluating a context change", "Patterns for stateful agents"]),
 ("3.2.13.", "Small Language Models & On-Device Inference", [
  "Why small models matter", "Capability versus size trade-offs",
  "Distillation and compression", "Quantisation for edge deployment",
  "On-device runtimes and frameworks", "Mobile and embedded constraints",
  "Privacy benefits of local inference", "Offline and intermittent connectivity",
  "Hybrid local and cloud routing", "Benchmarking small models fairly",
  "Fine-tuning small models", "Choosing between small and large"]),
 ("3.2.13.", "Reasoning Models & Inference-Time Compute", [
  "What reasoning models change", "Test-time compute scaling",
  "Chain-of-thought as a trained behaviour", "Reasoning effort controls",
  "Latency and cost implications", "Tasks that benefit from reasoning",
  "Tasks where reasoning wastes budget", "Evaluating reasoning quality",
  "Reasoning traces and transparency", "Combining reasoning with tools",
  "Routing between model classes", "Operational guidance for reasoning models"]),
 ("3.2.13.", "Domain-Specific Language Models", [
  "The case for domain-specific models", "Continued pretraining on domain data",
  "Instruction tuning for a vertical", "Domain vocabulary and tokenisation",
  "Accuracy gains over general models", "Compliance and auditability benefits",
  "Data requirements and sourcing", "Evaluation with domain experts",
  "Maintenance as the domain changes", "Cost of ownership",
  "Buy versus build for verticals", "Deployment patterns in regulated sectors"]),
 ("3.2.19.", "AI Gateways, Model Routing & Inference Cost Management", [
  "What an AI gateway provides", "Centralised key and credential management",
  "Routing by task difficulty", "Fallback and multi-provider failover",
  "Semantic and exact-match caching", "Rate limiting and quota enforcement",
  "Per-team cost attribution", "Budget alerts and hard caps",
  "Observability at the gateway", "Policy enforcement in the gateway",
  "Latency overhead of a gateway", "Build versus buy for gateways"]),
 ("3.13.7.", "Non-Human & AI Agent Identity", [
  "The non-human identity problem", "Service accounts, workloads and agents",
  "Why agents break human-centric IAM", "Issuing identity to an agent",
  "Short-lived credentials and rotation", "Delegated and on-behalf-of access",
  "Scoping agent permissions tightly", "Workload identity federation",
  "Discovering unmanaged machine identities", "Access review for non-human identities",
  "Detecting compromised agent identity", "Governance model for agent identity"]),
 ("3.13.5.", "Pre-emptive & Predictive Defence", [
  "Moving from reactive to pre-emptive", "Attack surface management",
  "Exposure and reachability analysis", "Predictive vulnerability prioritisation",
  "Automated moving target defence", "Deception technology and honeytokens",
  "Adversary emulation for prediction", "AI-assisted threat anticipation",
  "Pre-emptive patching decisions", "Measuring prevented incidents",
  "Limits and false promise of prediction", "Building a pre-emptive programme"]),
 ("3.14.6.", "ISO/IEC 42001 & AI Management Systems", [
  "What ISO 42001 specifies", "AI management system scope",
  "Clause structure and requirements", "Risk and impact assessment duties",
  "Roles, responsibilities and governance", "Documentation and records",
  "Internal audit of an AIMS", "Certification process and effort",
  "Relationship to ISO 27001", "What certification does not prove",
  "Common implementation pitfalls", "Building an AIMS incrementally"]),
 ("3.14.6.", "Conformity Assessment & AI Assurance", [
  "EU AI Act conformity routes", "High-risk system obligations",
  "Harmonised standards and prEN 18286", "Technical documentation requirements",
  "Notified bodies and self-assessment", "Post-market monitoring duties",
  "Serious incident reporting", "Third-party AI audit practice",
  "Assurance evidence and artefacts", "Red teaming as assurance evidence",
  "Assurance across the supply chain", "Preparing for an AI audit"]),
 ("3.3.2.", "Sovereign Cloud, Data Residency & Geopatriation", [
  "Drivers of digital sovereignty", "Data residency versus data sovereignty",
  "Sovereign cloud offerings", "Geopatriation of workloads",
  "Jurisdiction and lawful access risk", "Regional isolation architectures",
  "Key management and customer-held keys", "Confidential computing for sovereignty",
  "Latency and cost of regional splits", "Operational complexity of sovereignty",
  "Contractual and audit requirements", "Designing a sovereignty strategy"]),
 ("5.3.5.", "Proof-of-Work in the AI Era", [
  "Why finished artefacts prove less now", "Showing process alongside outcome",
  "Documenting decisions and trade-offs", "Build logs and development journals",
  "Live demonstration of capability", "Defending your work in conversation",
  "Contributions with public review history", "Depth over volume in a portfolio",
  "Disclosing AI assistance honestly", "Selecting work that shows judgement",
  "Keeping proof current", "Building a credible evidence trail"]),
]
for pre, title, items in SUBS:
    log.append("ADD SUB   " + mk.add_subtopic(r, pre, title, items))

# ----------------------------------------------- complete the thin 1.2.6 topic
MORE_126 = [
 ("Choosing the Right AI Tool", [
  "Matching tool to task", "General assistants versus specialised tools",
  "Built-in versus standalone tools", "Free and paid tiers compared",
  "Trialling a tool properly", "Reading privacy terms before use",
  "Checking workplace approval", "Avoiding tool sprawl",
  "Switching costs and lock-in", "Comparing output quality",
  "Keeping a shortlist that works", "Deciding what to stop using"]),
 ("AI in Documents & Writing Tools", [
  "Drafting with AI in a word processor", "Rewriting and tone adjustment",
  "Summarising long documents", "Extracting action points",
  "Translating documents", "Formatting and structuring help",
  "Reviewing and proofreading", "Keeping your own voice",
  "Tracking what was AI-written", "Version control and drafts",
  "Confidentiality in document tools", "Practical document workflows"]),
 ("AI in Spreadsheets & Data Tools", [
  "Natural-language formula help", "Explaining an unfamiliar spreadsheet",
  "Cleaning and standardising data", "Summarising a dataset",
  "Generating charts from a request", "Spotting errors and anomalies",
  "Building simple models with help", "Verifying AI-produced calculations",
  "Limits with large spreadsheets", "Sensitive data in spreadsheet tools",
  "Reproducibility of AI-assisted analysis", "When to do it manually"]),
 ("AI in Email & Messaging", [
  "Drafting and replying faster", "Summarising long threads",
  "Tone adjustment for difficult messages", "Translating correspondence",
  "Prioritising and triaging an inbox", "Scheduling and follow-up help",
  "Templates and reusable replies", "Avoiding impersonal communication",
  "Confidentiality in email tools", "Mistakes that reach the wrong people",
  "Disclosure norms for AI-written mail", "Healthy email habits with AI"]),
 ("AI in Meetings & Collaboration", [
  "Automatic transcription and notes", "Meeting summaries and actions",
  "Catching up on a missed meeting", "Consent and recording etiquette",
  "Accuracy limits of transcription", "Speaker attribution errors",
  "Sensitive discussions and recording", "Retention of meeting data",
  "Sharing summaries appropriately", "Accessibility benefits of captions",
  "Reducing meetings with better notes", "Meeting AI ground rules"]),
 ("AI in Search & Research", [
  "AI answers versus traditional search", "Verifying AI-provided facts",
  "Following and checking citations", "Research synthesis across sources",
  "Recognising confident fabrication", "Comparing multiple sources",
  "Deep research modes and their limits", "Bias in retrieved sources",
  "Knowing when to read the original", "Keeping a research trail",
  "Search habits worth preserving", "Effective research workflows"]),
 ("AI in Images, Slides & Media", [
  "Generating images responsibly", "Editing and enhancing images",
  "Building slide decks with AI", "Design suggestions and templates",
  "Audio and video editing help", "Captions and transcripts",
  "Rights and licensing of generated media", "Attribution and disclosure",
  "Brand and style consistency", "Accessibility of generated media",
  "Quality limits to watch for", "Practical media workflows"]),
 ("Privacy & Confidentiality", [
  "What happens to what you type", "Training opt-outs and settings",
  "Personal data in prompts", "Client and employer confidentiality",
  "Regulated data and AI tools", "Enterprise versus consumer accounts",
  "Retention and deletion controls", "Shared and team workspaces",
  "Auditing your own tool use", "Incidents and how to report them",
  "Reading a privacy policy quickly", "A personal confidentiality rule"]),
 ("Verifying & Correcting AI Output", [
  "Treating output as a draft", "Checking facts and figures",
  "Verifying names, dates and quotes", "Testing instructions before following",
  "Recognising plausible-sounding errors", "Cross-checking across tools",
  "Knowing which tasks need full review", "Correcting and re-prompting",
  "When to abandon and do it yourself", "Keeping a record of corrections",
  "Building verification into your routine", "Teaching others to verify"]),
 ("Building Everyday AI Habits", [
  "Starting with one repeated task", "Keeping a prompt library",
  "Measuring whether it actually helps", "Avoiding novelty for its own sake",
  "Protecting skills you want to keep", "Setting personal usage limits",
  "Reviewing your toolset periodically", "Sharing what works with colleagues",
  "Staying current without chasing every release", "Managing subscription costs",
  "Recognising when AI is the wrong tool", "A sustainable personal practice"]),
]
for title, items in MORE_126:
    log.append("ADD SUB   " + mk.add_subtopic(r, "1.2.6.", title, items))

mk.save(data)
print("\n".join(log))
print(f"\nStage 2c complete: {len(log)} operations")
print("node counts by depth:", mk.counts(data))
