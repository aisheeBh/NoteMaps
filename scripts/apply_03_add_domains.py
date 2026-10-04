"""Stage 2b - new Career Domain topics (Pillar 3)."""
import sys
sys.path.insert(0, "scripts")
import _mapkit as mk

data = mk.load()
r = mk.root(data)
log = []
T = []

# ----------------------------------------------------------------- 3.2.21
T.append(("3.2. ", "3.2.21", "LLMOps & AI Observability", [
 ("LLMOps Fundamentals", [
  "What LLMOps covers", "How LLMOps differs from MLOps",
  "The production LLM lifecycle", "Stateless models and stateful systems",
  "Non-determinism as an operational problem", "Quality as a moving target",
  "Roles on an LLMOps team", "Maturity model for LLM operations",
  "Build versus buy decisions", "Common first-year failures",
  "Platform versus per-team ownership", "Starting an LLMOps practice"]),
 ("Tracing LLM & Agent Systems", [
  "Why traces matter more than logs", "Spans for prompts and completions",
  "Tracing multi-step agent runs", "Capturing tool calls and results",
  "Retrieval steps in a trace", "Linking traces to user sessions",
  "OpenTelemetry for LLM workloads", "Semantic conventions for GenAI",
  "Sampling high-volume traces", "Storing and querying traces",
  "Privacy in captured traces", "Reading a trace to find a fault"]),
 ("Evaluation in Production", [
  "Offline versus online evaluation", "Golden datasets and regression suites",
  "LLM-as-a-judge methods", "Judge calibration and bias",
  "Rubric design for quality", "Evaluating trajectories, not just answers",
  "Task success and step efficiency", "Human review workflows",
  "Sampling production traffic for review", "Continuous evaluation pipelines",
  "Evaluation cost control", "Acting on evaluation results"]),
 ("Monitoring Quality & Drift", [
  "Defining quality signals", "Implicit user feedback",
  "Explicit feedback collection", "Detecting prompt drift",
  "Detecting data and retrieval drift", "Model version change impact",
  "Upstream provider changes", "Canary comparison of models",
  "Alerting on quality regressions", "Dashboards that matter",
  "Distinguishing noise from regression", "Quality incident response"]),
 ("Cost, Latency & Token Economics", [
  "Token accounting fundamentals", "Cost per request and per session",
  "Cost attribution by team and feature", "Latency budgets for AI features",
  "Time to first token", "Streaming to improve perceived latency",
  "Caching strategies for LLM calls", "Semantic caching",
  "Batching and concurrency", "Model tiering by task difficulty",
  "Forecasting AI spend", "Cutting cost without cutting quality"]),
 ("Prompt & Configuration Management", [
  "Prompts as versioned artefacts", "Prompt registries",
  "Environment-specific configuration", "Safe prompt rollout",
  "A/B testing prompt variants", "Rollback of a bad prompt",
  "Reviewing prompt changes", "Templating and composition",
  "Linking prompts to evaluations", "Prompt change audit trail",
  "Ownership of prompt content", "Avoiding prompt sprawl"]),
 ("Deployment & Release Practices", [
  "Shadow deployment of models", "Canary and progressive rollout",
  "Feature flags for AI features", "Blue-green model switching",
  "Pinning model versions", "Handling provider deprecations",
  "Multi-provider fallback", "Rollback readiness",
  "Release checklists for AI changes", "Change management and approvals",
  "Coordinating prompt and code releases", "Post-release verification"]),
 ("Reliability & Failure Handling", [
  "Failure modes unique to LLM systems", "Timeouts and retries done right",
  "Partial results and graceful degradation", "Circuit breakers for model calls",
  "Rate limit handling", "Provider outage playbooks",
  "Queueing and backpressure", "Idempotency for agent actions",
  "Guarding irreversible operations", "Dead-letter handling",
  "Chaos testing AI systems", "Reliability targets for AI features"]),
 ("Guardrails & Safety Operations", [
  "Input and output filtering", "Structured output validation",
  "Groundedness and citation checks", "Refusal and escalation paths",
  "PII detection and redaction", "Prompt injection monitoring",
  "Abuse and misuse detection", "Policy enforcement at runtime",
  "Guardrail false-positive management", "Logging blocked interactions",
  "Tuning guardrails over time", "Safety incident handling"]),
 ("Data & Feedback Loops", [
  "Capturing interactions responsibly", "Consent and retention policy",
  "Building datasets from production", "Labelling production samples",
  "Feeding failures into evaluation sets", "Closing the loop to fine-tuning",
  "Avoiding feedback loop contamination", "Detecting model collapse risk",
  "Data minimisation in logs", "Anonymisation of captured data",
  "Dataset versioning", "Governance of production data use"]),
 ("Platform & Tooling", [
  "Observability platforms for LLMs", "Self-hosted versus managed tooling",
  "Instrumentation libraries", "Integrating with existing APM",
  "Gateways as an observability point", "Vector store monitoring",
  "Inference server metrics", "GPU and capacity monitoring",
  "Building an internal AI platform", "Developer experience for AI teams",
  "Tool consolidation decisions", "Evaluating LLMOps vendors"]),
 ("LLMOps Career & Practice", [
  "Skills that define the role", "Overlap with SRE and data engineering",
  "Interview topics for LLMOps roles", "Portfolio projects that demonstrate skill",
  "Working with research and product teams", "On-call for AI systems",
  "Writing runbooks for AI incidents", "Communicating AI reliability to leaders",
  "Keeping current as tooling churns", "Avoiding resume-driven architecture",
  "Building organisational AI maturity", "Career paths from LLMOps"]),
]))

