def risk_agent(scam_indicators, financial_risks):
    """
    Combines scam and financial indicators
    to determine an overall risk level.
    """

    total_signals = len(scam_indicators) + len(financial_risks)

    if total_signals >= 5:
        risk_level = "HIGH"
    elif total_signals >= 2:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_level": risk_level,
        "total_signals": total_signals,
        "scam_indicators": scam_indicators,
        "financial_risks": financial_risks
    }