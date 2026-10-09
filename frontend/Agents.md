# DevRadar AI Coding Rules

## Purpose

DevRadar is being built incrementally.

AI coding agents are implementation assistants.

They do not own the architecture or product decisions.

The developer owns:

- Product scope
- Architecture
- Interfaces
- Data models
- Dependencies
- Tradeoffs
- Final code quality

---

# 1. General Rules

Do not implement features that have not been explicitly requested.

Do not redesign the architecture unless explicitly asked.

Do not add speculative abstractions, dependencies, services, or database tables.

Prefer the smallest implementation that satisfies the acceptance criteria.

Do not optimize for hypothetical future requirements.

---

# 2. Before Coding

For every task:

1. Inspect the relevant existing files.
2. Identify the files that need to change.
3. Explain the implementation approach briefly.
4. Check whether the requested change conflicts with PRODUCT.md or ARCHITECTURE.md.
5. Do not modify unrelated files.

If the architecture conflicts with the task, stop and explain the conflict before making changes.

---

# 3. During Coding

- Keep changes focused.
- Do not refactor unrelated code.
- Do not introduce new dependencies without justification.
- Reuse existing code where appropriate.
- Prefer simple functions over unnecessary abstractions.
- Keep external API-specific logic isolated.
- Do not duplicate business logic.
- Do not generate placeholder systems for future features.
- Do not create files unless they are needed.
- Do not add comments that merely restate obvious code.

---

# 4. Dependencies

Before adding a dependency, explain:

1. What problem it solves.
2. Why the standard library or existing dependencies are insufficient.
3. Whether the dependency is required for the MVP.

Do not add dependencies for convenience alone.

---

# 5. Frontend Rules

Frontend:

- React
- JavaScript
- Vite
- TailwindCSS

Do not introduce:

- Next.js
- TypeScript
- Redux
- Zustand
- React Query
- UI frameworks

unless explicitly approved.

For simple API state, use React's existing mechanisms until they become insufficient.

---

# 6. Backend Rules

Backend:

- Python
- FastAPI
- SQLite

Keep the backend simple.

Do not introduce:

- Celery
- Redis
- PostgreSQL
- Docker orchestration
- Microservices

unless explicitly required.

---

# 7. API Rules

API contracts must be explicit.

For every endpoint, define:

- HTTP method
- URL
- Input
- Output
- Error behavior

Do not silently change an existing API contract.

---

# 8. External API Rules

External API integrations must be isolated in connector modules.

Do not spread SerpApi-specific response handling throughout the application.

Convert external responses into DevRadar's own structures.

Do not create a generic provider abstraction until a second real provider exists.

---

# 9. AI Rules

Claude is a reasoning component, not the application architecture.

Do not ask Claude to perform work that deterministic code can perform reliably.

Prefer:

```text
External API
    ↓
Normalize
    ↓
Filter
    ↓
Structure
    ↓
Claude
    ↓
Structured result

over:

External API
    ↓
Huge raw response
    ↓
Claude does everything

AI-generated conclusions must remain distinguishable from source evidence.

10. Testing

Every meaningful backend feature should have tests.

At minimum test:

expected behavior
invalid input
important edge cases

Do not write tests that merely reproduce the implementation.

11. Git

Keep commits small and meaningful.

Prefer:

Add FastAPI health endpoint
Add SerpApi Google connector
Normalize Google results
Add opportunity model

Avoid:

Build entire application

Do not mix unrelated changes into one commit.

12. Reprompting

If the first implementation is wrong:

Do not immediately ask the AI to rewrite everything.

First ask it to:

Diagnose the problem.
Identify the root cause.
Identify which files are involved.
Explain the smallest correction.

Only then implement the correction.

Prefer deletion and simplification over accumulating patches.

13. Task Boundaries

Each coding task should have:

Context
Objective
Existing contract
Files allowed to change
Files that must not change
Constraints
Acceptance criteria
Tests

Do not combine unrelated features into one task.

14. After Coding

After every implementation task, report:

Files changed
What changed
Tests added
Tests run
Dependencies added
Important architectural decisions
Known limitations
Anything uncertain
15. Learning Requirement

The developer is learning the architecture and implementation.

When a task introduces an unfamiliar concept, explain it briefly before implementing it.

Do not hide complexity behind generated abstractions.

The developer should be able to explain:

What the code does
Why it exists
Who calls it
What it returns
How it fails
What would break if it were deleted
16. Product Authority

PRODUCT.md defines what DevRadar should do.

ARCHITECTURE.md defines the current technical boundaries.

If implementation requirements conflict with either document:

STOP.

Explain the conflict.

Do not silently change the product or architecture.