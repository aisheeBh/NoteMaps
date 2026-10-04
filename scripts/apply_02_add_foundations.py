"""Stage 2a - additions to Pillars 1 and 2 (the foundation layers)."""
import sys
sys.path.insert(0, "scripts")
import _mapkit as mk

data = mk.load()
r = mk.root(data)
log = []

T = []  # (section_prefix, number, title, [(subtopic, [notes])])

# ------------------------------------------------------------------ 1.6.13
T.append(("1.6. ", "1.6.13", "AI Agents & Assistants for Everyone", [
 ("What an AI Agent Is", [
  "From chatbot to agent- what changes", "Agents, assistants and copilots compared",
  "How an agent decides what to do next", "Tools- how agents act on the world",
  "Memory- how agents remember across sessions", "Autonomy levels explained simply",
  "What agents are good at today", "What agents still do badly",
  "Agents vs traditional automation", "Common myths about AI agents",
  "A day in the life with an agent", "Deciding if you need an agent at all"]),
 ("Everyday Agent Use Cases", [
  "Inbox triage and email drafting", "Meeting scheduling and calendar management",
  "Research and summarising long documents", "Travel planning and booking",
  "Shopping, comparison and price tracking", "Personal finance and expense sorting",
  "Learning plans and study companions", "Home and personal admin tasks",
  "Content drafting and editing help", "Data gathering and simple reporting",
  "Routine job-search tasks", "Choosing the right task for an agent"]),
 ("Giving an Agent Good Instructions", [
  "Describing the outcome, not the steps", "Supplying the context an agent needs",
  "Setting constraints and boundaries", "Defining what done looks like",
  "Providing examples of good output", "Telling an agent what not to touch",
  "Breaking a big task into checkpoints", "Correcting an agent mid-task",
  "When to restart instead of repair", "Saving instructions you reuse",
  "Common instruction mistakes", "Building your own prompt library"]),
 ("Connecting Agents to Your Tools & Data", [
  "Why agents need access to be useful", "Connectors, plugins and integrations",
  "What the Model Context Protocol does", "Granting and revoking access safely",
  "Read-only vs read-write permissions", "Connecting email, calendar and files",
  "Connecting work systems responsibly", "Keeping personal and work data separate",
  "What an agent can see once connected", "Reviewing connected apps regularly",
  "Disconnecting and cleaning up access", "Checklist before you connect anything"]),
 ("Supervising & Reviewing Agent Work", [
  "Why review matters more as agents improve", "Spot-checking vs full review",
  "Reviewing reasoning, not just the answer", "Catching confident mistakes",
  "Checking sources and citations", "Approval gates for risky actions",
  "Keeping a human in the loop", "Knowing when to stop an agent",
  "Undo, rollback and damage limits", "Logging what an agent did",
  "Escalating when something goes wrong", "Building a personal review habit"]),
 ("Trust, Risk & Safety with Agents", [
  "What can go wrong with an autonomous tool", "Prompt injection in plain language",
  "Agents acting on untrusted content", "Oversharing and data leakage risks",
  "Financial and irreversible actions", "Impersonation and identity risks",
  "Agents that get stuck in loops", "Recognising manipulated or poisoned inputs",
  "Safe defaults for everyday users", "Red flags that an agent is misbehaving",
  "Reporting problems and incidents", "A personal agent safety checklist"]),
 ("Agents at Work", [
  "Workplace policies on agent use", "What you may and may not automate",
  "Agents and confidential information", "Agents in shared team workflows",
  "Disclosing agent involvement to colleagues", "Accountability for agent output",
  "Agents and customer-facing work", "Licensing and approved tools at work",
  "Introducing agents to a sceptical team", "Measuring whether an agent helped",
  "Avoiding shadow automation", "Talking to IT and security about agents"]),
 ("Multi-Agent and Chained Workflows", [
  "When one agent is not enough", "Agents that hand off to other agents",
  "Planner and worker patterns explained", "Chaining steps into a workflow",
  "Where chained workflows break", "Cost and time of long agent runs",
  "Keeping chained work understandable", "Debugging a workflow that went wrong",
  "Simple orchestration tools for non-engineers", "When to simplify back to one step",
  "Reliability expectations for chains", "Designing a workflow you can trust"]),
 ("Cost, Speed & Practical Limits", [
  "What makes an agent run expensive", "Tokens and context in everyday terms",
  "Why agents slow down on long tasks", "Setting budgets and usage limits",
  "Free, paid and enterprise tiers", "When a simple tool beats an agent",
  "Latency and waiting-time expectations", "Rate limits and quotas",
  "Measuring return on time invested", "Avoiding runaway usage",
  "Comparing agent pricing models", "Getting value without overspending"]),
 ("Choosing & Comparing Agent Tools", [
  "The current agent tool landscape", "General assistants vs specialised agents",
  "Desktop, browser and mobile agents", "Agents built into tools you already use",
  "Evaluating an agent before adopting", "Privacy terms worth reading",
  "Data retention and training opt-outs", "Portability and lock-in risks",
  "Trialling an agent safely", "Comparing output quality fairly",
  "Keeping up as tools change", "Deciding what to stop using"]),
 ("Ethics & Responsibility", [
  "Who is responsible for agent actions", "Honesty about agent-assisted work",
  "Agents and other people's data", "Consent when agents contact others",
  "Bias carried into agent decisions", "Environmental cost of heavy agent use",
  "Agents and employment effects", "Avoiding deceptive agent use",
  "Respecting platform terms and rules", "Agents in sensitive personal matters",
  "Teaching others to use agents well", "Setting your own ethical lines"]),
 ("Building Your Agent Practice", [
  "Starting with one low-risk task", "Keeping a log of what works",
  "Growing autonomy gradually", "Knowing which tasks to keep human",
  "Protecting the skills you want to retain", "Reviewing your setup periodically",
  "Sharing good patterns with others", "Staying current without chasing hype",
  "Preparing for more capable agents", "Building judgement, not dependence",
  "A personal agent operating model", "Your next three experiments"]),
]))

