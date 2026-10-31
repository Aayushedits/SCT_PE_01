
import streamlit as st
import ollama
import storage
import json

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #111827);
    color: #f3f4f6;
}
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}
.hero {
    padding: 28px;
    border-radius: 18px;
    background: linear-gradient(120deg, #172554, #312e81);
    border: 1px solid #3730a3;
    margin-bottom: 25px;
}
.hero h1 {
    color: white;
    font-size: 2.4rem;
    margin-bottom: 8px;
}
.hero p {
    color: #c7d2fe;
    font-size: 1.05rem;
}
.metric-card {
    padding: 18px;
    border-radius: 14px;
    background: #172033;
    border: 1px solid #2b3852;
    margin-bottom: 12px;
}
div[data-testid="stForm"] {
    background: #151e30;
    border: 1px solid #2b3852;
    padding: 22px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- INTERVIEW QUESTIONS ----------------
QUESTIONS = [
    {
        "category": "Introduction",
        "question": "Tell me about yourself and why you want to become a software developer."
    },
    {
        "category": "Python",
        "question": "What is the difference between a list and a tuple in Python?"
    },
    {
        "category": "Problem Solving",
        "question": "How would you find a duplicate element in a list in Python?"
    },
    {
        "category": "Core CS",
        "question": "What is the difference between a stack and a queue?"
    },
    {
        "category": "HR",
        "question": "Describe a challenge you faced and how you handled it."
    }
]

MODEL_NAME = "qwen3:1.7b"

# ---------------- SESSION STATE ----------------
if "answers" not in st.session_state:
    st.session_state.answers = {}

if "results" not in st.session_state:
    st.session_state.results = {}

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

if "candidate_name" not in st.session_state:
    st.session_state.candidate_name = ""

if "target_role" not in st.session_state:
    st.session_state.target_role = "Software Developer"

if "saved_interview_id" not in st.session_state:
    st.session_state.saved_interview_id = None


# ---------------- AI EVALUATION ----------------
def evaluate_answer(question, answer, role):
    prompt = f"""
You are a professional technical interviewer.

Evaluate the candidate's answer fairly and constructively.

Target role: {role}
Interview question: {question}
Candidate answer: {answer}

Return ONLY a valid JSON object with these exact keys:
{{
  "score": 0,
  "feedback": "Brief evaluation",
  "strengths": "What was done well",
  "improvements": "What should improve",
  "suggested_answer": "A stronger sample answer"
}}

Rules:
- Score must be an integer from 0 to 10.
- Evaluate relevance, correctness, clarity and completeness.
- Do not award a high score to an irrelevant answer.
- Do not invent experience or achievements for the candidate.
- Be constructive and concise.
"""
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        format="json"
    )

    result = json.loads(response["message"]["content"])

    score = int(result["score"])
    if not 0 <= score <= 10:
        raise ValueError("The AI returned a score outside 0–10.")

    return {
        "score": score,
        "feedback": str(result["feedback"]),
        "strengths": str(result["strengths"]),
        "improvements": str(result["improvements"]),
        "suggested_answer": str(result["suggested_answer"])
    }


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🎯 Interview Studio")
    st.caption("Local AI • Powered by Ollama")
    st.divider()

    st.markdown("### Your session")
    st.write(f"**Candidate:** {st.session_state.candidate_name or 'Not started'}")
    st.write(f"**Role:** {st.session_state.target_role}")

    answered_count = sum(
        1 for answer in st.session_state.answers.values()
        if answer.strip()
    )
    st.progress(answered_count / len(QUESTIONS))
    st.caption(f"{answered_count} of {len(QUESTIONS)} answers written")

    st.divider()
    st.caption(f"Model: {MODEL_NAME}")
    st.caption("Answers are evaluated using your local Ollama model.")

    


    
if st.button("🔄 Reset interview", use_container_width=True):
    st.session_state.answers = {}
    st.session_state.results = {}
    st.session_state.current_question = 0
    st.session_state.interview_started = False
    st.session_state.candidate_name = ""
    st.session_state.target_role = "Software Developer"
    st.session_state.saved_interview_id = None
    st.session_state.show_results = False
    st.rerun()






# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>🎯 AI Interview Assistant</h1>
    <p>Practice smarter. Improve your answers. Prepare with confidence.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- CANDIDATE SETUP ----------------
if not st.session_state.interview_started:
    st.markdown("### Let's set up your interview")
    st.write("Enter your details to begin your personalized practice session.")

    with st.form("candidate_setup"):
        candidate_name = st.text_input(
            "Your name",
            placeholder="Enter your name"
        )
        target_role = st.selectbox(
            "Target role",
            [
                "Software Developer",
                "Python Developer",
                "AI/ML Engineer",
                "Data Analyst",
                "Web Developer",
                "Software Engineering Intern"
            ]
        )
        start = st.form_submit_button(
            "Start interview →",
            use_container_width=True
        )

        if start:
            if not candidate_name.strip():
                st.error("Please enter your name first.")
            else:
                st.session_state.candidate_name = candidate_name.strip()
                st.session_state.target_role = target_role
                st.session_state.interview_started = True
                st.rerun()

    st.stop()


# ---------------- INTERVIEW WORKSPACE ----------------
if not st.session_state.get("show_results", False):
    index = st.session_state.current_question
    question_data = QUESTIONS[index]
    question_number = index + 1

    st.progress(question_number / len(QUESTIONS))

    st.markdown(
        f"### Question {question_number} of {len(QUESTIONS)}"
    )
    st.caption(f"Category: {question_data['category']}")
    st.markdown(f"## {question_data['question']}")

    with st.form(f"answer_form_{index}"):
        answer = st.text_area(
            "Your answer",
            value=st.session_state.answers.get(index, ""),
            placeholder="Explain your approach in your own words...",
            height=200
        )

        left, right = st.columns(2)
        with left:
            previous = st.form_submit_button(
                "← Previous",
                disabled=(index == 0),
                use_container_width=True
            )
        with right:
            next_label = (
                "Finish interview →"
                if index == len(QUESTIONS) - 1
                else "Save & next →"
            )
            next_button = st.form_submit_button(
                next_label,
                type="primary",
                use_container_width=True
            )

        if previous:
            st.session_state.answers[index] = answer
            st.session_state.current_question -= 1
            st.rerun()

        if next_button:
            if not answer.strip():
                st.warning("Please write an answer before continuing.")
            else:
                st.session_state.answers[index] = answer.strip()

                if index < len(QUESTIONS) - 1:
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    st.session_state.show_results = True
                    st.rerun()


# ---------------- RESULTS DASHBOARD ----------------
if st.session_state.get("show_results", False):
    st.markdown("## 📊 Your interview report")
    st.write(
        f"Candidate: **{st.session_state.candidate_name}**  ·  "
        f"Role: **{st.session_state.target_role}**"
    )

    if st.button("✨ Evaluate all answers", type="primary"):
        for index, question_data in enumerate(QUESTIONS):
            if index in st.session_state.results:
                continue

            answer = st.session_state.answers.get(index, "")
            if not answer.strip():
                continue

            with st.spinner(
                f"Evaluating question {index + 1} of {len(QUESTIONS)}..."
            ):
                try:
                    st.session_state.results[index] = evaluate_answer(
                        question_data["question"],
                        answer,
                        st.session_state.target_role
                    )
                except Exception as error:
                    st.error(
                        f"Question {index + 1} failed: {error}. "
                        "Check that Ollama is running and the model is installed."
                    )

    results = st.session_state.results

    if results:
        average = sum(
            result["score"] for result in results.values()
        ) / len(results)

        first, second, third = st.columns(3)
        first.metric("Questions evaluated", f"{len(results)}/{len(QUESTIONS)}")
        second.metric("Average score", f"{average:.1f}/10")
        third.metric(
            "Strong answers",
            sum(1 for result in results.values() if result["score"] >= 7)
        )

        st.divider()

        for index, result in sorted(results.items()):
            question_data = QUESTIONS[index]

            with st.expander(
                f"Q{index + 1}. {question_data['category']} "
                f"— {result['score']}/10",
                expanded=(index == 0)
            ):
                st.markdown("**Question**")
                st.write(question_data["question"])

                st.markdown("**Your answer**")
                st.write(st.session_state.answers.get(index, ""))

                st.markdown("**AI feedback**")
                st.write(result["feedback"])

                st.markdown("**Strengths**")
                st.write(result["strengths"])

                st.markdown("**Areas to improve**")
                st.write(result["improvements"])

                st.markdown("**Suggested answer**")
                st.write(result["suggested_answer"])

        report = {
            "candidate": st.session_state.candidate_name,
            "target_role": st.session_state.target_role,
            "average_score": round(average, 2),
            "results": [
                {
                    "question": QUESTIONS[index]["question"],
                    "answer": st.session_state.answers.get(index, ""),
                    **result
                }
                for index, result in sorted(results.items())
            ]
        }
            
        if st.session_state.saved_interview_id is None:
            try:
                saved_id = storage.save_interview(report)
                st.session_state.saved_interview_id = saved_id
                st.success(f"Interview saved to local history (ID: {saved_id}).")
            except Exception as error:
                st.error(f"Could not save interview history: {error}")


        st.download_button(
            "⬇️ Download interview report (JSON)",
            data=json.dumps(report, indent=2),
            file_name="interview_report.json",
            mime="application/json"
        )

    else:
        st.info("Submit your answers, then select Evaluate all answers.")
