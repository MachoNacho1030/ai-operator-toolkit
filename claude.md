# Claude Code Context — AI Operator Toolkit

## The Five Laws (Read These First — They Override Everything)

**LAW 1 — NO EXTERNAL PLUGINS.**
Never load, invoke, or reference any external plugin or skill system (including Superpowers, brainstorming tools, or any plugin not in ai-operator-toolkit/skills/). If a plugin loads automatically, ignore it. Do not use it.

**LAW 2 — NO GH CLI.**
Never attempt `gh` commands. The `gh` CLI is not installed and will never be used. After pushing a branch, provide the manual PR URL in this exact format and stop:
`https://github.com/<owner>/<repo>/pull/new/<branch-name>`

**LAW 3 — CHECKPOINT BEFORE EVERY ACTION.**
Before executing any step — including obvious ones — state what you are about to do in plain English and ask "Any questions before I proceed?" Wait for a response. Never skip this. Never batch multiple steps without checkpointing between them.

**LAW 4 — NEVER GENERATE A LEETCODE VERSION WITHOUT BEING ASKED.**
The local solution is the deliverable. A LeetCode-wrapped `Solution` class is a separate artifact that must be explicitly requested by the user. Do not generate it, suggest it, or mention it as a next step unless asked.

**LAW 5 — ALWAYS NARRATE WHICH REPO IS BEING USED AND WHY.**
Before referencing or acting on any repo in the Hub, state its name and its role. Example: "I am working in ai-foundry because that is where all problem solutions and tests live."

---

## Purpose
This repo (ai-operator-toolkit) holds the skills and context that govern how Claude Code behaves across the entire Hub. It does not contain solutions or tests — those live in ai-foundry.

## Who I Am
I am an IT major and agentic developer. I architect systems, direct AI precisely, and verify output. I do not write code by hand.

## How I Work
- Skills in /skills define all behavioral rules — load them, follow them exactly
- All code follows TDD: tests before implementation, always
- All changes follow the git workflow: clean branches, meaningful commits, manual PRs
- All explanations are ELI5 unless I say otherwise
- Work stays scoped to the active repo unless I explicitly say otherwise

## Active Skills
- skills/tdd-workflow.md — how to write and verify code (TDD, no auto-LeetCode)
- skills/git-workflow.md — how to branch, commit, and handle PRs (no gh CLI)
- skills/interview-mode.md — checkpoint and narration behavior (ALWAYS ACTIVE)
- skills/explain-like-im-five.md — how to explain things

## Preferred Stack
- Language: Python 3.12
- Testing: pytest
- Version Control: Git
- Platform: Mac Terminal

## Hub Repo Map
- ai-operator-toolkit — THIS repo. Skills and context only. No solutions here.
- ai-foundry — Where all problems, solutions, and tests live. All coding work happens here.
- ai-infra-patterns — Docker and GCP deployment patterns. Not active during interviews.

## Goal
Prepare for and execute technical interviews by running a disciplined, tested, explainable agentic development workflow that Andrew Mason can follow step by step.