# ------------------------------------------------------------------- 1.4.9
T.append(("1.4. ", "1.4.9", "AI-Ready Data & Synthetic Data", [
 ("What Makes Data AI-Ready", [
  "Why AI raises the bar on data quality", "Completeness and coverage",
  "Consistency and standard formats", "Labelling and annotation basics",
  "Freshness and update cadence", "Structure, semi-structure and unstructured data",
  "Metadata and why it matters", "Documentation and data dictionaries",
  "Representativeness of the real world", "Known gaps and blind spots",
  "Signs your data is not AI-ready", "An AI-readiness checklist"]),
 ("Data Quality for AI", [
  "Accuracy and correctness", "Duplicates and near-duplicates",
  "Missing values and how to handle them", "Outliers and anomalies",
  "Inconsistent categories and naming", "Measurement and collection errors",
  "Quality at scale vs quality by sampling", "Automated quality checks",
  "Quality scorecards and thresholds", "Fixing versus excluding bad data",
  "Quality debt and how it accumulates", "Who owns data quality"]),
 ("Data Provenance & Lineage", [
  "Where did this data come from", "Tracking transformations end to end",
  "Why lineage matters for AI trust", "Source reliability assessment",
  "Chain of custody for sensitive data", "Versioning datasets over time",
  "Reproducing a past result", "Lineage and regulatory evidence",
  "Documenting collection methods", "Third-party and purchased data",
  "Scraped and public web data", "Provenance red flags"]),
 ("Rights, Consent & Licensing", [
  "Do you have the right to use this data", "Consent for AI-specific use",
  "Licence terms and permitted purposes", "Personal data in training sets",
  "Copyright and content ownership", "Attribution requirements",
  "Data from customers and employees", "Cross-border transfer basics",
  "Opt-out and deletion requests", "Contractual restrictions to check",
  "Public does not mean free to use", "When to seek legal advice"]),
 ("Bias and Representativeness", [
  "How sampling creates bias", "Historical bias baked into records",
  "Under-represented groups in data", "Proxy variables and hidden signals",
  "Measuring representativeness", "Balancing a skewed dataset",
  "Documenting known limitations", "Bias that reweighting cannot fix",
  "Testing outputs across groups", "Involving affected communities",
  "Bias in labels, not just features", "Communicating bias honestly"]),
 ("Introduction to Synthetic Data", [
  "What synthetic data is", "Why organisations generate it",
  "Fully synthetic vs partially synthetic", "Simulation-based generation",
  "Model-generated synthetic records", "Augmentation versus generation",
  "Common use cases", "What synthetic data cannot fix",
  "Synthetic data and privacy claims", "Quality measures for synthetic data",
  "Costs and effort involved", "When synthetic data is the wrong answer"]),
 ("Using Synthetic Data Responsibly", [
  "Disclosing synthetic origin", "Avoiding false confidence in results",
  "Model collapse and recursive training", "Keeping a real-data benchmark",
  "Synthetic data in testing environments", "Privacy guarantees and their limits",
  "Re-identification risks", "Regulatory views on synthetic data",
  "Validating against ground truth", "Mixing real and synthetic safely",
  "Documenting synthetic components", "Governance for synthetic datasets"]),
 ("Preparing Data for AI Use", [
  "Collecting with a purpose in mind", "Cleaning and standardising",
  "Structuring for retrieval and search", "Chunking documents sensibly",
  "Tagging and enriching with metadata", "Removing sensitive fields",
  "Anonymisation and pseudonymisation", "Sampling for evaluation sets",
  "Holding data back for testing", "Refreshing and re-processing",
  "Storage and access considerations", "A practical preparation workflow"]),
 ("Data Contracts & Shared Expectations", [
  "What a data contract is", "Agreeing schema and meaning",
  "Service expectations for data", "Breaking-change notification",
  "Ownership and accountability", "Quality guarantees in writing",
  "Contracts between teams", "Contracts with external providers",
  "Monitoring contract compliance", "Handling violations",
  "Contracts and AI reliability", "Starting simple with contracts"]),
 ("Evaluating Data Before You Trust It", [
  "First questions to ask of any dataset", "Checking sample records by hand",
  "Comparing against a known reference", "Spotting too-good-to-be-true data",
  "Understanding collection incentives", "Looking for survivorship effects",
  "Checking time ranges and gaps", "Verifying units and definitions",
  "Asking who is missing from this data", "Documenting your assessment",
  "Deciding fit for purpose", "Saying no to unusable data"]),
 ("Data Readiness in Practice", [
  "Assessing what your team already has", "Prioritising what to fix first",
  "Quick wins in data readiness", "Building a small, excellent dataset",
  "Making readiness visible to leaders", "Budgeting for data work",
  "Common organisational blockers", "Working with data owners",
  "Readiness as ongoing work", "Measuring improvement over time",
  "Avoiding readiness theatre", "A ninety-day readiness plan"]),
]))

