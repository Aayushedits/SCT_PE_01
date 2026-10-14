"""
Task 2: Prompting for Creativity
Prompt Experiment Manager

This local Python app helps you:
1. View the base prompt and three prompt variations.
2. Save AI-generated outputs that you copy from ChatGPT.
3. Rate each experiment.
4. Generate a Markdown report for GitHub.

No external packages or API key are required.
"""

from pathlib import Path
import json
from datetime import datetime

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "task2_data"
OUTPUTS_DIR = DATA_DIR / "outputs"
DATA_FILE = DATA_DIR / "experiments.json"
REPORT_FILE = PROJECT_DIR / "Task02_Comparison_Report.md"

PROMPTS = {
    "Base Prompt": (
        "Generate 3 innovative startup ideas that solve real problems faced by "
        "college students in India. For each idea, provide a name, the problem "
        "it solves, the target audience, its unique selling point, and a simple "
        "monetization strategy. Keep the ideas practical, creative, and suitable "
        "for a student founder with a limited budget."
    ),
    "Experiment A - Professional Tone": (
        "Generate 3 startup ideas that solve real problems faced by college "
        "students in India. Use a professional and business-oriented tone. For "
        "each idea, explain the problem statement, proposed solution, target "
        "market, competitive advantage, and revenue model. Prioritize feasibility "
        "and market relevance for a student founder with a limited budget."
    ),
    "Experiment B - Creative Tone": (
        "Act as a highly creative startup innovator. Generate 3 original and "
        "unconventional startup ideas that solve real problems faced by college "
        "students in India. Give each idea a memorable name, a surprising "
        "solution, a unique selling point, and a practical revenue model. Avoid "
        "generic ideas while keeping them achievable for a student founder with "
        "a limited budget."
    ),
    "Experiment C - Detailed Output": (
        "Generate 3 startup ideas that solve real problems faced by college "
        "students in India. For each idea, explain the problem, proposed solution, "
        "target audience, unique selling point, a realistic example of how a "
        "student would use it, estimated initial costs with assumptions, and a "
        "potential revenue model. Provide specific and actionable details while "
        "keeping each idea feasible for a student founder with a limited budget."
    ),
}


def load_data():
    """Load saved experiment data, or return an empty structure."""
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Warning: saved data could not be read. Starting with empty data.")
    return {
        name: {"output": "", "ratings": {}, "notes": ""}
        for name in PROMPTS
    }


def save_data(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def show_prompts():
    print("\nPROMPTS")
    print("=" * 72)
    for name, prompt in PROMPTS.items():
        print(f"\n{name}\n{'-' * len(name)}\n{prompt}")


def save_output(data):
    names = list(PROMPTS.keys())
    print("\nChoose the experiment to save:")
    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")

    choice = input("Enter number: ").strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(names):
        print("Invalid choice.")
        return

    name = names[int(choice) - 1]
    print(
        "\nPaste the AI-generated response below.\n"
        "When finished, enter a new line containing only: END"
    )

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    output = "\n".join(lines).strip()
    if not output:
        print("No output entered; nothing saved.")
        return

    data[name]["output"] = output
    save_data(data)

    safe_name = (
        name.lower()
        .replace(" ", "_")
        .replace("-", "")
    )
    output_path = OUTPUTS_DIR / f"{safe_name}.txt"
    output_path.write_text(output, encoding="utf-8")
    print(f"\nSaved response to: {output_path}")


def rate_experiment(data):
    names = list(PROMPTS.keys())
    print("\nChoose an experiment to rate:")
    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")

    choice = input("Enter number: ").strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(names):
        print("Invalid choice.")
        return

    name = names[int(choice) - 1]
    criteria = [
        ("Tone match", "Does the output match the intended tone?"),
        ("Creativity", "How original and interesting are the ideas?"),
        ("Detail", "How specific and complete is the output?"),
        ("Practicality", "How feasible are the ideas for a student founder?"),
    ]

    ratings = {}
    print("\nRate each criterion from 1 (low) to 5 (high).")
    for key, question in criteria:
        while True:
            value = input(f"{key}: {question} ").strip()
            if value.isdigit() and 1 <= int(value) <= 5:
                ratings[key] = int(value)
                break
            print("Please enter a number from 1 to 5.")

    notes = input("Optional observation about this output: ").strip()
    data[name]["ratings"] = ratings
    data[name]["notes"] = notes
    save_data(data)
    print(f"Ratings saved for {name}.")


def generate_report(data):
    lines = [
        "# Task 2: Prompting for Creativity",
        "",
        "**Internship:** SkillCraft Technology  ",
        "**Project theme:** Startup ideas for college students in India  ",
        f"**Report generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Objective",
        "",
        "This experiment explores how changing prompt wording affects AI-generated "
        "startup ideas. Outputs are reviewed for tone, creativity, detail, and practicality.",
        "",
    ]

    for name, prompt in PROMPTS.items():
        record = data.get(name, {})
        lines.extend([
            f"## {name}",
            "",
            "### Prompt",
            "",
            f"> {prompt}",
            "",
            "### Generated output",
            "",
            record.get("output", "").strip() or
            "_No output saved yet. Use the application to paste the actual AI response._",
            "",
            "### Evaluation",
            "",
        ])

        ratings = record.get("ratings", {})
        if ratings:
            lines.extend([
                "| Criterion | Score (1–5) |",
                "|---|---:|",
            ])
            for criterion in ("Tone match", "Creativity", "Detail", "Practicality"):
                score = ratings.get(criterion, "Not rated")
                lines.append(f"| {criterion} | {score} |")
            lines.append("")
        else:
            lines.extend(["_Not rated yet._", ""])

        if record.get("notes"):
            lines.extend(["**Observation:** " + record["notes"], ""])

    lines.extend([
        "## Comparative summary",
        "",
        "| Experiment | Tone | Creativity | Detail | Practicality |",
        "|---|---:|---:|---:|---:|",
    ])

    for name in PROMPTS:
        ratings = data.get(name, {}).get("ratings", {})
        values = [ratings.get(key, "—") for key in
                  ("Tone match", "Creativity", "Detail", "Practicality")]
        lines.append(f"| {name} | " + " | ".join(map(str, values)) + " |")

    lines.extend([
        "",
        "## Conclusion",
        "",
        "Complete this section after reviewing the actual outputs. Explain which prompt "
        "best matched each goal and support the conclusion with observations from your comparison.",
        "",
        "## Limitations",
        "",
        "- Ratings are subjective and based on a small set of generated responses.",
        "- Any cost estimates should be treated as estimates unless independently verified.",
        "- Startup concepts should be validated with real students before business decisions are made.",
        "",
    ])

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport generated: {REPORT_FILE}")
    print("Open the Markdown file and complete the conclusion before submitting it.")


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    data = load_data()

    while True:
        print("\n" + "=" * 48)
        print(" TASK 2: PROMPT EXPERIMENT MANAGER")
        print("=" * 48)
        print("1. View prompts")
        print("2. Save a generated AI output")
        print("3. Rate an experiment")
        print("4. Generate GitHub Markdown report")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_prompts()
        elif choice == "2":
            save_output(data)
        elif choice == "3":
            rate_experiment(data)
        elif choice == "4":
            generate_report(data)
        elif choice == "5":
            save_data(data)
            print("Saved. Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
