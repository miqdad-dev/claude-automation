```

# task.md

### Tasks

1. **Repository Bootstrapping**
   - [ ] Create GitHub repository `auto-projects`.
   - [ ] Add `.gitignore` and `requirements.txt`.

2. **Claude Prompt Integration**
   - [ ] Save the `claude.md` file with full AI instructions.
   - [ ] Implement parser in `scripts/generate_next.py` to handle fenced filename outputs.

3. **Workflow Setup**
   - [ ] Write `.github/workflows/auto.yml` with daily + 5-hour cron.
   - [ ] Configure git user/email inside workflow.
   - [ ] Test commit cycle manually with `workflow_dispatch`.

4. **Project Generation Script**
   - [ ] Implement logic to:
       - Choose random programming field.
       - Prompt Claude Code.
       - Parse outputs into new dated folder.
       - Ensure fallback project if AI fails.

5. **Testing & Validation**
   - [ ] Confirm generated projects are non-trivial.
   - [ ] Run tests included by Claude.
   - [ ] Validate README run instructions.

6. **Secrets & Config**
   - [ ] Add GitHub secrets: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`.
   - [ ] Add Actions variables: `PROVIDER`, `MODEL_NAME`.

7. **Continuous Improvement**
   - [ ] Monitor output quality.
   - [ ] Tune prompt if outputs are too trivial or too large.
   - [ ] Add optional project themes via `TOPIC_PLAN`.

```
