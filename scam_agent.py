def scam_agent(message):
    """
    Detects common financial scam indicators.
    """

    text = message.lower()

    indicators = []

    scam_patterns = {
        "otp": "Requests OTP",
        "pin": "Requests PIN",
        "password": "Requests password",
        "click": "Asks the user to click a link",
        "urgent": "Uses urgent language",
        "immediately": "Uses urgent language",
        "account blocked": "Threatens account blocking",
        "account will be blocked": "Threatens account blocking",
        "kyc": "Mentions KYC verification",
        "upi": "Mentions UPI/payment",
        "cashback": "Uses cashback/reward claim",
        "prize": "Uses prize/reward claim",
        "winner": "Claims the user is a winner"
    }

    for keyword, reason in scam_patterns.items():
        if keyword in text:
            indicators.append(reason)

    # Remove duplicate indicators
    indicators = list(set(indicators))

    return indicators