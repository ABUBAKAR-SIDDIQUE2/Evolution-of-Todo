---
id: 0001
title: Update Project Constitution Principles
stage: constitution
date: 2026-02-05
surface: agent
model: gemini-2.0-flash
feature: none
branch: master
user: abubakar
command: /sp.constitution
labels: ["governance", "setup", "principles"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  []
---

## Prompt

/sp.constitution Project Constitution: The Evolution of Todo – Mastering Spec-Driven Development & Cloud Native AI
Purpose and Scope

This project constitution governs the five-phase “Evolution of Todo” hackathon, from a simple in-memory CLI to a distributed cloud-native AI system. Its purpose is to define the technical and process standards that the solo developer will follow throughout all phases. The scope covers all five phases: Phase I (Python CLI), Phase II (Next.js/React + FastAPI web app), Phase III (AI chatbot with OpenAI Agents and MCP tools), Phase IV (local Kubernetes deployment with Minikube/Helm), and Phase V (cloud deployment on Kubernetes with Kafka and Dapr). Each phase builds on the previous, so this constitution ensures consistency from prototype to production-grade deployment. The overarching goal is to “build progressively complex software without writing boilerplate code”, using Spec-Driven Development with GEMINI CLI and Spec-Kit Plus as required by the hackathon rules.
Governance Principles (Constitution)

The constitution is a living document of project-wide rules and standards. It sets non-negotiable guardrails for development (e.g. coding style, architecture, security, testing, and Git policy). At initialization, the Spec-Kit Plus command /sp.constitution is used to create or update these principles. For example, a constitution entry might state: “Focus on code quality, testing standards, user experience consistency, and performance requirements”

. Key sections of the constitution should include:

    Build & Deployment – commands and scripts to run the code (e.g. how to launch the CLI, the web app, containers, Helm charts).

    Code Style & Guidelines – formatting (PEP 8, lint rules), naming conventions, and language versions.

    Testing Policy – requirement that each feature has accompanying tests (unit/integration) and defines acceptance criteria. 

    Architecture & Design – fixed tech choices (Next.js, FastAPI, Postgres, etc.), layer boundaries, and expected data flow.

    Security Rules – e.g. JWT auth for APIs, no hard-coded secrets, CORS settings.

    Version Control Workflow – branch naming conventions, merge policy, and release tagging (see below).

By committing this constitution in constitution.md at the repo root, both human and AI coding assistants will reference it as the authoritative rulebook for the project

. Any change to architecture or standards must begin by updating the constitution so that subsequent code generation remains aligned.
Spec-Driven Development Mandate

This project follows Spec-Driven Development (SDD): every feature begins with a detailed spec document, not code. As Birgitta Böckeler (ThoughtWorks) defines, “Spec-driven development means writing a ‘spec’ before writing code with AI (‘documentation first’). The spec becomes the source of truth for the human and the AI”. In practice, the developer writes a clear Markdown spec describing the functional requirements, behavior, constraints, and acceptance criteria for each feature. GEMINI CLI (with Spec-Kit Plus) then uses this spec to generate implementation code. The spec remains the authoritative artifact: code is validated against it, and future changes are driven by updating the spec first. This ensures that all work (code, tests, docs) traces back to the original requirements. In concrete terms, no manual coding is allowed: the hackathon rules explicitly state that you “must write a Markdown Constitution and Spec for every feature… and use GEMINI CLI to generate the implementation. Constraint: You cannot write the code manually”. The workflow is iterative: use /sp.specify to articulate what to build, /sp.plan to outline the architecture, /sp.tasks to break it into implementable steps, and /sp.implement to run the code generation. If the output is incorrect, refine the spec until GEMINI CLI produces the expected result. In summary, specs are the single source of truth, code is derived and tested against them

.
Tooling and Workflow Enforcement

All work uses Spec-Kit Plus and GEMINI CLI as first-class tools. Spec-Kit Plus (the specifyplus or sp CLI) provides structured slash-commands to guide development

. In particular:

    /sp.constitution – Initialize or update project-wide principles (code quality, testing standards, UX consistency, etc.)

    .

    /sp.specify – Write the feature specification (requirements/user stories) as Markdown.

    /sp.plan – Define the technical plan (stack, components, data models) for that spec.

    /sp.tasks – Generate an actionable list of tasks (step-by-step work items) from the spec and plan.

    /sp.implement – Execute all tasks to build the feature (via GEMINI CLI invoking the chosen AI model).

Using these commands enforces the SDD workflow: for example, Spec-Kit Plus will even produce “unit tests for English” (via /sp.checklist) and include test-writing tasks before implementation

. GEMINI CLI is configured by project-specific files (GEMINI.md at the repo root and in subfolders) that teach the agent how to apply the specs. As the summary states: “Spec-Kit Plus provides organized, structured specs that GEMINI CLI can reference. The GEMINI.md files tell GEMINI CLI how to use those specs and project-specific conventions”. Thus the constitution is enforced by these tools at every step, preventing ad hoc coding or deviation from standards.
Version Control and Branching

All artifacts (specs, code, tests, configurations) are tracked in Git to maintain full history and auditability. We use a feature-branch workflow: each new feature or user story is developed on its own branch, which contains the spec, plan, tasks, and code changes. For example, Spec-Kit Plus itself creates one Git branch per spec/feature. When a feature is complete, the branch is reviewed (manually or by AI checks), then merged into main. This ensures isolation of work and a clean main branch. A clear branching strategy streamlines collaboration and stability (“A branching strategy defines how developers organize, write, and merge code… to streamline collaboration and maintain stability”

). In practice: use descriptive branch names (e.g. feature/add-task-cli), commit all related artifacts together (spec file, code, tests), and write detailed commit messages linking back to spec IDs or tickets.

We will maintain a monorepo for this hackathon. As the project guide recommends, a single repository (instead of separate frontend/backend repos) makes it easier for GEMINI CLI to apply cross-cutting changes. The monorepo has a layered GEMINI.md setup: a root file for overall context, and sub-folder GEMINI.md for technology-specific patterns. Releases or phase milestones can be tagged (e.g. v1.0-phase1) to snapshot progress.
Project Structure

The repository follows an organized, consistent layout so that specs, code, and docs are easy to find. For all phases, the root of the repo should contain:

    constitution.md – This project constitution (this document).

    GEMINI.md – Global GEMINI CLI instructions and conventions.

    /specs/ – Folder of specification files, organized by feature or phase. For example, /specs/add_task.md, /specs/update_task.md, etc. Subfolders can group related specs. (The specs folder is the source of truth: “What to build”.)

    README.md – High-level overview of the project, prerequisites, and build steps for each phase.

    (Later) /charts/ or /helm/ – Helm charts and Kubernetes manifests for deployment (Phase IV/V).

Within /specs/, each feature’s Markdown spec documents must reside. The Spec-Kit Plus workflow will generate intermediate files (plan.md, tasks.md, etc.) either in specs or alongside code.

Beyond the root, code is organized by phase/layer:

    Phase I: Place the Python console app under /src/ (e.g. src/app.py). Any simple tests or scripts can go under /tests/.

    Phase II: Create /frontend/ and /backend/ directories. In /frontend/, initialize a Next.js app. In /backend/, initialize a FastAPI project with SQLModel. Each of these folders should contain its own GEMINI.md for service-specific patterns. Common specs remain in /specs/.

    Phase III: Add directories as needed for AI components, e.g. /chatbot/ or /agents/ for the OpenAI Agents code and MCP server. The FastAPI backend will have endpoints for chat (e.g. /api/chat).

    Phase IV/V: Add a charts/ (or helm/) directory for Kubernetes deployment configurations and any Dockerfiles at project root or in each service folder. Dapr component YAMLs, Kafka topic definitions, and other cloud configs should be placed in charts/ or k8s/.

This structured layout (monorepo with layered GEMINI.md files and a specs folder) follows the hackathon guidance and ensures clarity: the summary states that a monorepo “provides single context” so GEMINI CLI can make cross-cutting changes, and that a specs folder lets you reference specs directly.
Quality Assurance and Testing

Code quality is enforced at every step. We adopt a test-driven mindset: specifications should include clear acceptance criteria, and we should generate or write tests accordingly. Spec-Kit Plus itself encourages this: it uses a “test-driven development structure – if tests are requested, test tasks are included and ordered to be written before implementation”

. In practice, for each feature:

    Write unit tests covering the behavior described in the spec (e.g. verify that adding a task produces the correct list entry).

    Add integration tests for service interactions (e.g. test a REST API endpoint end-to-end).

    For critical features like user auth or data storage, include security and edge-case tests.

Continuous Integration (CI) should run on every commit/merge (e.g. via GitHub Actions). CI steps include linting (flake8, ESLint, etc.), running unit tests, and reporting coverage. Any failures (failing tests or lint errors) must block merges. This automated QA loop, driven by the specifications, yields “complete traceability” from requirements to code and tests. Indeed, one source notes: “Complete Traceability: From a business requirement to a line of code, every connection is maintained and visible… Quality Assurance: Generated code includes comprehensive tests based on the use case specifications.”

. We will aim to match that standard. Regular manual reviews (at least self-review with AI assistance) of both specs and code help catch issues that automated checks might miss.
Artifact Traceability & Documentation

Every artifact is versioned and linked. The repo’s history should allow tracing a feature from its specification through the generated code and tests

. We will use consistent identifiers or file naming (e.g. feature codes or spec filenames) so it’s clear which spec produced which code. For documentation: each phase must include an updated README.md or doc pages explaining setup, architecture, and deployment steps. In particular:

    Deployment docs: For Phases IV/V, document how to deploy to Minikube and to the cloud (DigitalOcean Kubernetes). Include example commands (kubectl, Helm install, Dapr run commands), environment variable descriptions, and rollback procedures.

    Architecture diagrams: Provide diagrams (in markdown or a docs folder) showing component interactions for the AI chatbot and Kubernetes services.

    Changelogs: Although formal release notes may not be required for a hackathon, we should maintain a CHANGELOG.md or use Git tags with notes to record major changes (especially as specs evolve).

By keeping all specs, plans, code, and docs in Git, we ensure a clear audit trail: one can always check what the system was supposed to do (the spec) and what it actually does (the code), as one source emphasizes that SDD output is “captured in easily shareable and customizable markdown files, providing a clear, auditable path from high-level user need to compliant implementation.”

.
Phase Overview & Deliverables

The constitution enforces that each phase meets its deliverables with spec-driven output. In summary:

    Phase I – In-Memory Python CLI App: Implement all five core todo features (add, delete, update, view list, complete) in a console app. Deliverables: a functioning src/ program; a constitution.md; all spec files in /specs/; a README.md with setup; and a GEMINI.md for CLI patterns. The code must be generated via GEMINI CLI from the specs.

    Phase II – Full-Stack Web Application: Transform the CLI into a web app. Frontend: Next.js (App Router) in /frontend/; Backend: FastAPI in /backend/; data storage: Neon PostgreSQL. Implement user signup/signin (Better Auth) and the same basic todo endpoints (REST API). Deliverables: expanded monorepo with /frontend/ and /backend/ folders (each with GEMINI.md for service-specific guidance), updated specs for each API endpoint, and deployment instructions. All features continue to use GEMINI CLI generation.

    Phase III – AI Chatbot: Add a conversational interface using OpenAI ChatKit on the frontend and OpenAI Agents on the backend. Build an MCP (Model Context Protocol) server with the Official MCP SDK in the FastAPI backend to expose task tools (e.g. add_task, list_tasks). The chatbot must handle natural-language requests for todo operations. Deliverables: chatbot code and updated specs documenting chatbot scenarios, plus any new environment or configuration files needed for the MCP server.

    Phase IV – Local Kubernetes Deployment: Containerize all services (frontend, backend, chatbot) with Docker. Deploy the system on Minikube using Helm charts. Include a Helm chart in /charts/ (or /helm/) that installs the app and sets up required services/ingresses. Leverage tools like kubectl-ai and kagent for Kubernetes AI operations. Deliverables: working local Kubernetes deployment (demonstrated on Minikube) and documentation of the deployment process.

    Phase V – Cloud Deployment (Kafka & Dapr): Push the system to a cloud Kubernetes cluster (e.g. DigitalOcean DOKS). Integrate Apache Kafka and Dapr: use Kafka for event-driven communication (e.g. new-task events), and Dapr for service invocation/pub-sub between microservices. Update Helm charts and add Dapr component YAMLs under /charts/. Provide clear instructions for provisioning cloud resources and deploying via Helm/Dapr. Deliverables: cloud-deployed, event-driven version of the app; Kafka topics configured; Dapr components defined; and comprehensive deployment docs.

Each phase’s deliverables must be traceable to its specs (see above), and each phase’s completion will be confirmed by running the spec-driven GEMINI workflows and verifying the output. Following these guidelines ensures that by the end of Phase V, the project is a fully spec-driven, AI-assisted, cloud-native application consistent with the industry best practices and hackathon requirements.

## Response snapshot

Updated project constitution to v1.0.0 with 8 core principles covering SDD, Tooling, Architecture, QA, Git, Traceability, Security, and Phased Delivery.

## Outcome

- ✅ Impact: Constitution defined v1.0.0
- 🧪 Tests: N/A
- 📁 Files: constitution.md updated
- 🔁 Next prompts: /sp.specify
- 🧠 Reflection: Constitution established.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A