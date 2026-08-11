import streamlit as st
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder

from utils.question_generator import generate_question
from utils.evaluator import evaluate_answer
from utils.learn_mode import explain_topic
from utils.review_mode import review_answer
from utils.speech_to_text import transcribe_audio

st.set_page_config(
    page_title="Interview",
    page_icon="🎤",
    layout="wide"
)

st.title(" AI Interview Session")

# ==================================
# SESSION CHECK
# ==================================

if "started" not in st.session_state or not st.session_state.started:
    st.warning("Please start from Home Page.")
    st.stop()

mode = st.session_state.get(
    "mode",
    "Mock Interview"
)

# ==================================
# MOCK INTERVIEW MODE
# ==================================

if mode == "Mock Interview":

    if "current_question" not in st.session_state:
        st.session_state.current_question = ""

    if "question_number" not in st.session_state:
        st.session_state.question_number = 1

    if "results" not in st.session_state:
        st.session_state.results = []

    if "evaluation_done" not in st.session_state:
        st.session_state.evaluation_done = False

    if "answer_box" not in st.session_state:
        st.session_state.answer_box = ""

    # ==================================
    # GENERATE QUESTION
    # ==================================

    if st.session_state.current_question == "":

        with st.spinner("Generating Question..."):

            st.session_state.current_question = generate_question(
                st.session_state.domain,
                st.session_state.difficulty
            )

    st.subheader(
        f"Question {st.session_state.question_number} of {st.session_state.num_questions}"
    )

    st.info(
        st.session_state.current_question
    )

    # ==================================
    # QUESTION AUDIO
    # ==================================

    try:

        tts = gTTS(
            text=st.session_state.current_question,
            lang="en"
        )

        audio_file = "question.mp3"

        tts.save(audio_file)

        st.audio(audio_file)

    except Exception as e:

        st.warning(
            f"Audio Error: {e}"
        )

    # ==================================
    # ANSWER INPUT
    # ==================================

    
    answer = st.text_area(
        "Your Answer",
        value=st.session_state.answer_box,
        height=200,
        placeholder="Type your answer here..."
    )
    if st.session_state.answer_box:
        st.info("Recognized Speech")
        st.code(st.session_state.answer_box)

    st.markdown(
        "### 🎤 Voice Answer"
    )

    audio = mic_recorder(
        start_prompt="🎙 Start Recording",
        stop_prompt="⏹ Stop Recording",
        key="voice_recorder"
    )

    if audio:

        st.success(
            "Voice Recorded Successfully"
        )

        try:

            with open(
                "recorded_audio.wav",
                "wb"
            ) as f:

                f.write(
                    audio["bytes"]
                )

            text = transcribe_audio(
                "recorded_audio.wav"
            )

            st.session_state.answer_box = text

            st.success(
                "Speech converted to text successfully!"
            )

            

        except Exception as e:

            st.error(
                f"Transcription Error: {e}"
            )

    # ==================================
    # SUBMIT ANSWER
    # ==================================

    if st.button(
        "Submit Answer",
        use_container_width=True
    ):

        user_answer = answer

        if not user_answer.strip():
            user_answer = st.session_state.answer_box

        if user_answer.strip() == "":

            st.error(
                "Please enter your answer."
            )

        else:

            with st.spinner(
                "Evaluating Answer..."
            ):

                evaluation = evaluate_answer(
                    st.session_state.current_question,
                    user_answer
                )

                st.session_state.results.append(
                    {
                        "question": st.session_state.current_question,
                        "answer": user_answer,
                        "evaluation": evaluation
                    }
                )

                st.session_state.evaluation_done = True

    # ==================================
    # SHOW RESULT
    # ==================================

    if st.session_state.evaluation_done:

        result = st.session_state.results[-1]["evaluation"]

        st.success(
            "Answer Evaluated Successfully!"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Technical Score",
                result["technical_score"]
            )

        with col2:

            st.metric(
                "Communication Score",
                result["communication_score"]
            )

        with col3:

            st.metric(
                "Completeness Score",
                result["completeness_score"]
            )

        st.subheader("Strengths")

        for item in result["strengths"]:
            st.write(f"✅ {item}")

        st.subheader("Weaknesses")

        for item in result["weaknesses"]:
            st.write(f"❌ {item}")

        st.subheader("Improvement Tips")

        for item in result["improvement_tips"]:
            st.write(f"💡 {item}")

        st.subheader("Ideal Answer")

        st.write(
            result["ideal_answer"]
        )

        if st.button(
            "Next Question",
            use_container_width=True
        ):

            st.session_state.question_number += 1
            st.session_state.evaluation_done = False

            if (
                st.session_state.question_number
                > st.session_state.num_questions
            ):

                st.switch_page(
                    "pages/report.py"
                )

            else:

                st.session_state.current_question = generate_question(
                    st.session_state.domain,
                    st.session_state.difficulty
                )

                st.session_state.answer_box = ""

                st.rerun()

# ==================================
# REVIEW MY INTERVIEW MODE
# ==================================

elif mode == "Review My Interview":

    st.header(
        "📝 Review My Interview"
    )

    question = st.text_area(
        "Interview Question"
    )

    answer = st.text_area(
        "Your Answer"
    )

    if st.button(
        "Analyze Answer",
        use_container_width=True
    ):

        if question and answer:

            with st.spinner(
                "Analyzing Answer..."
            ):

                result = review_answer(
                    question,
                    answer
                )

            st.success(
                "Analysis Completed"
            )

            st.markdown(result)

        else:

            st.error(
                "Please enter both question and answer."
            )

# ==================================
# LEARN INTERVIEW QUESTIONS MODE
# ==================================

elif mode == "Learn Interview Questions":

    st.header(
        "📚 Learn Interview Questions"
    )

    topic = st.text_input(
        "Enter Any Topic"
    )

    if st.button(
        "Explain",
        use_container_width=True
    ):

        if topic:

            with st.spinner(
                "Generating Explanation..."
            ):

                result = explain_topic(
                    topic
                )

            st.markdown(result)

        else:

            st.error(
                "Please enter a topic."
            )



