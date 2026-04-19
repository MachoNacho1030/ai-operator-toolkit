# Skill: Git Workflow

## Purpose
Clean revision history is non negotiable.
Every change should be tracked, meaningful, and easy to follow.

## Rules
- Always work on a feature branch, never commit directly to main
- Commit messages must be clear and descriptive
- One logical change per commit
- Always pull before starting new work
- PRs are required to merge into main

## Workflow
1. Create a new branch for the task
2. Do the work
3. Stage and commit with a clear message
4. Push the branch to GitHub
5. Open a PR with a description of what changed and why

## Branch Naming Convention
feature/short-description
fix/short-description
prep/short-description

## Commit Message Format
type: short description

examples:
feat: add tdd workflow skill file
fix: correct test assertion in test_sample.py
docs: update README with hub structure
prep: scaffold ai-operator-toolkit structure

## Common Commands
git checkout -b feature/your-branch-name
git add .
git commit -m "feat: your message here"
git push origin feature/your-branch-name

## Philosophy
Clean git history tells the story of how something was built.
It shows you think ahead, work methodically, and respect the codebase.