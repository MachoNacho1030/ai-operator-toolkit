# Claude Code Context

## Purpose
This file gives Claude Code the context it needs to work the way I want it to.
Read this before doing anything in this repo.

## Who I Am
I am an IT major and agentic developer who uses AI to design and ship reliable tested code at speed.
I do not write code by hand — I architect systems, direct AI precisely, and verify output is correct.

## How I Work
- I use skill files in /skills to personalize how you behave
- All code must follow TDD workflow — tests before implementation
- All changes must follow the git workflow — clean branches and commits
- When I ask for an explanation use ELI5 unless I say otherwise
- Only work on files in this repo unless I explicitly say otherwise
- Use the Superpowers plugin to enhance capabilities where available

## Active Skills
- skills/explain-like-im-five.md — how to explain things to me
- skills/tdd-workflow.md — how to write and verify code
- skills/git-workflow.md — how to commit and branch

## Rules
- Never touch files outside this repo
- Always write tests before implementation
- Always explain what you are doing and why
- If something is unclear ask me before assuming
- Keep code simple and readable
- Always leverage the Superpowers plugin for enhanced context and capabilities

## Preferred Stack
- Language: Python 3.12
- Testing: pytest
- Version Control: Git
- Platform: Mac Terminal
- Containerization: Docker (spin up local containers to view progress before deploying)

## Local Development Workflow
1. Write and test code locally first
2. Spin up Docker container to verify in isolated environment
3. Confirm everything works in container
4. Commit and push clean branch to GitHub
5. Open PR

## Superpowers Plugin
The Superpowers plugin is used to enhance Claude Code capabilities including:
- Extended context awareness across the Hub repos
- Personalized skill file loading
- ELI5 explanation mode
- TDD enforcement
- Git workflow automation
- Docker container management
Always activate Superpowers at the start of a new session for best results.

## Repo Scope
This repo is part of a larger system called the Hub which contains:
- ai-operator-toolkit — this repo, skills and context for Claude Code
- ai-infra-patterns — local Docker and GCP deployment patterns
- ai-foundry — where prototyping requests are processed and PRs are created

Only work within the repo I am currently in unless explicitly told otherwise.
Scope discipline is critical to keeping the Hub clean and organized.

## Goal For This Repo
Prepare for a technical interview by mirroring my agentic development workflow.
Be able to solve LeetCode style problems using TDD, clean git history, clear explanation,
and local Docker containerization before final commit.