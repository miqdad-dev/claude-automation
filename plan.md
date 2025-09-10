# Claude Automation Project Plan

## Overview
This is an automated project generation system that creates new mini-hard coding projects daily using AI APIs (Claude and OpenAI). The system automatically commits these projects to GitHub on a schedule.

## Architecture

### Core Components
1. **Project Generator Script** (`scripts/generate_next.py`)
   - Selects random programming fields
   - Calls AI APIs to generate complete projects
   - Parses generated content and writes files
   - Commits to Git automatically

2. **GitHub Actions Workflow** (`.github/workflows/auto.yml`)
   - Runs daily at 09:00 UTC
   - Runs every 5 hours
   - Can be triggered manually
   - Sets up Python environment and dependencies
   - Executes project generation script

3. **Environment Configuration** (`.env`)
   - API keys for Claude and OpenAI
   - Provider selection (anthropic/openai)
   - Model configuration

### Programming Fields Rotation
The system randomly selects from these fields:
- Backend API
- Frontend web/app
- Systems programming
- Data engineering
- ML/AI
- Distributed systems
- DevOps/infrastructure
- Databases
- Networking
- Security
- Compilers/interpreters
- Robotics/IoT
- Game development
- Scripting/automation

### Project Structure
Generated projects follow this pattern:
- Folder name: `YYYY-MM-DD-<field-slug>`
- Contains complete runnable code (200-600 LOC)
- Includes tests, README, and build files
- Non-trivial logic implementation
- Minimal external dependencies

## Setup Instructions

1. **Environment Variables**
   Set these in `.env` file:
   ```
   PROVIDER=openai  # or anthropic
   ANTHROPIC_API_KEY=your_claude_key
   OPENAI_API_KEY=your_openai_key
   MODEL_NAME=gpt-4  # optional, defaults based on provider
   ```

2. **GitHub Repository Secrets**
   - `ANTHROPIC_API_KEY`: Your Claude API key
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `GITHUB_TOKEN`: Automatically provided by GitHub Actions

3. **Repository Variables (Optional)**
   - `PROVIDER`: "anthropic" or "openai" (default: openai)
   - `MODEL_NAME`: Specific model to use

## Automation Schedule
- **Daily**: 09:00 UTC every day
- **Frequent**: Every 5 hours throughout the day
- **Manual**: Can be triggered via GitHub Actions UI

## Quality Assurance
- Projects must have non-trivial logic
- Include comprehensive README files
- Have working tests
- Be runnable from clean clone
- Follow best practices for the chosen field