# ------------------------------------------------------------------ 2.8.13
T.append(("2.8. ", "2.8.13", "Open Table Formats (Iceberg, Delta Lake, Hudi)", [
 ("Why Open Table Formats Exist", [
  "Limits of files-on-object-storage", "The lakehouse idea",
  "Separating storage, table format and engine", "What a table format adds",
  "ACID on object storage", "Open formats vs proprietary warehouses",
  "Engine interoperability as the goal", "Vendor neutrality and portability",
  "How the formats converged", "Choosing a format in practice",
  "Migration considerations", "When you do not need one"]),
 ("Apache Iceberg Fundamentals", [
  "Iceberg table anatomy", "Metadata files and manifests",
  "Snapshots and table versions", "Hidden partitioning",
  "Schema evolution in Iceberg", "Partition evolution",
  "Row-level deletes and updates", "Iceberg specification versions",
  "Reading and writing with common engines", "Iceberg catalogs overview",
  "Operational gotchas", "When Iceberg is the right default"]),
 ("Delta Lake Fundamentals", [
  "Delta transaction log", "Parquet plus log design",
  "Time travel in Delta", "Schema enforcement and evolution",
  "MERGE and upserts", "Deletion vectors",
  "Z-ordering and data skipping", "Delta UniForm and interoperability",
  "Open-source vs managed Delta", "Common Delta operations",
  "Performance tuning basics", "When Delta fits best"]),
 ("Apache Hudi Fundamentals", [
  "Hudi design goals", "Copy-on-write tables",
  "Merge-on-read tables", "Record keys and indexing",
  "Incremental queries", "Hudi timeline",
  "Clustering and compaction in Hudi", "Streaming ingestion with Hudi",
  "Hudi and CDC workloads", "Operational characteristics",
  "Hudi compared with the alternatives", "When Hudi fits best"]),
 ("Catalogs & Metadata Management", [
  "What a catalog does", "Hive Metastore and its limits",
  "REST catalog specification", "Managed catalog services",
  "Catalog federation", "Namespace and table organisation",
  "Access control at the catalog layer", "Catalog as the interoperability point",
  "Migrating between catalogs", "Catalog high availability",
  "Multi-engine catalog access", "Choosing a catalog"]),
 ("Table Maintenance Operations", [
  "Why maintenance is mandatory", "Small-file problems",
  "Compaction strategies", "Snapshot expiry",
  "Orphan file cleanup", "Vacuum and retention windows",
  "Rewriting manifests", "Sorting and clustering data",
  "Scheduling maintenance jobs", "Cost of maintenance",
  "Monitoring table health", "Maintenance runbook"]),
 ("Schema & Partition Evolution", [
  "Adding and dropping columns safely", "Renaming without rewriting",
  "Type widening rules", "Nested field evolution",
  "Backward and forward compatibility", "Evolving partitions over time",
  "Avoiding partition explosion", "Choosing partition columns",
  "Partition pruning in practice", "Evolution and downstream consumers",
  "Testing an evolution change", "Evolution mistakes to avoid"]),
 ("Streaming & Real-Time Lakehouse", [
  "Batch and streaming on one table", "The topic becomes the table",
  "Exactly-once ingestion concerns", "Change data capture into tables",
  "Streaming upserts at scale", "Latency expectations and trade-offs",
  "Streaming SQL engines in front", "Late and out-of-order data",
  "Watermarks and completeness", "Combining streams and historical data",
  "Operational complexity of streaming", "When batch is still better"]),
 ("Query Engines & Interoperability", [
  "Spark on open table formats", "Trino and Presto access",
  "Flink for streaming workloads", "DuckDB and single-node analytics",
  "Warehouse engines reading open tables", "Cross-engine consistency concerns",
  "Feature parity gaps between engines", "Choosing an engine per workload",
  "Avoiding engine lock-in", "Benchmarking fairly",
  "Mixed-engine architectures", "Interoperability in practice"]),
 ("Governance, Security & Cost", [
  "Table-level and column-level access", "Row filtering and masking",
  "Auditing table access", "Encryption at rest and in transit",
  "Data retention and legal holds", "Storage cost drivers",
  "Compute cost drivers", "Cost attribution by table",
  "Lifecycle policies", "Governance across engines",
  "Compliance evidence from metadata", "Controlling lakehouse spend"]),
 ("Lakehouse Architecture in Practice", [
  "Bronze, silver and gold layers", "Designing the raw landing zone",
  "Modelling curated tables", "Serving layer choices",
  "Semantic layer on top", "Feeding AI and ML workloads",
  "Migrating from a warehouse", "Migrating from a raw data lake",
  "Team ownership boundaries", "Documentation and discoverability",
  "Common architecture mistakes", "A reference lakehouse blueprint"]),
]))

