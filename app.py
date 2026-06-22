from flask import Flask, render_template, request, send_file
import os
import pandas as pd

from qr_reader import read_qr
from url_checker import check_url
from reputation_checker import check_reputation
from scan_logger import log_scan
from report_generator import generate_report
from ml_model import predict_url
from dl_model import predict_dl

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    url = None
    reputation = None
    score = None
    reasons = []

    ml_prediction = None
    dl_prediction = None

    if request.method == "POST":

        manual_url = request.form.get("manual_url")

        # Manual URL
        if manual_url and manual_url.strip():

            url = manual_url.strip()

        # QR Upload
        elif "qrfile" in request.files and request.files["qrfile"].filename != "":

            file = request.files["qrfile"]

            filepath = os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )

            file.save(filepath)

            url = read_qr(filepath)

            print("Extracted URL:", url)

            if not url:
                result = "No QR Code Detected"

        else:
            result = "Please upload a QR image or enter a URL"

        # URL Analysis
        if url:

            score, reasons = check_url(url)

            # ML Prediction
            # ML Prediction (Display Only)

            try:

                ml_result = predict_url(url)

                if ml_result == 1:
                    ml_prediction = "Malicious"
                else:
                    ml_prediction = "Benign"

            except Exception:

                ml_prediction = "Not Available"

            # DL Prediction (Display Only)
            try:
                dl_prediction = predict_dl(url)
            except Exception:
                dl_prediction = "Not Available"

            print("URL:", url)
            print("Score:", score)
            print("Reasons:", reasons)
            print("ML:", ml_prediction)
            print("DL:", dl_prediction)

            # FINAL VERDICT
            # FINAL VERDICT (Rule-Based)

        if score is not None:

            if score >= 6:
                result = "Phishing Detected"

            elif score >= 3:
                result = "Suspicious"

            else:
                result = "Safe"

        else:
            result = "Safe"

            reputation = check_reputation(url)

            log_scan(url, result)

    return render_template(
        "index.html",
        result=result,
        url=url,
        reputation=reputation,
        score=score,
        reasons=reasons,
        ml_prediction=ml_prediction,
        dl_prediction=dl_prediction
    )


@app.route("/dashboard")
def dashboard():

    try:

        df = pd.read_csv(
            "scan_logs.csv",
            header=None,
            names=["timestamp", "url", "result"]
        )

        total = len(df)

        safe = len(
            df[df["result"] == "Safe"]
        )

        suspicious = len(
            df[df["result"] == "Suspicious"]
        )

        phishing = len(
            df[df["result"] == "Phishing Detected"]
        )

        scans = df.tail(10).values.tolist()[::-1]

    except Exception as e:

        print(e)

        total = 0
        safe = 0
        suspicious = 0
        phishing = 0
        scans = []

    return render_template(
        "dashboard.html",
        total=total,
        safe=safe,
        suspicious=suspicious,
        phishing=phishing,
        scans=scans
    )


@app.route("/download_report")
def download_report():

    pdf = generate_report(
        "Sample URL",
        10,
        "Safe",
        "Phishing Detected",
        "Malicious"
    )

    return send_file(
        pdf,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)