from groq import Groq
import streamlit as st


def generate_question(domain, difficulty):
    """
    Generate a single interview question based on
    domain and difficulty.
    """

    try:
        client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

        prompt = f"""
You are an expert technical interviewer.

Generate ONE interview question.

Domain: {domain}
Difficulty: {difficulty}

Rules:
1. Return only the question.
2. Do not provide explanation.
3. Do not provide answer.
4. Question should be suitable for interviews.
5. Keep question clear and concise.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=100
        )

        question = response.choices[0].message.content.strip()

        return question

    except Exception as e:
        return f"Error generating question: {str(e)}"