# ------------------------------------------------------------------ 2.9.13
T.append(("2.9. ", "2.9.13", "WebAssembly & Modern Web Runtimes", [
 ("WebAssembly Fundamentals", [
  "What WebAssembly is", "Why Wasm exists",
  "Wasm modules and instances", "Linear memory model",
  "The Wasm instruction set", "Text and binary formats",
  "Wasm vs JavaScript performance", "What Wasm is not good for",
  "Browser support and maturity", "The Wasm specification process",
  "Common misconceptions", "When to reach for Wasm"]),
 ("Compiling to WebAssembly", [
  "Rust to Wasm toolchain", "C and C++ with Emscripten",
  "Go and TinyGo targets", "AssemblyScript basics",
  "Toolchain output and artefacts", "Optimising build size",
  "Source maps and debug builds", "Build reproducibility",
  "Managing toolchain versions", "Cross-compilation pitfalls",
  "Build times and caching", "Choosing a source language"]),
 ("JavaScript Interoperability", [
  "Loading and instantiating a module", "Passing numbers across the boundary",
  "Passing strings and buffers", "Sharing memory with JavaScript",
  "wasm-bindgen and binding generators", "Callback patterns",
  "Boundary-crossing cost", "Avoiding chatty interfaces",
  "Error handling across the boundary", "Garbage collection interaction",
  "Typed arrays and views", "Interop design guidelines"]),
 ("Performance Engineering with Wasm", [
  "Where Wasm genuinely wins", "Measuring before porting",
  "SIMD in WebAssembly", "Threads and shared memory",
  "Memory growth and allocation", "Avoiding copies",
  "Startup and instantiation cost", "Streaming compilation",
  "Profiling Wasm in the browser", "Bundle size versus speed",
  "Benchmarking honestly", "Knowing when not to optimise"]),
 ("WASI & Wasm Outside the Browser", [
  "What WASI provides", "WASI preview versions",
  "Filesystem and clock access", "Sockets and networking",
  "Wasm on the server", "Wasm in edge runtimes",
  "Wasm as a plugin format", "Sandboxing guarantees",
  "Capability-based security model", "Host function design",
  "Portability across runtimes", "Server-side Wasm use cases"]),
 ("The Component Model", [
  "Why components were introduced", "Interface types explained",
  "WIT interface definitions", "Composing components",
  "Language-agnostic interfaces", "Component registries",
  "Versioning components", "Components vs modules",
  "Current tooling maturity", "Building a simple component",
  "Component model limitations", "Where components are heading"]),
 ("Wasm Runtimes", [
  "Browser engines as runtimes", "Wasmtime overview",
  "Wasmer overview", "WasmEdge and edge focus",
  "Embedding a runtime in an application", "Ahead-of-time compilation",
  "Just-in-time compilation trade-offs", "Resource limits and fuel",
  "Runtime security posture", "Benchmarking runtimes",
  "Choosing a runtime", "Operating Wasm in production"]),
 ("Security & Sandboxing", [
  "The Wasm sandbox boundary", "What the sandbox does not protect",
  "Capability grants and least privilege", "Untrusted code execution patterns",
  "Side-channel considerations", "Supply chain risk in Wasm modules",
  "Verifying module provenance", "Resource exhaustion defence",
  "Host function attack surface", "Auditing a Wasm dependency",
  "Sandbox escape history", "A Wasm security checklist"]),
 ("Modern Web Runtime Landscape", [
  "Browser JavaScript engines today", "Service workers as a runtime",
  "Edge runtime constraints", "Node, Deno and Bun compared",
  "Standard web APIs on the server", "Runtime-agnostic code",
  "Cold start characteristics", "Runtime API compatibility",
  "Polyfills and shims", "Choosing a runtime for a workload",
  "Portability strategies", "Where runtimes are converging"]),
 ("Practical Wasm Use Cases", [
  "Image and video processing in-browser", "Cryptography and hashing",
  "Games and simulation", "CAD and 3D in the browser",
  "Data science and notebooks on the web", "Running databases in the browser",
  "Language runtimes compiled to Wasm", "Legacy code brought to the web",
  "Plugin systems for applications", "Serverless function isolation",
  "Machine learning inference in Wasm", "Evaluating a candidate use case"]),
 ("Adopting Wasm in a Real Project", [
  "Making the case for Wasm", "Prototyping before committing",
  "Incremental adoption strategy", "Team skills required",
  "Debugging workflow in practice", "Testing Wasm modules",
  "CI and build pipeline setup", "Shipping and caching modules",
  "Monitoring Wasm in production", "Maintenance burden",
  "Knowing when to roll back", "Lessons from real adoptions"]),
]))

