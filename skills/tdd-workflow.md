# Skill: Test Driven Development (TDD) Workflow

## Purpose
Before any final code is produced, tests must be written and passing first.
This ensures all generated code is reliable and verified before use.

## Rules
- Always write tests BEFORE the final implementation
- Tests live in the /tests folder
- Every function must have at least one test
- Tests must pass before code is considered complete
- Use pytest for all testing

## Workflow
1. Understand the problem
2. Write the test cases first
3. Write the implementation to pass the tests
4. Run the tests and confirm passing
5. Clean up and commit

## Test Structure
- tests/conftest.py — shared fixtures and setup
- tests/test_[feature].py — tests for each feature

## Example Trigger
"Use TDD for this"
"Write tests first"
"Follow the TDD workflow"

## Running Tests
```bash
make test
```

## Philosophy
Code that isn't tested isn't done.
AI generated code especially needs verification —
just because it looks right doesn't mean it works right.