# ----------------------------------------------------------------- 3.1.17
T.append(("3.1. ", "3.1.17", "Internationalization & Localization Engineering", [
 ("i18n Foundations", [
  "Internationalization versus localization", "Why retrofitting i18n is expensive",
  "Locales and locale identifiers", "Language, region and script",
  "Designing for text expansion", "Separating content from code",
  "Externalising user-facing strings", "Resource bundles and catalogs",
  "Fallback chains", "Pseudo-localization testing",
  "i18n in the development lifecycle", "Common i18n mistakes"]),
 ("Text, Encoding & Unicode", [
  "Unicode fundamentals", "UTF-8 and encoding choices",
  "Code points, graphemes and clusters", "Normalization forms",
  "Case conversion pitfalls", "Collation and sorting by locale",
  "String comparison correctness", "Bidirectional text handling",
  "Complex scripts and shaping", "Emoji and variation sequences",
  "Truncation without breaking text", "Encoding bugs and how to find them"]),
 ("Dates, Numbers & Formatting", [
  "Locale-aware date formatting", "Calendars beyond Gregorian",
  "Time zones and offsets", "Daylight saving edge cases",
  "Number and decimal separators", "Currency formatting and codes",
  "Percentages and units", "Measurement systems",
  "Address and name formats", "Phone number handling",
  "Formatting libraries and standards", "Testing format correctness"]),
 ("Pluralization & Grammar", [
  "Plural rules across languages", "CLDR plural categories",
  "Gendered language handling", "Grammatical case and inflection",
  "Avoiding string concatenation", "Message format syntax",
  "Placeholders and ordering", "Context for translators",
  "Avoiding untranslatable idioms", "Inclusive language considerations",
  "Handling untranslated fallbacks", "Linting message strings"]),
 ("Localization Workflow & TMS", [
  "Translation management systems", "Extracting strings for translation",
  "Translation memory and glossaries", "Style guides for translators",
  "Continuous localization pipelines", "Handling in-flight string changes",
  "Review and linguistic QA", "Vendor and community translation",
  "Cost and turnaround planning", "Machine translation in the loop",
  "Post-editing workflows", "Measuring translation quality"]),
 ("Localizing the Product Experience", [
  "Layout and bidirectional interfaces", "Right-to-left mirroring rules",
  "Typography and font coverage", "Images, icons and cultural meaning",
  "Colour connotations across cultures", "Audio, video and captions",
  "Localized search behaviour", "Local payment methods",
  "Regional content and catalogues", "Legal text per jurisdiction",
  "Accessibility across locales", "Cultural adaptation beyond language"]),
 ("Engineering Architecture for i18n", [
  "Locale resolution and negotiation", "Server versus client rendering",
  "URL structure and routing by locale", "SEO for multilingual sites",
  "Caching localized content", "Bundle splitting by locale",
  "Lazy loading translations", "Database storage of multilingual data",
  "Search indexing per language", "API design for localized content",
  "Mobile platform i18n APIs", "Performance cost of localization"]),
 ("Testing & Quality Assurance", [
  "Pseudo-locale testing", "Automated i18n linting",
  "Visual regression across locales", "Text overflow detection",
  "Hardcoded string detection", "Locale-specific test data",
  "Bidirectional layout testing", "Date and number assertion pitfalls",
  "Screenshot review workflows", "Native speaker testing",
  "Regression suites for localization", "Release gates for locales"]),
 ("Scaling to Many Markets", [
  "Choosing which locales to support", "Market prioritisation criteria",
  "Tiered locale support levels", "Adding a new locale efficiently",
  "Deprecating a locale", "Regional compliance differences",
  "Data residency per market", "Local support and operations",
  "Pricing and currency strategy", "Partner and reseller localization",
  "Measuring market performance", "Sunsetting underperforming markets"]),
 ("AI in Localization", [
  "Machine translation quality today", "LLM translation versus traditional MT",
  "Context-aware AI translation", "AI for terminology consistency",
  "Automated linguistic QA", "AI-generated locale variants",
  "Human-in-the-loop post-editing", "Risk of AI translation errors",
  "Brand voice preservation", "Cost impact of AI localization",
  "Evaluating AI translation output", "Where human translators remain essential"]),
 ("Localization Career & Practice", [
  "The localization engineer role", "Working with linguists and vendors",
  "Partnering with product and design", "Advocating for i18n early",
  "Building an i18n platform team", "Tooling ownership",
  "Metrics that demonstrate value", "Common organisational resistance",
  "Standards and industry bodies", "Certifications and communities",
  "Career paths in localization", "Staying current in the field"]),
]))