# ----------------------------------------------------------------- 2.12.13
T.append(("2.12. ", "2.12.13", "AI Coding Assistants & Agentic Development", [
 ("The AI-Assisted Development Landscape", [
  "Completion, chat and agent modes", "How coding assistants work",
  "In-editor versus terminal agents", "Assistants built into platforms",
  "What changed with agentic coding", "Capability and its limits today",
  "Effect on team workflows", "Effect on the junior-to-senior path",
  "Measuring whether it helps", "Avoiding productivity theatre",
  "Choosing tools for a team", "Where the field is heading"]),
 ("Prompting for Code", [
  "Describing intent precisely", "Supplying the right context files",
  "Specifying constraints and style", "Asking for tests alongside code",
  "Requesting explanations of output", "Iterating instead of restarting",
  "Narrowing scope to improve accuracy", "Giving examples of desired shape",
  "Prompting for refactors", "Prompting for debugging help",
  "Reusable prompt patterns", "Prompting anti-patterns"]),
 ("Context Management in Coding Tools", [
  "Why context determines quality", "Selecting files that matter",
  "Repository-wide context and its cost", "Indexing and semantic search",
  "Context windows in practice", "Keeping context current",
  "Project instruction files", "Conventions the assistant should follow",
  "Excluding files from context", "Context and monorepos",
  "Managing long sessions", "Context hygiene habits"]),
 ("Agentic Coding Workflows", [
  "Letting an agent run multi-step tasks", "Planning before editing",
  "Agents that run tests and iterate", "Approval gates for file changes",
  "Working on a branch or worktree", "Scoping a task for an agent",
  "Tasks agents handle well", "Tasks to keep manual",
  "Recovering from a bad agent run", "Parallel agent tasks",
  "Reviewing an agent's whole diff", "Designing a safe agent loop"]),
 ("Reviewing AI-Generated Code", [
  "Why review matters more now", "Reading for intent, not just syntax",
  "Spotting plausible but wrong logic", "Checking edge cases and errors",
  "Verifying against requirements", "Hidden performance problems",
  "Security review of generated code", "Dependency additions to scrutinise",
  "Licence risk in generated code", "Avoiding rubber-stamp approval",
  "Review checklists for AI output", "Teaching juniors to review"]),
 ("Testing & Verification", [
  "Tests as the safety net for AI code", "Generating tests responsibly",
  "Avoiding tests that assert the bug", "Property-based testing fits",
  "Coverage as a weak signal", "Running tests in the agent loop",
  "Integration and end-to-end checks", "Manual verification that still matters",
  "Regression risk from large diffs", "Verifying refactors preserved behaviour",
  "Test review discipline", "Building trust through verification"]),
 ("Security & Supply Chain Risks", [
  "Secrets leaking into prompts", "Code exfiltration concerns",
  "Insecure patterns in generated code", "Hallucinated package names",
  "Slopsquatting and dependency attacks", "Prompt injection via repository content",
  "Agents with shell and network access", "Sandboxing agent execution",
  "Reviewing agent tool permissions", "Audit logging of agent actions",
  "Enterprise policy and controls", "A security checklist for AI coding"]),
 ("Code Quality & Maintainability", [
  "Consistency with existing codebase", "Avoiding duplicated abstractions",
  "Generated code and readability", "Comment density and noise",
  "Over-engineering from assistants", "Architectural drift over time",
  "Keeping diffs reviewable in size", "Refactoring generated code",
  "Technical debt from fast generation", "Style and lint enforcement",
  "Documentation expectations", "Quality gates in CI"]),
 ("Team Practices & Governance", [
  "Agreeing team norms for AI use", "Disclosure in pull requests",
  "Approved tools and licensing", "Data handling and compliance",
  "Onboarding juniors in an AI workflow", "Pairing humans with agents",
  "Attribution and accountability", "Measuring team-level impact",
  "Avoiding skill atrophy", "Handling disagreement about AI use",
  "Policy for customer code", "Writing a team AI coding policy"]),
 ("Building Your Own Tooling", [
  "Custom instructions and rules files", "Project-level agent configuration",
  "Exposing internal tools to agents", "Model Context Protocol servers",
  "Automating repetitive agent tasks", "Hooks and lifecycle automation",
  "Internal prompt and skill libraries", "Sharing configuration across a team",
  "Testing your own tooling", "Versioning agent configuration",
  "Maintaining custom tooling", "When custom tooling pays off"]),
 ("Skills That Still Matter", [
  "Architecture and system design", "Debugging from first principles",
  "Reading unfamiliar code fast", "Performance analysis",
  "Security thinking", "Knowing the domain deeply",
  "Judging trade-offs", "Writing clear specifications",
  "Communicating technical decisions", "Mentoring in an AI era",
  "Deliberate practice without assistance", "Staying employable as tools improve"]),
]))

