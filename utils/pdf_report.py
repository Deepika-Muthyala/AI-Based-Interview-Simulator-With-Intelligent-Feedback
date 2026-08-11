from fpdf import FPDF
import os


def generate_pdf_report(results, percentage, grade):
    """
    Generate interview report PDF.
    """

    os.makedirs("reports", exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "AI Interview Simulator Report", ln=True, align="C")

    pdf.ln(10)

    # Summary
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, f"Overall Percentage: {percentage}%", ln=True)

    pdf.cell(200, 10, f"Grade: {grade}", ln=True)

    pdf.ln(5)

    # Question-wise Details
    for i, item in enumerate(results, start=1):

        evaluation = item["evaluation"]

        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 8, f"Question {i}")

        pdf.set_font("Arial", "", 11)

        pdf.multi_cell(
            0,
            8,
            f"Question: {item['question']}"
        )

        pdf.multi_cell(
            0,
            8,
            f"Answer: {item['answer']}"
        )

        pdf.multi_cell(
            0,
            8,
            f"Technical Score: {evaluation['technical_score']}/25"
        )

        pdf.multi_cell(
            0,
            8,
            f"Communication Score: {evaluation['communication_score']}/25"
        )

        pdf.multi_cell(
            0,
            8,
            f"Completeness Score: {evaluation['completeness_score']}/25"
        )

        strengths = ", ".join(
            evaluation.get("strengths", [])
        )

        weaknesses = ", ".join(
            evaluation.get("weaknesses", [])
        )

        tips = ", ".join(
            evaluation.get("improvement_tips", [])
        )

        pdf.multi_cell(
            0,
            8,
            f"Strengths: {strengths}"
        )

        pdf.multi_cell(
            0,
            8,
            f"Weaknesses: {weaknesses}"
        )

        pdf.multi_cell(
            0,
            8,
            f"Improvement Tips: {tips}"
        )

        pdf.multi_cell(
            0,
            8,
            f"Ideal Answer: {evaluation['ideal_answer']}"
        )

        pdf.ln(5)

    file_path = "reports/interview_report.pdf"

    pdf.output(file_path)

    return file_path