# ---------------------------------------------------------------- 3.14.13
T.append(("3.14. ", "3.14.13", "Trust & Safety and Content Moderation", [
 ("Trust & Safety Fundamentals", [
  "What trust and safety covers", "History of the discipline",
  "Platform responsibility debates", "Harm taxonomies",
  "Severity and prevalence concepts", "Safety by design principles",
  "Trust and safety versus security", "Stakeholders and competing interests",
  "Team structures and functions", "Vocabulary of the field",
  "Measuring platform health", "Entering the profession"]),
 ("Policy Development", [
  "Writing enforceable content policy", "Defining prohibited content",
  "Edge cases and grey areas", "Context and intent in policy",
  "Cultural and regional variation", "Policy versus community norms",
  "Stakeholder consultation", "Policy testing before launch",
  "Communicating policy to users", "Policy change management",
  "Documenting enforcement rationale", "Reviewing policy effectiveness"]),
 ("Content Moderation Operations", [
  "Proactive versus reactive moderation", "User reporting flows",
  "Moderation queue design", "Prioritisation and triage",
  "Reviewer tooling requirements", "Decision consistency and calibration",
  "Quality assurance sampling", "Service level expectations",
  "Escalation paths", "Handling high-profile cases",
  "Crisis and surge response", "Operational metrics"]),
 ("Automated Detection Systems", [
  "Classifier-based detection", "Hash matching for known content",
  "Perceptual hashing", "Keyword and pattern matching",
  "LLM-assisted classification", "Multimodal detection",
  "Precision and recall trade-offs", "Threshold setting",
  "Human review of automated flags", "Adversarial evasion",
  "Model retraining cadence", "Evaluating detection systems"]),
 ("Harmful Content Categories", [
  "Violent and graphic content", "Hate speech and harassment",
  "Child safety and CSAM obligations", "Self-harm and crisis content",
  "Terrorism and violent extremism", "Fraud and scams",
  "Spam and platform manipulation", "Misinformation and disinformation",
  "Non-consensual intimate imagery", "Regulated goods and services",
  "Impersonation and identity abuse", "Emerging harm categories"]),
 ("Synthetic Media & AI-Generated Harm", [
  "Deepfakes and synthetic video", "Voice cloning abuse",
  "AI-generated CSAM obligations", "Scaled AI-generated spam",
  "Detecting synthetic content", "Provenance signals and watermarks",
  "AI-assisted social engineering", "Labelling AI-generated content",
  "Policy for generative AI outputs", "Platform liability questions",
  "Detection arms race dynamics", "Preparing for synthetic media volume"]),
 ("Enforcement & Appeals", [
  "Enforcement action ladders", "Warnings and temporary restrictions",
  "Account suspension and termination", "Content removal versus reduction",
  "Demonetisation and reach limits", "Proportionality in enforcement",
  "Appeals process design", "Transparency to the affected user",
  "Reinstatement and error correction", "Repeat offender handling",
  "Coordinated behaviour enforcement", "Measuring enforcement accuracy"]),
 ("Regulation & Compliance", [
  "Digital Services Act obligations", "Online Safety Act requirements",
  "Intermediary liability frameworks", "Legal removal requests",
  "Law enforcement cooperation", "Mandatory reporting duties",
  "Transparency report requirements", "Risk assessment obligations",
  "Age assurance requirements", "Cross-border compliance conflicts",
  "Regulator engagement", "Building a compliance evidence trail"]),
 ("Reviewer Wellbeing", [
  "Psychological impact of the work", "Exposure limits and rotation",
  "Content blurring and grayscale tools", "Resilience training",
  "Access to mental health support", "Peer support structures",
  "Signs of vicarious trauma", "Manager responsibilities",
  "Outsourced workforce ethics", "Fair pay and conditions",
  "Designing humane workflows", "Industry standards for wellbeing"]),
 ("Transparency & Accountability", [
  "Transparency report construction", "Metrics worth publishing",
  "External audits and researchers", "Data access for research",
  "Oversight boards and external review", "Explaining decisions publicly",
  "Handling media scrutiny", "Civil society engagement",
  "Documenting policy rationale", "Avoiding transparency theatre",
  "Accountability for mistakes", "Building durable public trust"]),
 ("Trust & Safety Engineering", [
  "Systems that support moderation", "Reviewer tool engineering",
  "Signal pipelines and feature stores", "Abuse detection infrastructure",
  "Rate limiting and friction design", "Account integrity systems",
  "Bot and automation detection", "Graph analysis for coordinated abuse",
  "Privacy-preserving investigation tooling", "Scaling review infrastructure",
  "Latency requirements for enforcement", "Engineering career in trust and safety"]),
 ("Career & Professional Practice", [
  "Roles across trust and safety", "Analyst, policy and engineering tracks",
  "Skills that transfer into the field", "Interviewing for these roles",
  "Ethical dilemmas in practice", "Working under public criticism",
  "Professional communities and conferences", "Staying current with harm trends",
  "Burnout and career sustainability", "Moving between platforms",
  "Consulting and advisory paths", "Leadership in trust and safety"]),
]))

