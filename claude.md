# claude.md

````
You are Claude Code. Output a COMPLETE, RUNNABLE “mini-hard” project with non-trivial logic.

GOAL
- Build a new mini-hard project (not trivial “hello world”) from a RANDOM field of programming.
- Include automation so GitHub commits a new dated project daily AND every 5 hours.

FIELDS (pick 1 randomly each run; rotate widely):
- backend api, frontend web/app, systems programming, data engineering, ml/ai, distributed systems, devops/infrastructure, databases, networking, security, compilers/interpreters, robotics/iot, game dev, scripting/automation.

CONSTRAINTS
- Root folder name MUST be: YYYY-MM-DD-<short-slug>  (today’s UTC date).
- Provide ALL files strictly as fenced blocks in this exact format (no language tag, no extra commentary outside blocks):

```path/filename
<file content here>
````

REQUIRED CONTENTS

1. Source code implementing a mini-hard project (≥1 substantial module).
2. README.md with:

   * what it does
   * how it works
   * how to run (exact commands)
   * example usage
   * notes on architecture & tradeoffs
3. Tests (unit or integration).
4. If applicable: Dockerfile or Compose; otherwise Makefile or a task runner.
5. A small sample dataset or fixtures if helpful.
6. Lint/format config if applicable.
7. A GitHub Actions workflow that runs on a schedule AND can generate/commit new dated folders automatically.

AUTOMATION DESIGN

* Include: `.github/workflows/auto.yml`
* Triggers:

  * cron: "0 9 \* \* \*"           # daily 09:00 UTC
  * cron: "0 \*/5 \* \* \*"         # every 5 hours
  * workflow\_dispatch:
* The workflow MUST:

  * set up Python 3.11
  * install deps from `requirements.txt`
  * run `scripts/generate_next.py` which:

    * picks a RANDOM field (from the list above),
    * creates a NEW dated folder (YYYY-MM-DD-<slug>) with a DIFFERENT project than before,
    * writes code/tests/readme as files,
    * commits & pushes.
* `scripts/generate_next.py` MUST support BOTH Anthropic (Claude) and OpenAI via env:

  * `PROVIDER` = "anthropic" or "openai"
  * `ANTHROPIC_API_KEY` (for Claude)
  * `OPENAI_API_KEY` (for OpenAI) = ''
  * Optional: `MODEL_NAME`
* Put a robust prompt inside `scripts/generate_next.py` to ask the model to emit files using the same fenced-filename format and then parse/write them.
* Store PAT/security via repo secrets. In workflow, configure git user and commit using Conventional Commits style, e.g. `feat(auto): add project 2025-09-09-<slug>`.

QUALITY BAR

* Non-trivial logic (e.g., algorithms, concurrency, state machines, streaming, indexing, parsers, protocol, etc.).
* Keep external deps minimal. Ensure README run steps work from a clean clone.
* Total LOC target: 200–600.
* Ensure tests pass locally (`make test` or `pytest` etc.).
* If web, include index.html + script.js (+ optional css) and a tiny local server if needed.

DELIVERABLES

* Output ONLY fenced filename blocks for every file (source, README, tests, scripts, workflow, requirements, etc.).
* Do NOT include explanation outside the blocks.

