from groq import Groq
import streamlit as st
import json


def evaluate_answer(question, answer):
    """
    Evaluate candidate answer and return
    scores, strengths, weaknesses,
    improvement tips and ideal answer.
    """

    try:
        client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

        prompt = f"""
You are an expert technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and return ONLY valid JSON.

Format:

{{
    "technical_score": 0,
    "communication_score": 0,
    "completeness_score": 0,
    "strengths": [
        ""
    ],
    "weaknesses": [
        ""
    ],
    "improvement_tips": [
        ""
    ],
    "ideal_answer": ""
}}

Scoring Rules:
- technical_score: 0-25
- communication_score: 0-25
- completeness_score: 0-25

Do not return anything except JSON.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=700
        )

        result = response.choices[0].message.content.strip()

        # Remove markdown if model returns ```json
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

        evaluation = json.loads(result)

        return evaluation

    except Exception as e:

        return {
            "technical_score": 0,
            "communication_score": 0,
            "completeness_score": 0,
            "strengths": [],
            "weaknesses": [f"Error: {str(e)}"],
            "improvement_tips": [],
            "ideal_answer": ""
        }