# ---------------------------------------------------------------- 3.14.14
T.append(("3.14. ", "3.14.14", "Digital Provenance & Content Authenticity", [
 ("Why Provenance Matters Now", [
  "Collapse of seeing is believing", "Synthetic media at scale",
  "Provenance versus detection approaches", "Trust signals for content",
  "Who needs provenance and why", "Journalism and evidence integrity",
  "Legal and forensic contexts", "Commercial and brand contexts",
  "Limits of what provenance proves", "Provenance as risk reduction",
  "Current state of adoption", "The case for acting early"]),
 ("C2PA & Content Credentials", [
  "What C2PA specifies", "Content Credentials explained",
  "Manifests, assertions and claims", "Claim signing and certificates",
  "Trust lists and validators", "Binding credentials to media",
  "Durable versus fragile binding", "Reading a credential in practice",
  "Tooling and SDKs", "Platform support status",
  "Known limitations and attacks", "Implementing C2PA in a product"]),
 ("Watermarking Techniques", [
  "Visible versus invisible watermarks", "Statistical text watermarking",
  "Image and video watermarking", "Audio watermarking",
  "Robustness to transformation", "Detection reliability",
  "Watermark removal attacks", "False positive consequences",
  "Open versus proprietary schemes", "Watermarking model outputs",
  "Standards and interoperability", "Where watermarking helps and fails"]),
 ("Cryptographic Foundations", [
  "Digital signatures for media", "Hashing and content identifiers",
  "Certificate authorities and chains", "Key management for signing",
  "Hardware-backed attestation", "Timestamping authorities",
  "Revocation and expiry handling", "Transparency logs",
  "Verifiable credentials concepts", "Decentralised identifiers",
  "Threat model for signing systems", "Cryptographic agility"]),
 ("Capture-Time Provenance", [
  "Signing at the camera", "Secure enclaves on devices",
  "Sensor attestation", "Location and time assertions",
  "Chain of custody from capture", "Editing while preserving provenance",
  "Software that honours credentials", "Breaking the chain inadvertently",
  "Consumer device support", "Professional capture workflows",
  "Verifying capture claims", "Spoofing risks at capture"]),
 ("Provenance for AI-Generated Content", [
  "Disclosing model-generated media", "Provenance in generative pipelines",
  "Model and prompt attribution", "Training data provenance questions",
  "Mixed human and AI authorship", "Agent-generated content provenance",
  "Provenance in code generation", "Document and text provenance",
  "Synthetic data lineage", "Regulatory disclosure requirements",
  "Industry commitments and pledges", "Operationalising AI disclosure"]),
 ("Platform & Distribution Integration", [
  "Preserving metadata through upload", "Metadata stripping by platforms",
  "Displaying credentials to users", "User interface for provenance",
  "Avoiding false assurance", "Handling unsigned content",
  "Search and recommendation signals", "Advertising and sponsored content",
  "Cross-platform credential portability", "Content delivery considerations",
  "Archival and long-term verification", "Platform adoption barriers"]),
 ("Supply Chain Provenance", [
  "Software bill of materials", "Build provenance attestations",
  "SLSA levels explained", "Sigstore and keyless signing",
  "Artifact signing and verification", "Dependency provenance",
  "Model and dataset provenance", "Container image attestation",
  "Policy enforcement on provenance", "Verifying before deployment",
  "Provenance in regulated industries", "Operational rollout patterns"]),
 ("Verification in Practice", [
  "Verifying a claim end to end", "Interpreting a failed verification",
  "Partial and degraded provenance", "Verification user experience",
  "Tooling for journalists", "Tooling for investigators",
  "Enterprise verification workflows", "Automated verification at scale",
  "Logging verification outcomes", "Handling disputed content",
  "Escalation and expert review", "Building verification into process"]),
 ("Policy, Law & Standards", [
  "AI content labelling mandates", "Regional disclosure laws",
  "Evidence admissibility questions", "Standards bodies and consortia",
  "Interoperability between schemes", "Privacy risks of provenance metadata",
  "Anonymity versus accountability tension", "Press freedom considerations",
  "Chilling effects to watch for", "Industry self-regulation",
  "Procurement requirements", "Where regulation is heading"]),
 ("Building a Provenance Programme", [
  "Assessing organisational exposure", "Prioritising content types",
  "Choosing standards to adopt", "Pilot design and scope",
  "Integrating with existing workflows", "Training staff on provenance",
  "Communicating to customers", "Measuring programme value",
  "Handling the unsigned majority", "Vendor selection criteria",
  "Roadmap for phased adoption", "Avoiding provenance theatre"]),
]))

