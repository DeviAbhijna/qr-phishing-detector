import re
import validators


def has_ip(url):
    pattern = r"http[s]?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    return re.search(pattern, url) is not None


def check_url(url):

    score = 0
    reasons = []

    # Invalid URL
    if not validators.url(url):
        return 10, ["Invalid URL"]

    # HTTP instead of HTTPS
    if url.startswith("http://"):
        score += 2
        reasons.append("Uses HTTP instead of HTTPS")

    # Suspicious keywords
    keywords = ["login", "verify", "bank", "secure", "update"]

    for word in keywords:
        if word in url.lower():
            score += 2
            reasons.append(
                f"Contains suspicious keyword: {word}"
            )

    # Brand impersonation detection
    brands = [
        "google",
        "amazon",
        "paypal",
        "microsoft",
        "facebook",
        "instagram",
        "netflix",
        "apple"
    ]

    for brand in brands:
        if brand in url.lower():

            official_domains = [
                f"{brand}.com",
                f"www.{brand}.com"
            ]

            if not any(domain in url.lower() for domain in official_domains):
                score += 3
                reasons.append(
                    f"Possible brand impersonation: {brand}"
                )

    # Long URL
    if len(url) > 70:
        score += 1
        reasons.append("Very long URL")

    # @ symbol
    if "@" in url:
        score += 2
        reasons.append("Contains @ symbol")

    # IP address usage
    if has_ip(url):
        score += 3
        reasons.append(
            "Uses IP address instead of domain name"
        )

    return score, reasons