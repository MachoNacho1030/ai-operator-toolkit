# Skill: Test Driven Development (TDD) Workflow

## Hard Rules

**RULE 1 — TESTS BEFORE CODE. ALWAYS.**
No implementation file is created until a test file exists and has been run to confirm it fails. No exceptions.

**RULE 2 — NEVER GENERATE A LEETCODE VERSION WITHOUT EXPLICIT REQUEST.**
The deliverable is a standalone Python function. A LeetCode `Solution` class wrapper is a separate artifact. Do not generate it, suggest it, offer it, or mention it as a next step. Wait until the user explicitly asks: "Can you make the LeetCode version?" or equivalent.

**RULE 3 — CHECKPOINT BEFORE EACH PHASE.**
Before writing tests: checkpoint.
Before writing implementation: checkpoint.
Before running tests: checkpoint.
Before committing: checkpoint.
See interview-mode.md for checkpoint format.

**RULE 4 — ALL WORK STAYS IN AI-FOUNDRY.**
Tests go in ai-foundry/tests/. Solutions go in ai-foundry/solutions/. Problems go in ai-foundry/problems/. Nothing goes anywhere else.

---

## Workflow

### Phase 1 — Write the Problem Spec
Repo: ai-foundry/problems/
Create a markdown file with the problem statement, examples, and constraints.
Checkpoint before creating.

### Phase 2 — Write the Tests
Repo: ai-foundry/tests/
Write test_[problem_name].py covering:
- All provided examples
- Edge cases: single element, all negatives, duplicates, empty-adjacent inputs
- No solution exists yet — tests will fail on import

Checkpoint before writing.

### Phase 3 — Confirm RED
Run the tests. They must fail with an ImportError or NameError (solution doesn't exist yet).
If they pass without a solution, the tests are wrong — fix them before proceeding.

Checkpoint before running.

### Phase 4 — Write the Implementation
Repo: ai-foundry/solutions/
Write the standalone function solution — the minimum code to pass the tests.
No extra features. No LeetCode wrapper. No class. Just the function.

Checkpoint before writing.

### Phase 5 — Confirm GREEN
Run the tests. All must pass. Output must be clean — no errors, no warnings.
If any test fails, fix the implementation, not the test.

Checkpoint before running.

### Phase 6 — Commit
Follow git-workflow.md. Commit with a clear message.

Checkpoint before committing.

---

## Test Structure

- ai-foundry/tests/test_[problem_name].py — one file per problem
- Import from solutions.[problem_name]
- Use pytest assertions
- Cover: provided examples, edge cases, error conditions

## Solution Structure

- ai-foundry/solutions/[problem_name].py — standalone function, no class wrapper
- Function signature matches the problem spec
- No LeetCode formatting unless explicitly requested

## Philosophy
Code that is not tested is not done. AI-generated code especially needs tests — it looks right more often than it is right.
