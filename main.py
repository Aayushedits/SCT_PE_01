
import json
import ollama


MODEL_NAME = "qwen3:1.7b"

QUESTIONS = [
    {
        "category": "Introduction",
        "question": (
            "Tell me about yourself and why you want to become "
            "a software developer."
        ),
    },
    {
        "category": "Python",
        "question": (
            "What is the difference between a list and a tuple in Python?"
        ),
    },
    {
        "category": "Problem Solving",
        "question": "How would you find a duplicate element in a list?",
    },
    {
        "category": "Core CS",
        "question": "What is the difference between a stack and a queue?",
    },
    {
        "category": "HR",
        "question": "Describe a challenge you faced and how you handled it.",
    },
]


def evaluate_answer(answer, question):
    """Evaluate an interview answer using a local Ollama model."""

    if not answer.strip():
        return {
            "score": 0,
            "feedback": "No answer was provided.",
            "strengths": "No strengths to assess yet.",
            "improvements": "Attempt the question and explain your reasoning.",
            "suggested_answer": "Start by answering the question in your own words.",
        }

    prompt = f"""
You are an experienced and fair software engineering interviewer.

Evaluate the candidate's answer using the interview question and answer below.

QUESTION:
{question}

CANDIDATE'S ANSWER:
{answer}

Evaluate:
1. Accuracy and correctness
2. Completeness and relevance
3. Clarity and explanation

Rules:
- Give an integer score from 0 to 10.
- Judge the actual content, not just keywords or answer length.
- For technical questions, prioritize technical correctness.
- For HR questions, consider relevance, actions, results, and reflection.
- Be constructive and specific.
- Do not invent facts about the candidate.
- Provide a concise, technically correct example answer where applicable.

Return a JSON object with exactly these keys:
{{
  "score": 0,
  "feedback": "Brief overall assessment",
  "strengths": "What the candidate did well",
  "improvements": "What is missing or incorrect",
  "suggested_answer": "A strong example answer"
}}
"""

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a fair interview evaluator. "
                        "Return only a valid JSON object."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            format="json",
            options={"temperature": 0.2},
        )

        result = json.loads(response["message"]["content"])

        score = int(result["score"])
        if not 0 <= score <= 10:
            raise ValueError("The model returned a score outside 0–10.")

        
        # Safely handle missing feedback fields.
        feedback = result.get("feedback", "No feedback provided.")
        strengths = result.get("strengths", "Not specified.")
        improvements = result.get(
            "improvements",
            "Explain your answer in more detail."
        )
        suggested_answer = result.get(
            "suggested_answer",
            "No suggested answer available."
        )

        return {
            "score": score,
            "feedback": str(feedback),
            "strengths": str(strengths),
            "improvements": str(improvements),
            "suggested_answer": str(suggested_answer),
        }

    
    except Exception as error:
        import traceback
        print("\nAI evaluation error:")
        traceback.print_exc()

        # Do not assign a fake score when evaluation fails.
        return {
            "score": None,
            "feedback": "This answer could not be evaluated.",
            "strengths": "Not evaluated.",
            "improvements": "Check the error above and try again.",
            "suggested_answer": "No suggestion is available."
        }

def main():
    print("=" * 55)
    print("          AI INTERVIEW ASSISTANT")
    print("=" * 55)

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
    print("AI evaluation runs locally through Ollama.")
    print("Each evaluation may take a little time.\n")

    total_score = 0
    evaluated_count = 0
    results = []

    for number, item in enumerate(QUESTIONS, start=1):
        print("\n" + "-" * 55)
        print(f"Question {number}/{len(QUESTIONS)}")
        print(f"Category: {item['category']}")
        print(item["question"])

        answer = input("\nYour answer (or type 'skip'): ").strip()

        if answer.lower() == "skip":
            print("Question skipped.")
            results.append({
                "category": item["category"],
                "score": None,
                "feedback": "Skipped.",
            })
            continue

        print("\nEvaluating your answer with the local AI model...")
        evaluation = evaluate_answer(answer, item["question"])
        score = evaluation["score"]

        if score is not None:
            total_score += score
            evaluated_count += 1
            print(f"\nPractice score: {score}/10")
        else:
            print("\nPractice score: Not available")

        print(f"Feedback: {evaluation['feedback']}")
        print(f"Strengths: {evaluation['strengths']}")
        print(f"Areas to improve: {evaluation['improvements']}")
        print(f"Suggested answer: {evaluation['suggested_answer']}")

        results.append({
            "category": item["category"],
            "score": score,
            "feedback": evaluation["feedback"],
        })

    print("\n" + "=" * 55)
    print("                  INTERVIEW REPORT")
    print("=" * 55)
    print(f"Candidate: {name}")
    print(f"Target role: {role}")
    print(f"Questions available: {len(QUESTIONS)}")
    print(f"Questions evaluated: {evaluated_count}")
    print(f"Questions skipped or not evaluated: {len(QUESTIONS) - evaluated_count}")

    if evaluated_count:
        average = total_score / evaluated_count
        print(f"Average AI practice score: {average:.1f}/10")
    else:
        print("Average AI practice score: Not available")

    print("\nIndividual results:")
    for number, result in enumerate(results, start=1):
        score_text = (
            f"{result['score']}/10"
            if result["score"] is not None
            else "Not evaluated"
        )
        print(
            f"{number}. {result['category']}: {score_text}"
            f" — {result['feedback']}"
        )

    print("\nImportant:")
    print("Scores and feedback are generated by a local AI model.")
    print("Use the feedback as practice guidance, not a definitive judgment.")
    print("=" * 55)


if __name__ == "__main__":
    main()
