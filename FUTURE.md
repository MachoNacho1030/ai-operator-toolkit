# Future Improvements

## Purpose
This file tracks planned improvements and future considerations for the Hub.
These are not current priorities but are important to keep in mind as the system grows.

## Planned Improvements

### 1. Transpose Layer
A transpose.py script that makes the Hub work regardless of the agentic tool being used.
Currently the Hub is built specifically for Claude Code.
The transpose layer would allow any AI agent to plug in and work the same way.

Supported agents planned:
- Claude Code (current)
- Gemini CLI
- GPT Engineer
- Aider
- Continue.dev

### 2. Infra Agent
A dedicated agent in ai-infra-patterns that handles:
- Local Docker container management
- GCP deployment via Pulumi and Terraform
- Environment variable management
- Infrastructure as Code patterns

### 3. Foundry Agent
A dedicated agent in ai-foundry that handles:
- Processing prototyping requests
- Creating feature branches automatically
- Managing PRs end to end
- Tracking prototype progress

### 4. MCP Integration
Full MCP server integration to give agents access to:
- GitHub API
- GCP APIs
- Docker API
- Custom tool servers

### 5. Hub CLI
A command line tool that lets you manage the entire Hub from one place:
- Start a new prototype
- Check status of all repos
- Run all tests across repos
- Deploy to GCP

### 6. Automated Testing Pipeline
A CI/CD pipeline that:
- Runs tests on every PR
- Blocks merges if tests fail
- Generates test coverage reports
- Notifies on failures

### 7. GCP Deployment
Full deployment pipeline from local Docker to GCP:
- Cloud Run for containerized apps
- Cloud Storage for static assets
- Cloud Build for CI/CD
- Terraform for infrastructure management

## Philosophy
The Hub is a living system.
It grows as my skills and needs grow.
Every improvement should make the system faster, cleaner, and more reliable.