# ---------------------------------------------------------------- 3.12.13
T.append(("3.12. ", "3.12.13", "Agriculture Technology (AgTech)", [
 ("AgTech Landscape", [
  "The agricultural technology sector", "Pressures driving adoption",
  "Smallholder versus industrial farming", "Value chain from field to consumer",
  "Key players and categories", "Regional differences in adoption",
  "Economics of farm technology", "Barriers to adoption on farms",
  "Sustainability drivers", "Food security context",
  "Investment and market trends", "Career entry points"]),
 ("Precision Agriculture", [
  "What precision agriculture means", "Variable rate application",
  "GPS guidance and auto-steer", "Field zoning and prescription maps",
  "Yield mapping and analysis", "Soil sampling strategies",
  "Return on investment analysis", "Equipment interoperability",
  "ISOBUS and machine standards", "Data ownership on the farm",
  "Precision livestock farming", "Implementation in practice"]),
 ("Remote Sensing & Imagery", [
  "Satellite imagery sources", "Drone and UAV imaging",
  "Multispectral and hyperspectral data", "Vegetation indices such as NDVI",
  "Thermal imaging applications", "Image resolution trade-offs",
  "Cloud cover and data gaps", "Georeferencing and orthomosaics",
  "Change detection over seasons", "Crop classification models",
  "Imagery processing pipelines", "Operational imagery workflows"]),
 ("IoT & Farm Sensing", [
  "Soil moisture and nutrient sensors", "Weather station networks",
  "Livestock wearables and tags", "Grain and storage monitoring",
  "Irrigation control systems", "Connectivity in rural areas",
  "LoRaWAN and low-power networks", "Power and battery constraints",
  "Sensor calibration and drift", "Ruggedisation for field conditions",
  "Edge processing on farm", "Sensor network maintenance"]),
 ("Farm Management Software", [
  "Field record keeping", "Crop planning and rotation",
  "Input and inventory management", "Labour scheduling",
  "Compliance and audit records", "Financial management for farms",
  "Equipment maintenance tracking", "Integration with machinery",
  "Mobile-first field usage", "Offline-capable design",
  "Usability for non-technical users", "Evaluating farm software"]),
 ("Agricultural Data Engineering", [
  "Agronomic data models", "Geospatial data handling",
  "Time series from sensors", "Data quality in field conditions",
  "Joining imagery with ground truth", "Standards and data exchange formats",
  "Interoperability across vendors", "Data pipelines for seasonal cycles",
  "Storage and cost considerations", "Privacy and farmer data rights",
  "Data cooperatives and sharing", "Building an agricultural data platform"]),
 ("AI & Modelling in Agriculture", [
  "Yield prediction models", "Disease and pest detection",
  "Weed identification and targeting", "Crop phenotyping",
  "Irrigation optimisation", "Harvest timing models",
  "Computer vision in the field", "Transfer learning with scarce labels",
  "Model performance across geographies", "Explainability for agronomists",
  "Field trials and validation", "Deploying models to farm equipment"]),
 ("Agricultural Robotics & Automation", [
  "Autonomous tractors", "Robotic weeding systems",
  "Harvesting robots and grippers", "Dairy and milking automation",
  "Greenhouse automation", "Spraying drones and regulation",
  "Navigation in unstructured fields", "Safety requirements",
  "Economics of farm robots", "Maintenance and support models",
  "Labour dynamics and automation", "Field deployment lessons"]),
 ("Controlled Environment Agriculture", [
  "Greenhouse technology", "Vertical farming systems",
  "Hydroponics and aeroponics", "Lighting and spectrum control",
  "Climate control systems", "Energy use and economics",
  "Nutrient dosing automation", "Crop selection for indoor growing",
  "Monitoring and control software", "Scaling and unit economics",
  "Failures in the vertical farming sector", "Where indoor growing fits"]),
 ("Supply Chain & Traceability", [
  "Farm to fork traceability", "Food safety compliance",
  "Cold chain monitoring", "Provenance and certification claims",
  "Blockchain claims versus reality", "Commodity grading and quality",
  "Logistics optimisation", "Waste reduction in the chain",
  "Market and price information systems", "Smallholder market access",
  "Retail and consumer transparency", "Traceability system design"]),
 ("Sustainability & Climate", [
  "Carbon measurement on farms", "Soil carbon sequestration",
  "Methane from livestock", "Regenerative agriculture practices",
  "Water stewardship", "Biodiversity monitoring",
  "Fertiliser efficiency and runoff", "Climate adaptation for crops",
  "Carbon credit programmes", "Measurement, reporting and verification",
  "Greenwashing risks", "Technology for sustainable intensification"]),
 ("AgTech Career & Industry", [
  "Roles across the sector", "Engineering roles in AgTech",
  "Data and AI roles in agriculture", "Agronomy plus technology careers",
  "Working with farmers effectively", "Field work expectations",
  "Seasonality in the industry", "Startups versus incumbents",
  "Public sector and research roles", "International development work",
  "Skills that transfer into AgTech", "Building a career in agriculture technology"]),
]))

