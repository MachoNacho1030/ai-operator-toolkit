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
6. Optional: LeetCode Judge Verification

## Optional: LeetCode Judge Verification
After pytest passes locally, there is an optional final verification step — run the solution on LeetCode to confirm it passes the judge's hidden test cases.

LeetCode requires solutions to be wrapped in a Solution class like this:

```python
class Solution:
    def method_name(self, params):
        # solution code here
```

Our local solutions are standalone functions. If LeetCode verification is requested, adapt the solution into the LeetCode class format, confirm it passes, then note the result.

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