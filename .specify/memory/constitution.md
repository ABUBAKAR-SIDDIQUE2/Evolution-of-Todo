<!--
Sync Impact Report
- Version change: [CONSTITUTION_VERSION] -> 1.0.0
- Modified principles: Initial baseline for Evolution of Todo
- Added sections: Preamble, Supremacy, Structure, Phase Contract, Gemini CLI Authority, SDD Lifecycle, Phase Evolution, Safety Rules, Engineering Standards, Security, MCP/Agent Governance, Dapr/Kafka Governance, README/GEMINI requirements, Anti-Patterns, Validation Checklist.
- Templates requiring updates: 
  - .specify/templates/plan-template.md (✅ updated)
  - .specify/templates/spec-template.md (✅ updated)
  - .specify/templates/tasks-template.md (✅ updated)
- Follow-up TODOs: None
-->

# Evolution of Todo Constitution
📜 PROJECT CONSTITUTION
Evolution of Todo — Spec-Driven, Multi-Phase System

(SpecKit-Plus · Gemini CLI · Panaversity Standard)

I. PREAMBLE

This Constitution defines the binding rules, constraints, and operational laws governing the development of the project:

“Evolution of Todo”

This project is built using Spec-Driven Development with SpecKit-Plus, executed exclusively through Gemini CLI, and evolves through multiple phases from a simple console application to a distributed, cloud-native, AI-driven system.

This Constitution is authoritative and mandatory.
Any action, output, or implementation that violates this document is invalid.

II. SUPREMACY & AUTHORITY

This Constitution has highest authority over:
- Specs
- Tasks
- Generated code
- README files
- GEMINI.md instructions
- Agent behavior

In case of conflict:
Constitution > Specs > Tasks > Implementation

The agent must refuse to act if instructions violate this Constitution.

III. PROJECT STRUCTURE (MANDATORY)

Root Structure:
Evolution-of-Todo/
├── phase-I/
├── phase-II/
├── phase-III/
├── phase-IV/
├── phase-V/
└── CONSTITUTION.md (Symlinked or referenced from .specify/memory/constitution.md)

IV. PHASE DIRECTORY CONTRACT (STRICT)

Each phase directory MUST contain the following:
phase-X/
├── README.md
├── GEMINI.md
├── specs/
│   ├── overview.md
│   ├── features/
│   ├── api/
│   ├── database/
│   ├── agents/ (when applicable)
│   ├── mcp/ (when applicable)
│   └── ui/ (frontend phases)
├── frontend/ (only from Phase II onward)
├── backend/ (only from Phase II onward)
└── src/ (Phase I only)

Enforcement Rules:
- Every phase must have its own README.md
- Every phase must have its own GEMINI.md
- No phase may rely on another phase’s README or GEMINI instructions
- No cross-phase imports or shared runtime dependencies
- Phases are logically independent evolutions

V. GEMINI CLI — EXCLUSIVE IMPLEMENTATION AUTHORITY

Absolute Rule:
All code MUST be generated using Gemini CLI.

Explicit Prohibitions:
❌ Manual coding by a human
❌ Editing generated source files by hand
❌ Writing logic outside Gemini CLI
❌ Copy-pasting code from external sources
❌ “Fixing” code manually
❌ Writing partial implementations

Allowed Human Actions:
✅ Writing or refining: Constitution, Specs, Tasks, README.md, GEMINI.md
✅ Running Gemini CLI commands
✅ Reviewing generated output
✅ Iterating on specs until correct output is produced

VI. SPEC-DRIVEN DEVELOPMENT LIFECYCLE (MANDATORY)

All work MUST follow this lifecycle without skipping steps:
1. PHR (Problem / History Record): /sp.phr
2. SPECIFICATION PHASE: /sp.spec
3. TASK DECOMPOSITION: /sp.task
4. IMPLEMENTATION PHASE: /sp.impl
5. GIT COMMIT PHASE: /sp.git/commit_pr

VII. PHASE EVOLUTION RULES

Each phase builds on the previous conceptually but is implemented independently.
- Phase I — Console App: Python, In-memory, No persistence.
- Phase II — Full Stack Web: Frontend/Backend, Persistent DB (Neon), JWT auth.
- Phase III — AI Chatbot: MCP server, OpenAI Agents SDK, Tool-first.
- Phase IV — Kubernetes (Local): Docker, Helm, Minikube, AI-assisted DevOps.
- Phase V — Cloud Native: Managed K8s, Kafka/Redpanda, Dapr, Event-driven.

VIII. FILE & DIRECTORY SAFETY RULES

Forbidden Actions:
❌ Inventing files, Renaming folders without instruction, Deleting files, Moving code across phases, Cross-phase imports.

Required Behavior:
✅ Always verify file existence, Respect declared structure, Modify only files listed in tasks.

IX. ENGINEERING STANDARDS

- Deterministic behavior, Explicit error handling, Clear data models, Explicit typing.
- Secrets: NEVER hardcoded, use env vars, Dapr/K8s Secrets, or platform managers.

X. SECURITY & ACCESS CONTROL

- Protected APIs require auth, JWT validated server-side, User isolation at query level.
- Never trust frontend input, validate all payloads.

XI. MCP & AGENT GOVERNANCE (Phase III+)

- Business operations exposed as MCP tools (Stateless, Deterministic).
- Agent orchestrates tool usage, never modifies DB directly.

XII. DAPR & KAFKA GOVERNANCE (Phase IV–V)

- Infrastructure access via Dapr APIs.
- Event-driven only, consumer idempotency.

XIII. README & GEMINI.md REQUIREMENTS

- Phase README: Purpose, Arch, How to run, Env vars, Limitations.
- Phase GEMINI.md: Role of Gemini CLI, Spec usage, Implementation rules.

XIV. PROHIBITED ANTI-PATTERNS

- Hardcoded URLs/credentials, Manual coding, Skipping specs, Mixing phases.

XV. VALIDATION CHECKLIST (BEFORE ANY IMPLEMENTATION)

Agent MUST confirm:
- Phase identified, Specs exist, Tasks defined, GEMINI.md/README present, Files listed.

XVI. FINAL GOVERNING PRINCIPLE

Correctness, traceability, reproducibility, and spec-compliance override speed.

## Governance

### Amendment Procedure
Amendments to this Constitution require a formal proposal, justification of the impact on existing phases, and an increment in the version number. All dependent templates and existing specifications must be audited for compliance after an amendment.

### Versioning Policy
- MAJOR: Backward incompatible governance or phase redefinitions.
- MINOR: New phase added or significant technical standard expansion.
- PATCH: Clarifications, wording, non-semantic refinements.

### Compliance Review
All task executions and implementation plans must include a "Constitution Check" to verify adherence to these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30