# ---------------------------------------------------------------- 3.12.14
T.append(("3.12. ", "3.12.14", "Real Estate Technology (PropTech)", [
 ("PropTech Landscape", [
  "What PropTech covers", "Residential, commercial and industrial segments",
  "Value chain from development to occupancy", "Market structure and incumbents",
  "Why real estate digitised late", "Regional market differences",
  "Investment cycles in PropTech", "Business models in the sector",
  "Regulatory environment", "Key industry terminology",
  "Sector challenges", "Career entry points"]),
 ("Listings, Search & Marketplaces", [
  "Listing data standards", "Multiple listing service structures",
  "Search and ranking systems", "Media and virtual tours",
  "Lead generation and routing", "Marketplace trust and verification",
  "Fraud in listings", "Portal economics",
  "Mobile search behaviour", "Personalisation and recommendation",
  "Data licensing and syndication", "Building a listings platform"]),
 ("Transactions & Digital Conveyancing", [
  "The transaction lifecycle", "Digital document workflows",
  "Electronic signature and legal validity", "Title search and insurance",
  "Escrow and settlement systems", "Know your customer requirements",
  "Anti-money-laundering obligations", "Mortgage application technology",
  "Closing coordination platforms", "Jurisdictional variation",
  "Fraud prevention in transactions", "Reducing time to close"]),
 ("Valuation & Market Analytics", [
  "Automated valuation models", "Comparable sales analysis",
  "Hedonic pricing approaches", "Data sources for valuation",
  "Accuracy and confidence intervals", "Model risk in valuation",
  "Market forecasting", "Rental yield analysis",
  "Portfolio analytics", "Geospatial analysis of markets",
  "Bias and fairness in valuation models", "Regulatory scrutiny of AVMs"]),
 ("Property & Facilities Management", [
  "Tenant and lease management", "Maintenance request workflows",
  "Vendor and contractor coordination", "Preventive maintenance programmes",
  "Asset registers and lifecycle", "Service charge management",
  "Inspection and condition reporting", "Resident communication tools",
  "Compliance and safety records", "Portfolio-level operations",
  "Cost control and benchmarking", "Choosing management software"]),
 ("Smart Buildings & Building IoT", [
  "Building management systems", "HVAC monitoring and control",
  "Occupancy and space utilisation sensing", "Access control and smart locks",
  "Energy submetering", "Lighting and automation",
  "Protocols such as BACnet and Modbus", "Integration and middleware layers",
  "Cybersecurity of building systems", "Retrofitting older buildings",
  "Data platforms for buildings", "Measuring smart building value"]),
 ("Construction Technology", [
  "Building information modelling", "Digital twins of buildings",
  "Project scheduling and controls", "Site progress monitoring",
  "Reality capture and scanning", "Prefabrication and modular methods",
  "Safety technology on site", "Procurement and supply chain tools",
  "Cost estimation software", "Quality and defect tracking",
  "Robotics in construction", "Handover to operations"]),
 ("Sustainability & Building Performance", [
  "Energy performance certification", "Operational carbon measurement",
  "Embodied carbon in materials", "Retrofit decision modelling",
  "Net zero building standards", "ESG reporting for property portfolios",
  "Water and waste monitoring", "Indoor environmental quality",
  "Green building certification schemes", "Climate risk to physical assets",
  "Insurance and climate exposure", "Decarbonisation roadmaps"]),
 ("Real Estate Investment Technology", [
  "Portfolio management platforms", "Underwriting automation",
  "Capital raising platforms", "Fractional and tokenised ownership",
  "REIT operations technology", "Debt and lending platforms",
  "Risk analytics for portfolios", "Investor reporting",
  "Due diligence data rooms", "Market intelligence tools",
  "Regulatory considerations", "Evaluating investment technology"]),
 ("Tenant & Occupier Experience", [
  "Workplace experience applications", "Desk and room booking",
  "Hybrid work and space demand", "Amenity and community platforms",
  "Resident apps in residential", "Rent payment technology",
  "Tenant screening and fairness", "Accessibility in building technology",
  "Privacy in occupancy monitoring", "Feedback and satisfaction measurement",
  "Flexible and coworking models", "Designing for occupier value"]),
 ("Data, Standards & Integration", [
  "Property data models", "Address and identifier standards",
  "Geospatial data in real estate", "Open data sources",
  "API integration across systems", "Data quality challenges",
  "System of record decisions", "Legacy system integration",
  "Data privacy for occupants", "Benchmarking data sets",
  "Industry data standards bodies", "Building an integration strategy"]),
 ("PropTech Career & Industry", [
  "Roles across PropTech", "Engineering in real estate technology",
  "Data and analytics roles", "Product management in PropTech",
  "Domain knowledge worth acquiring", "Working with traditional operators",
  "Sales cycles and enterprise buyers", "Startups versus established firms",
  "Public sector and housing roles", "Industry events and communities",
  "Skills that transfer into PropTech", "Building a career in the sector"]),
]))

