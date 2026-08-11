
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Interview Simulator",
    layout="wide"
)

# -----------------------------
# Session State Initialization
# -----------------------------
defaults = {
    "started": False,
    "domain": "",
    "difficulty": "",
    "num_questions": 5,
    "mode": "Mock Interview"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -----------------------------
# Title
# -----------------------------
st.title("AI Based Interview Simulator with Intelligent Feedback")

st.markdown("""
Practice interviews, analyze real interview answers,
and learn interview concepts using AI.
""")

st.divider()

# -----------------------------
# Select Mode
# -----------------------------
st.subheader("Choose Mode")

mode = st.radio(
    "Select a Mode",
    [
        "Mock Interview",
        "Review My Interview",
        "Learn Interview Questions"
    ],
    horizontal=True
)

st.session_state.mode = mode

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("⚙ Interview Settings")

    domain = st.selectbox(
        "Select Domain",
        [
            "Python",
            "Machine Learning",
            "Data Science",
            "AI/ML",
            "Web Development",
            "HR Interview"
        ]
    )

    difficulty = st.selectbox(
        "Select Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    num_questions = st.slider(
        "Number of Questions",
        min_value=1,
        max_value=10,
        value=5
    )

    st.divider()

    if st.button(
        "📄 Report",
        use_container_width=True
    ):
        st.switch_page("pages/report.py")

# -----------------------------
# Configuration Preview
# -----------------------------
st.subheader("Configuration")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info(f"Mode\n\n{mode}")

with col2:
    st.info(f"Domain\n\n{domain}")

with col3:
    st.info(f"Difficulty\n\n{difficulty}")

with col4:
    st.info(f"Questions\n\n{num_questions}")

st.divider()

# -----------------------------
# Mode Descriptions
# -----------------------------
if mode == "Mock Interview":

    st.success("""
    AI will ask interview questions,
    evaluate answers,
    and provide feedback.
    """)

elif mode == "Review My Interview":

    st.info("""
    Enter a real interview question
    and the answer you gave.

    AI will identify mistakes,
    missing points,
    and suggest a better answer.
    """)

elif mode == "Learn Interview Questions":

    st.info("""
    Ask any interview question.

    AI will explain the concept,
    provide sample answers,
    and suggest follow-up questions.
    """)

st.divider()

# -----------------------------
# Continue Button
# -----------------------------
if st.button(
    "Continue",
    use_container_width=True
):

    st.session_state.started = True
    st.session_state.domain = domain
    st.session_state.difficulty = difficulty
    st.session_state.num_questions = num_questions

    st.session_state.current_question = ""
    st.session_state.question_number = 1
    st.session_state.results = []
    st.session_state.evaluation_done = False

    st.switch_page("pages/interview.py")

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "AI Based Interview Simulator with Intelligent Feedback"
)
