
QUESTIONS = [
    {
        "category": "Introduction",
        "question": "Tell me about yourself and why you want to become a software developer.",
        "keywords": ["student", "programming", "skills", "project", "developer"],
    },
    {
        "category": "Python",
        "question": "What is the difference between a list and a tuple in Python?",
        "keywords": ["mutable", "immutable", "change", "element"],
    },
    {
        "category": "Problem Solving",
        "question": "How would you find a duplicate element in a list?",
        "keywords": ["set", "loop", "element", "duplicate"],
    },
    {
        "category": "Core CS",
        "question": "What is the difference between a stack and a queue?",
        "keywords": ["lifo", "fifo", "last", "first"],
    },
    {
        "category": "HR",
        "question": "Describe a challenge you faced and how you handled it.",
        "keywords": ["challenge", "action", "solution", "learned"],
    },
]


def evaluate_answer(answer, keywords):
    words = answer.lower().split()

    if len(words) < 5:
        return 1

    matches = sum(
        1 for keyword in keywords
        if keyword in answer.lower()
    )

    score = round((matches / len(keywords)) * 10)
    return max(1, min(score, 10))


def main():
    print("=" * 50)
    print("          AI INTERVIEW ASSISTANT")
    print("=" * 50)

    name = input("Enter your name: ").strip()
    role = input("Target role (e.g. Software Developer): ").strip()

    if not name:
        name = "Candidate"

    if not role:
        role = "Software Developer"

    print(f"\nWelcome, {name}!")
    print(f"Target role: {role}")
    print("\nYour interview is starting.")
    print("Answer each question in your own words.\n")

    total_score = 0

    for number, item in enumerate(QUESTIONS, start=1):
        print("-" * 50)
        print(f"Question {number}/{len(QUESTIONS)}")
        print(f"Category: {item['category']}")
        print(item["question"])

        answer = input("\nYour answer: ").strip()
        score = evaluate_answer(answer, item["keywords"])
        total_score += score

        print(f"Practice score: {score}/10\n")

    average = total_score / len(QUESTIONS)

    print("=" * 50)
    print("             INTERVIEW REPORT")
    print("=" * 50)
    print(f"Candidate: {name}")
    print(f"Target role: {role}")
    print(f"Questions answered: {len(QUESTIONS)}")
    print(f"Average practice score: {average:.1f}/10")

    print("\nImportant:")
    print("This is a basic keyword-based score, not an AI evaluation.")
    print("Your answers should be reviewed for accuracy and clarity.")
    print("=" * 50)


if __name__ == "__main__":
    main()
