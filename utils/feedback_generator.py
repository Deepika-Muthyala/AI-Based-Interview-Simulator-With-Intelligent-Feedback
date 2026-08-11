def generate_feedback(evaluation):
    """
    Extract feedback information from
    evaluation result.
    """

    return {
        "strengths": evaluation.get("strengths", []),
        "weaknesses": evaluation.get("weaknesses", []),
        "improvement_tips": evaluation.get("improvement_tips", []),
        "ideal_answer": evaluation.get("ideal_answer", "")
    }