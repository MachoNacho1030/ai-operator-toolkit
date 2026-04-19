# Architecture Decision Record

A log of the key decisions that shaped how the Hub is built and why.

---

## ADR-001: Three Repos Instead of One

**Decision:** Split the Hub into three separate repositories — ai-foundry, ai-operator-toolkit, and ai-infra-patterns.

**Why not one repo:**
A single repo mixes concerns. Code lives next to deployment config lives next to workflow definitions. When something breaks you don't know which layer caused it. Separation makes each layer independently debuggable and independently evolvable.

**Why these three:**
- Code production (foundry) and infrastructure (infra-patterns) change at different rates and for different reasons
- The operator toolkit (skills, context, agent behavior) is reusable across future foundries — it shouldn't be coupled to any one workspace
- This mirrors how real engineering organizations structure their work: application code, platform tooling, and infrastructure are owned by different teams for a reason

---

## ADR-002: Skills as Markdown Files

**Decision:** Store workflow instructions as markdown skill files in ai-operator-toolkit/skills/ rather than hardcoded behavior or a config file.

**Why markdown:**
Plain text files are version-controlled, readable by humans, and composable. You can add a new skill without touching existing ones. You can update a skill and the change is visible in git history. A JSON config or environment variable would hide this logic and make it harder to reason about.

**Why separate files per skill:**
Each skill has a single responsibility. The TDD workflow skill shouldn't know anything about git. The git workflow skill shouldn't know anything about how to explain code. Single responsibility means each file can be updated, reviewed, or replaced without side effects.

---

## ADR-003: Tests Before Code (TDD)

**Decision:** Tests are always written before the implementation. This is enforced by the tdd-workflow skill and is non-negotiable.

**Why:**
Writing tests first forces clarity about what the code is supposed to do before you write it. It eliminates the temptation to write tests that just pass whatever the implementation happens to do. It means the test suite is an honest specification, not a rubber stamp.

In a system where code is generated rather than hand-typed, this matters even more. Generated code can look correct and be wrong. Tests that were written independently of the implementation will catch that.

---

## ADR-004: Feature Branches and PRs for Every Problem

**Decision:** Every problem gets its own branch. Every branch gets a pull request. Nothing goes directly to main.

**Why:**
This is how real teams work. Main should always be in a deployable state. A branch gives you a safe space to work, a PR gives you a review checkpoint, and the merge history tells the story of how the codebase evolved.

Skipping this for "small" problems is how codebases become untrustworthy. The discipline matters most on the problems that seem too small to bother.

---

## ADR-005: Interview Mode as an Explicit Skill

**Decision:** Created a dedicated interview-mode skill that defines exactly how to present work to a non-technical audience.

**Why:**
Technical work presented without context is invisible to most audiences. An interviewer or stakeholder who doesn't code doesn't care what a hashmap is — they care whether you can explain why you made a choice, whether you can slow down and make your thinking visible, and whether the work is trustworthy.

Interview mode enforces: explain before executing, pause for questions, celebrate passing tests, never assume the audience knows what you know. This is a communication skill, and like any skill it needs a spec.