# ----------------------------------------------------------------- 2.13.13
T.append(("2.13. ", "2.13.13", "eBPF & Kernel Programmability", [
 ("eBPF Fundamentals", [
  "What eBPF is", "Why in-kernel programmability matters",
  "eBPF versus kernel modules", "The eBPF virtual machine",
  "Program types overview", "Maps as shared state",
  "The verifier and its guarantees", "JIT compilation",
  "Helper functions", "Kernel version dependencies",
  "What eBPF cannot do", "Where eBPF is used today"]),
 ("Writing eBPF Programs", [
  "C with libbpf", "CO-RE and portability",
  "BTF type information", "Compiling and loading programs",
  "Attaching to hooks", "Reading and writing maps",
  "Ring buffers for events", "Rust and Go toolchains",
  "bpftrace for quick scripts", "Debugging a rejected program",
  "Testing eBPF code", "Project layout conventions"]),
 ("Tracing & Observability", [
  "kprobes and kretprobes", "Tracepoints and raw tracepoints",
  "uprobes for user space", "USDT probes",
  "perf events integration", "Low-overhead sampling",
  "Building a latency histogram", "Tracing syscalls safely",
  "Continuous profiling with eBPF", "Flame graphs from eBPF data",
  "Overhead measurement", "Production tracing discipline"]),
 ("Networking with eBPF", [
  "XDP for early packet processing", "TC ingress and egress hooks",
  "Socket filters and redirects", "Load balancing in the kernel",
  "Packet parsing patterns", "NAT and tunnelling",
  "Bandwidth and rate limiting", "Connection tracking",
  "Bypassing the network stack", "Performance characteristics",
  "Debugging packet paths", "Networking use cases"]),
 ("Security & Enforcement", [
  "LSM hooks and eBPF", "Syscall monitoring and blocking",
  "Runtime security detection", "Container escape detection",
  "File and process event capture", "Signature versus behaviour detection",
  "Avoiding time-of-check issues", "Tamper resistance",
  "Audit trail generation", "Privilege requirements",
  "Security of eBPF itself", "Enforcement versus observation"]),
 ("eBPF in Kubernetes", [
  "Cilium and CNI networking", "Replacing kube-proxy",
  "Network policy enforcement", "Service mesh without sidecars",
  "Pod-level observability", "Identity-based networking",
  "Multi-cluster connectivity", "Hubble and flow visibility",
  "Performance versus iptables", "Operational considerations",
  "Troubleshooting Cilium", "Adoption path in a cluster"]),
 ("Performance & Overhead", [
  "Measuring eBPF program cost", "Per-event overhead sources",
  "Map lookup performance", "Reducing data copied to user space",
  "Aggregating in kernel", "Sampling strategies",
  "Verifier complexity limits", "Instruction count budgets",
  "Tail calls and program chaining", "Memory footprint of maps",
  "Benchmarking methodology", "Avoiding observability overhead"]),
 ("Tooling Ecosystem", [
  "bcc toolkit", "bpftrace one-liners",
  "libbpf and libbpf-rs", "Aya for Rust",
  "cilium ebpf for Go", "bpftool for inspection",
  "Pixie and auto-instrumentation", "Parca and continuous profiling",
  "Falco for runtime security", "Choosing a tool for the job",
  "Packaging eBPF with applications", "Keeping tools current"]),
 ("Operating eBPF in Production", [
  "Deployment and lifecycle", "Kernel compatibility testing",
  "Graceful degradation", "Program lifetime and pinning",
  "Resource limits and quotas", "Monitoring your eBPF programs",
  "Rolling out changes safely", "Rollback procedures",
  "Incident response with eBPF", "Permissions and capabilities",
  "Multi-tenant concerns", "Production readiness checklist"]),
 ("Limits, Risks & Alternatives", [
  "Verifier rejection frustrations", "Kernel version fragmentation",
  "Debuggability challenges", "Skill scarcity on teams",
  "When a userspace agent is enough", "When a kernel module is warranted",
  "Vendor lock-in in eBPF platforms", "Stability of unstable interfaces",
  "Performance regressions from eBPF", "Security risk of broad eBPF access",
  "Maintenance cost over time", "Deciding whether eBPF fits"]),
]))

for sec, num, title, subs in T:
    log.append("ADD TOPIC " + mk.add_topic(r, sec, num, title, subs))

mk.save(data)
print("\n".join(log))
print(f"\nStage 2a complete: {len(log)} topics added")
print("node counts by depth:", mk.counts(data))