# ---------------------------------------------------------------- 3.27.13
T.append(("3.27. ", "3.27.13", "Neurotechnology & Brain-Computer Interfaces", [
 ("Neurotechnology Foundations", [
  "What neurotechnology covers", "Reading from versus writing to the nervous system",
  "Neuroanatomy essentials for engineers", "Neural signals and their origins",
  "Clinical versus consumer neurotech", "History of the field",
  "Current state of the art", "Realistic near-term capability",
  "Hype versus evidence", "Key research groups and companies",
  "Terminology of the field", "Entry points for technologists"]),
 ("Signal Acquisition Modalities", [
  "Electroencephalography basics", "Electrocorticography",
  "Intracortical microelectrode arrays", "Functional near-infrared spectroscopy",
  "Magnetoencephalography", "Functional MRI for BCI research",
  "Electromyography and peripheral signals", "Invasive versus non-invasive trade-offs",
  "Spatial and temporal resolution", "Signal-to-noise characteristics",
  "Comparing modalities for a use case", "Emerging acquisition methods"]),
 ("Signal Processing Pipelines", [
  "Amplification and digitisation", "Filtering and artefact removal",
  "Eye blink and muscle artefacts", "Referencing schemes",
  "Epoching and windowing", "Feature extraction methods",
  "Frequency band analysis", "Spatial filtering such as CSP",
  "Dimensionality reduction", "Real-time processing constraints",
  "Latency budgets for control", "Pipeline validation"]),
 ("Decoding & Machine Learning", [
  "Classification of mental states", "Regression for continuous control",
  "Deep learning for neural decoding", "Limited data and subject variability",
  "Cross-subject generalisation", "Calibration sessions and burden",
  "Online adaptation and co-adaptation", "Non-stationarity of neural signals",
  "Evaluation metrics for decoders", "Overfitting risks in small cohorts",
  "Benchmark datasets", "Reproducibility in BCI research"]),
 ("BCI Paradigms", [
  "Motor imagery control", "P300 spellers",
  "Steady-state visual evoked potentials", "Error-related potentials",
  "Attention and workload monitoring", "Speech and language decoding",
  "Handwriting decoding", "Passive versus active BCI",
  "Hybrid BCI approaches", "Shared control with autonomy",
  "Paradigm selection criteria", "Designing a new paradigm"]),
 ("Neural Stimulation & Writing", [
  "Deep brain stimulation", "Transcranial magnetic stimulation",
  "Transcranial direct current stimulation", "Vagus nerve stimulation",
  "Spinal cord stimulation", "Sensory feedback restoration",
  "Closed-loop stimulation systems", "Stimulation parameter optimisation",
  "Safety limits and tissue response", "Adverse effects to monitor",
  "Evidence base for stimulation claims", "Consumer stimulation device concerns"]),
 ("Clinical & Assistive Applications", [
  "Restoring communication in paralysis", "Prosthetic limb control",
  "Exoskeleton and mobility assistance", "Epilepsy monitoring and intervention",
  "Parkinson's disease management", "Stroke rehabilitation",
  "Chronic pain management", "Depression and psychiatric applications",
  "Hearing and vision restoration", "Patient selection criteria",
  "Long-term implant performance", "Outcomes that matter to users"]),
 ("Hardware & Implant Engineering", [
  "Electrode materials and design", "Biocompatibility requirements",
  "Chronic implant stability", "Wireless power and telemetry",
  "Low-power embedded design", "On-device signal processing",
  "Thermal and safety constraints", "Surgical and explant considerations",
  "Device longevity and revision", "Manufacturing and quality systems",
  "Consumer headset engineering", "Reliability testing"]),
 ("Software, Platforms & Standards", [
  "Open BCI software stacks", "Lab Streaming Layer",
  "BIDS and data standards", "Real-time operating constraints",
  "Device drivers and APIs", "Interoperability across hardware",
  "Reproducible research tooling", "Cloud processing of neural data",
  "Security of neural devices", "Firmware update practices",
  "Open hardware communities", "Building a BCI application"]),
 ("Ethics, Privacy & Neurorights", [
  "Mental privacy as a concept", "Neural data sensitivity",
  "Informed consent in neurotech", "Agency and identity concerns",
  "Neurorights legislative proposals", "Consumer data resale risks",
  "Cognitive enhancement debates", "Access and equity questions",
  "Workplace neuromonitoring", "Legal admissibility of neural data",
  "Research ethics in neurotech", "Responsible communication of results"]),
 ("Regulation & Translation", [
  "Medical device classification", "Clinical trial pathways",
  "FDA and CE routes for neurotech", "Breakthrough device designations",
  "Quality management systems", "Risk management standards",
  "Evidence requirements for claims", "Consumer device regulatory gaps",
  "Reimbursement and health economics", "Academic to clinical translation",
  "Funding landscape", "Timeline realism for translation"]),
 ("Neurotech Career & Research", [
  "Roles across the neurotech stack", "Engineering versus neuroscience paths",
  "Essential interdisciplinary skills", "Graduate study considerations",
  "Industry versus academic research", "Working with clinicians and patients",
  "Publishing and conferences in the field", "Open source contribution opportunities",
  "Startups in neurotechnology", "Evaluating claims critically",
  "Long time horizons in the field", "Building a neurotech career"]),
]))

