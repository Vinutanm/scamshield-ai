def financial_agent(message):
    """
    Identifies financial-risk signals in a message.
    """

    text = message.lower()

    risks = []

    financial_patterns = {
        "otp": "Possible attempt to obtain a one-time password",
        "pin": "Possible attempt to obtain a banking PIN",
        "upi": "Contains a UPI/payment request",
        "send money": "Requests a money transfer",
        "transfer": "Mentions a financial transfer",
        "pay": "Requests payment",
        "payment": "Requests payment",
        "bank": "Impersonates or references a bank",
        "account": "References a financial account",
        "refund": "Uses a refund-related claim",
        "cashback": "Uses a cashback-related claim",
        "loan": "Contains a loan-related request",
    }

    for keyword, reason in financial_patterns.items():
        if keyword in text:
            risks.append(reason)

    return list(set(risks))