# Task 2 — Prompting for Creativity

SkillCraft Technology internship task.

## Files
- `Task02_Prompting_for_Creativity.md` — report with the base prompt, three variations, observations, comparison, and conclusion.
- `Task02_Experiment_A.txt` — professional-tone experiment output.
- `Task02_Experiment_B.txt` — creative-tone experiment output.
- `Task02_Experiment_C.txt` — detailed, example-driven experiment output.
- `task2_prompt_experiment_manager.py` — local Python menu to save responses, record ratings, and generate a Markdown report.
- `task2_data/` — data folder created/used by the Python manager.

## Run the Python manager (no API key required)
Open this folder in VS Code, then open **Terminal → New Terminal** and run:

```bash
python3 task2_prompt_experiment_manager.py
```

Menu options:
1. View prompts
2. Save a generated AI output
3. Rate an experiment
4. Generate a Markdown report
5. Exit

When pasting an output into the program, type `END` on its own line when finished.

## Notes
- The Python manager does not call an AI model. Generate outputs in ChatGPT and paste them into the program.
- Review all output summaries and ratings before submitting; ratings are qualitative and subjective.
- Cost figures in startup ideas are illustrative estimates, not verified quotes.
- Do not include API keys or secrets in GitHub.
