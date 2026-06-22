from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
    url,
    score,
    reputation,
    result,
    ml_prediction
):

    pdf_file = "security_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "QR Code Phishing Detection Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(f"URL: {url}", styles["BodyText"])
    )

    content.append(
        Paragraph(f"Risk Score: {score}", styles["BodyText"])
    )

    content.append(
        Paragraph(
            f"ML Prediction: {ml_prediction}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Domain Reputation: {reputation}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Final Verdict: {result}",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_file