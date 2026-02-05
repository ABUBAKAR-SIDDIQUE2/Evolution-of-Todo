<!--
SYNC IMPACT REPORT
Version: 0.0.0 -> 1.0.0
- Added Principle 1: Spec-Driven Development (SDD)
- Added Principle 2: Tooling & Workflow Enforcement
- Added Principle 3: Architecture & Structure
- Added Principle 4: Quality Assurance & Testing
- Added Principle 5: Version Control & Branching
- Added Principle 6: Artifact Traceability
- Added Principle 7: Security & Governance
- Added Principle 8: Phased Delivery & Deliverables
- Validated Templates: plan-template.md, spec-template.md, tasks-template.md (Compatible)
-->
# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (SDD)
Every feature begins with a detailed Markdown specification, not code. The spec is the single source of truth; code is derived from it using GEMINI CLI. Manual coding is prohibited unless correcting minor generative errors; all major logic must flow from `spec -> plan -> tasks -> implementation`. "Spec-driven development means writing a ‘spec’ before writing code with AI... The spec becomes the source of truth."

### II. Tooling & Workflow Enforcement
All work must utilize Spec-Kit Plus (`/sp.*`) and GEMINI CLI. The workflow is strictly iterative:
1. `/sp.constitution`: Initialize/Update principles.
2. `/sp.specify`: Define requirements.
3. `/sp.plan`: Architect the solution.
4. `/sp.tasks`: Break down implementation.
5. `/sp.implement`: Generate code via AI.
Directly jumping to code without these steps is a violation of the constitution.

### III. Architecture & Structure
The project operates as a **Monorepo** to facilitate cross-cutting changes.
- **Root**: `constitution.md`, `GEMINI.md`, `/specs/`, `README.md`.
- **Phase I**: `/src/` (Python CLI).
- **Phase II+**: `/frontend/` (Next.js), `/backend/` (FastAPI), `/charts/` (Kubernetes).
Layered `GEMINI.md` files (root and sub-service) dictate context-specific rules.

### IV. Quality Assurance & Testing
**Test-First Mindset**: Tests must be specified in the plan and written before implementation where feasible.
- **Unit Tests**: Required for all core logic.
- **Integration Tests**: Required for all API endpoints and service interactions.
- **CI/CD**: Linting, formatting, and tests must pass on every commit. Merges are blocked on failure.
"If tests are requested, test tasks are included and ordered to be written before implementation."

### V. Version Control & Branching
**Feature Branch Workflow**:
- Each feature/spec gets a dedicated branch (`feature/name`).
- Commit messages must be descriptive and link to specs/tasks.
- Main branch is protected; merge only via PR/MR after verification.
- Release tags (e.g., `v1.0-phase1`) mark milestones.

### VI. Artifact Traceability
Every code artifact must be traceable back to a specific version of a specification.
- Specs are versioned in Git.
- Documentation (README, Deployment docs, Architecture diagrams) must be updated per phase.
- A `CHANGELOG.md` or annotated tags must track evolution.

### VII. Security & Governance
**Non-Negotiable Security Rules**:
- No hard-coded secrets (use `.env` / Kubernetes Secrets).
- Authentication required for APIs (e.g., JWT).
- Input validation on all public interfaces.
- Deployment artifacts (containers, charts) must be scanned/verified.

### VIII. Phased Delivery & Deliverables
The project evolves through five distinct phases, each with strict deliverables:
1. **Phase I**: In-Memory Python CLI (Spec-driven).
2. **Phase II**: Full-Stack (Next.js + FastAPI + Postgres).
3. **Phase III**: AI Chatbot (OpenAI Agents + MCP).
4. **Phase IV**: Local Kubernetes (Minikube + Helm).
5. **Phase V**: Cloud Native (DOKS + Kafka + Dapr).

## Governance

This constitution supersedes all other documentation. Amendments require a version bump and a corresponding update to the `SYNC IMPACT REPORT`. Any change to architecture or standards must begin by updating this constitution so that subsequent code generation remains aligned.

**Version**: 1.0.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05