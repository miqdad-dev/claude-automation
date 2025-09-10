
---

# plan.md

**Objective:**
Automate generation of a mini-hard project every 5 hours and once daily, committing automatically to GitHub.

**Plan:**
1. **Repository Setup**
   - Create GitHub repo with `.github/workflows/auto.yml`.
   - Add `scripts/generate_next.py` for orchestrating AI calls.

2. **AI Prompting**
   - Use the `claude.md` prompt to instruct Claude Code to produce full runnable projects.
   - Enforce fenced filename format for clean parsing.

3. **Project Rotation**
   - Randomly select a programming field (backend, ML, game dev, etc.) on each run.
   - Generate a fresh project under a dated folder (YYYY-MM-DD-<slug>).

4. **Workflow Automation**
   - Schedule GitHub Actions at 09:00 UTC daily and every 5 hours.
   - Workflow runs Python, installs deps, calls generator script.
   - Commit with Conventional Commit format.

5. **Testing & Quality**
   - Ensure every project includes tests.
   - Limit size to ~200–600 LOC.
   - Require clear README with instructions.

6. **Scalability**
   - Store API keys (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`) as GitHub secrets.
   - Allow switching between Claude and OpenAI easily.

---
