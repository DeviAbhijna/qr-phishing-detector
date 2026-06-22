import requests

API_KEY = "ad4cd3112aa240de168fa3fd1a1c2ae994ba2dddaaf83c995f90ecaec3a566e2"


def check_reputation(url):

    if API_KEY == "" or API_KEY == "PASTE_YOUR_API_KEY_HERE":
        return "API Key Not Added"

    headers = {
        "x-apikey": API_KEY
    }

    try:

        response = requests.post(
            "https://www.virustotal.com/api/v3/urls",
            headers=headers,
            data={"url": url}
        )

        if response.status_code != 200:
            return "Unable to analyze URL"

        analysis_id = response.json()["data"]["id"]

        report = requests.get(
            f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
            headers=headers
        )

        stats = report.json()["data"]["attributes"]["stats"]

        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)

        if malicious > 0:
            return f"Malicious ({malicious} detections)"

        elif suspicious > 0:
            return f"Suspicious ({suspicious} detections)"

        else:
            return "Safe"

    except Exception as e:
        print("VirusTotal Error:", e)
        return "Error Checking Reputation"