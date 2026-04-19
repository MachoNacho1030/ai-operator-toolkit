# Skill: Git Workflow

## Hard Rules

**RULE 1 — NEVER USE GH CLI.**
The `gh` command is not installed and will never be used. Never attempt `gh pr create` or any `gh` command. After pushing a branch, provide the manual PR URL in this exact format and stop:
`https://github.com/<owner>/<repo>/pull/new/<branch-name>`
Tell the user to open it themselves.

**RULE 2 — CHECKPOINT BEFORE EVERY GIT ACTION.**
Before creating a branch: checkpoint.
Before committing: checkpoint.
Before pushing: checkpoint.
See interview-mode.md for checkpoint format.

**RULE 3 — NARRATE THE REPO.**
Before any git command, state which repo you are operating in and why.
Example: "I am creating this branch in ai-foundry — that is where all solution work lives."

**RULE 4 — NEVER COMMIT DIRECTLY TO MAIN.**
All work happens on feature branches. Main is only updated via merged PRs.

**RULE 5 — ONE LOGICAL CHANGE PER COMMIT.**
Each commit covers one thing: the problem spec, the test file, the solution, or the LeetCode version (if requested). Do not bundle unrelated changes.

---

## Workflow

### Step 1 — Create Branch
Repo: wherever the work is scoped (ai-foundry for all interview problems)
Checkpoint, then:
```
git checkout -b feature/problem-name
```

### Step 2 — Do the Work
Follow tdd-workflow.md. Checkpoint between each phase.

### Step 3 — Stage and Commit
Checkpoint, then stage specific files (never `git add .` or `git add -A`):
```
git add problems/file.md solutions/file.py tests/test_file.py
git commit -m "feat: description of what this does"
```

### Step 4 — Push
Checkpoint, then:
```
git push -u origin feature/problem-name
```

### Step 5 — Provide PR URL
After pushing, provide this URL and stop. Do not attempt gh CLI.
```
https://github.com/<owner>/<repo>/pull/new/<branch-name>
```
Tell the user: "Open this URL to create the PR. I cannot create it automatically — gh CLI is not installed."

---

## Branch Naming
- `feature/problem-name` — new solution
- `fix/problem-name` — correction to existing solution
- `prep/description` — infrastructure or toolkit changes

## Commit Message Format
```
feat: short description
fix: short description
docs: short description
overhaul: short description
```

## Philosophy
Clean git history tells the story of how something was built. Every commit should be something Andrew Mason can read and understand in five seconds.
