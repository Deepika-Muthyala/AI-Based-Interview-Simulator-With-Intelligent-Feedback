import streamlit as st

st.set_page_config(
    page_title="Interview Report",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Final Interview Report")

# Check interview data
if "results" not in st.session_state:
    st.error("No interview data found.")
    st.stop()

results = st.session_state.results

if len(results) == 0:
    st.error("No interview data found.")
    st.stop()

# Calculate Scores
technical_total = 0
communication_total = 0
completeness_total = 0

for item in results:
    evaluation = item["evaluation"]

    technical_total += evaluation["technical_score"]
    communication_total += evaluation["communication_score"]
    completeness_total += evaluation["completeness_score"]

total_score = (
    technical_total
    + communication_total
    + completeness_total
)

max_score = len(results) * 75

percentage = round(
    (total_score / max_score) * 100,
    2
)

# Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Needs Improvement"

# Summary Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Technical",
        technical_total
    )

with col2:
    st.metric(
        "Communication",
        communication_total
    )

with col3:
    st.metric(
        "Completeness",
        completeness_total
    )

with col4:
    st.metric(
        "Overall %",
        f"{percentage}%"
    )

st.success(f"Final Grade: {grade}")

st.divider()

# Detailed Results
st.subheader("Question Wise Analysis")

for i, item in enumerate(results, start=1):

    evaluation = item["evaluation"]

    with st.expander(f"Question {i}"):

        st.write("### Question")
        st.write(item["question"])

        st.write("### Your Answer")
        st.write(item["answer"])

        st.write("### Scores")

        st.write(
            f"Technical Score: {evaluation['technical_score']}/25"
        )

        st.write(
            f"Communication Score: {evaluation['communication_score']}/25"
        )

        st.write(
            f"Completeness Score: {evaluation['completeness_score']}/25"
        )

        st.write("### Strengths")

        for strength in evaluation["strengths"]:
            st.write(f"✅ {strength}")

        st.write("### Weaknesses")

        for weakness in evaluation["weaknesses"]:
            st.write(f"❌ {weakness}")

        st.write("### Improvement Tips")

        for tip in evaluation["improvement_tips"]:
            st.write(f"💡 {tip}")

        st.write("### Ideal Answer")
        st.write(evaluation["ideal_answer"])

st.divider()

# Restart Interview
if st.button("🔄 Start New Interview"):

    keys_to_remove = [
        "started",
        "domain",
        "difficulty",
        "num_questions",
        "current_question",
        "question_number",
        "results",
        "evaluation_done"
    ]

    for key in keys_to_remove:
        if key in st.session_state:
            del st.session_state[key]

    st.switch_page("app.py")