# ---------------------------------------------------------------- 3.28.13
T.append(("3.28. ", "3.28.13", "Physical AI & Embodied Intelligence", [
 ("Physical AI Foundations", [
  "What physical AI means", "Embodiment and intelligence",
  "Difference from software-only AI", "The sim-to-real problem",
  "Why physical AI is hard", "Data scarcity in the physical world",
  "Safety as a first-class constraint", "Current capability frontier",
  "Industry investment landscape", "Terminology of the field",
  "Relationship to classical robotics", "Where physical AI is heading"]),
 ("Foundation Models for Robotics", [
  "Vision-language-action models", "Generalist robot policies",
  "Pretraining on robot demonstrations", "Cross-embodiment transfer",
  "Scaling laws in robot learning", "Open robot foundation models",
  "Fine-tuning for a specific robot", "Prompting a robot policy",
  "Evaluation of generalist policies", "Failure modes of large policies",
  "Compute requirements", "Practical deployment today"]),
 ("World Models & Prediction", [
  "What a world model is", "Learned dynamics models",
  "Video prediction for control", "Latent space planning",
  "Model-based reinforcement learning", "Uncertainty in learned models",
  "Long-horizon prediction errors", "World models for simulation",
  "Evaluating world model quality", "Combining models with planning",
  "Generative simulation environments", "Research directions"]),
 ("Perception for Embodied Systems", [
  "Multimodal sensing fusion", "Depth and 3D perception",
  "Semantic scene understanding", "Object pose estimation",
  "Affordance detection", "Tactile and force sensing",
  "Proprioception and state estimation", "Perception under occlusion",
  "Robustness to lighting and weather", "Latency constraints on perception",
  "On-robot inference optimisation", "Perception failure handling"]),
 ("Manipulation & Dexterity", [
  "Grasp planning and synthesis", "Dexterous multi-finger manipulation",
  "Contact-rich tasks", "Deformable object manipulation",
  "Tool use by robots", "Bimanual coordination",
  "Force control strategies", "Learning from demonstration",
  "Teleoperation for data collection", "Benchmarks for manipulation",
  "Generalising across objects", "Why manipulation remains unsolved"]),
 ("Locomotion & Mobility", [
  "Legged locomotion control", "Wheeled and tracked platforms",
  "Humanoid balance and gait", "Rough terrain navigation",
  "Reinforcement learning for locomotion", "Reactive versus planned motion",
  "Energy efficiency in motion", "Fall detection and recovery",
  "Whole-body control", "Mobile manipulation combined",
  "Field robustness", "Benchmarks for locomotion"]),
 ("Simulation & Sim-to-Real", [
  "Physics simulation fidelity", "Domain randomisation",
  "System identification", "Photorealistic rendering for perception",
  "Parallel simulation at scale", "GPU-accelerated simulators",
  "Reality gap diagnosis", "Real-world fine-tuning",
  "Digital twins of workcells", "Scenario generation for testing",
  "Simulation validation", "When simulation misleads"]),
 ("Data Collection & Scaling", [
  "Teleoperated demonstration collection", "Scripted data generation",
  "Human video as a data source", "Play data and autonomous collection",
  "Data quality versus quantity", "Open robot datasets",
  "Data formats and standards", "Annotation for embodied data",
  "Cost of physical data collection", "Fleet learning across robots",
  "Privacy in collected environments", "Building a data engine"]),
 ("Safety & Assurance", [
  "Hazard analysis for robots", "Functional safety standards",
  "Safe reinforcement learning", "Runtime monitors and shields",
  "Collision avoidance guarantees", "Human-robot proximity safety",
  "Fail-safe and fail-operational design", "Verification of learned policies",
  "Testing coverage for physical systems", "Incident investigation",
  "Certification challenges for learned control", "Safety case construction"]),
 ("Humanoids & General-Purpose Robots", [
  "Why humanoid form factors", "Current humanoid platforms",
  "Economic case and unit costs", "Task generality claims examined",
  "Warehouse and logistics pilots", "Manufacturing deployments",
  "Service and hospitality trials", "Hardware reliability realities",
  "Battery and runtime constraints", "Teleoperation fallback models",
  "Public expectations versus reality", "Realistic adoption timelines"]),
 ("Deployment & Operations", [
  "Commissioning a robot system", "Fleet management software",
  "Over-the-air policy updates", "Monitoring robot behaviour",
  "Remote intervention workflows", "Maintenance and wear",
  "Workforce training and acceptance", "Measuring deployment value",
  "Edge compute on robots", "Connectivity requirements",
  "Incident response for robot fleets", "Scaling from pilot to production"]),
 ("Physical AI Career & Research", [
  "Roles in physical AI teams", "Skills spanning ML and robotics",
  "Research versus product paths", "Labs and companies to know",
  "Hardware access for learners", "Simulation-first learning path",
  "Open source projects to contribute to", "Conferences and publication venues",
  "Evaluating claims in the field", "Interview topics for these roles",
  "Long-term career outlook", "Building toward a physical AI career"]),
]))

for sec, num, title, subs in T:
    log.append("ADD TOPIC " + mk.add_topic(r, sec, num, title, subs))

mk.save(data)
print("\n".join(log))
print(f"\nStage 2b complete: {len(log)} topics added")
print("node counts by depth:", mk.counts(data))
