# AI Operator Toolkit

A personal operator toolkit designed to supercharge agentic development workflows using Claude Code.

## Purpose
This repo provides skill files, prompts, and patterns that give Claude Code the context it needs to produce reliable, tested, version-controlled code — the way I want it.

## Structure
ai-operator-toolkit/
├── skills/         # Skill files that personalize how Claude Code works
├── tests/          # Test suite for validating generated code
├── agents.md       # Agent behavior definitions
├── claude.md       # Claude Code specific context and instructions
├── Makefile        # Common commands
└── FUTURE.md       # Planned improvements

## Philosophy
The skill isn't writing code anymore — it's knowing how to architect systems, direct AI precisely, and verify the output is correct.

## Repos In The Hub
- ai-operator-toolkit — this repo, skills and context for Claude Code
- ai-infra-patterns — local Docker and GCP deployment patterns
- ai-foundry — where prototyping requests are processed and PRs are created

## Tech Stack
- Claude Code
- Python 3.12
- pytest
- Git