from groq import Groq
import streamlit as st

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def explain_topic(topic):

    prompt = f"""
    Explain the topic: {topic}

    Give:
    1. Definition
    2. Important Concepts
    3. Interview Questions
    4. Sample Answer
    5. Follow-up Questions
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

