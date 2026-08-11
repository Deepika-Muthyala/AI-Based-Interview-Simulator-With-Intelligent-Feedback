def calculate_scores(results):
    """
    Calculate overall interview scores.
    """

    technical_total = 0
    communication_total = 0
    completeness_total = 0

    for item in results:

        evaluation = item["evaluation"]

        technical_total += evaluation.get(
            "technical_score",
            0
        )

        communication_total += evaluation.get(
            "communication_score",
            0
        )

        completeness_total += evaluation.get(
            "completeness_score",
            0
        )

    total_score = (
        technical_total
        + communication_total
        + completeness_total
    )

    max_score = len(results) * 75

    percentage = 0

    if max_score > 0:
        percentage = round(
            (total_score / max_score) * 100,
            2
        )

    # Grade Calculation
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

    return {
        "technical_total": technical_total,
        "communication_total": communication_total,
        "completeness_total": completeness_total,
        "total_score": total_score,
        "max_score": max_score,
        "percentage": percentage,
        "grade": grade
    }