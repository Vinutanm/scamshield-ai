import streamlit as st

from agents.language_agent import language_agent
from agents.scam_agent import scam_agent
from agents.financial_agent import financial_agent
from agents.risk_agent import risk_agent


st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️"
)

st.title("🛡️ ScamShield AI")
st.subheader("Vernacular Financial Fraud Detection")

st.write(
    "Analyze suspicious financial messages using multiple "
    "specialized detection agents."
)

language = st.selectbox(
    "🌐 Preferred response language",
    ["English", "ಕನ್ನಡ", "हिन्दी"]
)

message = st.text_area(
    "📩 Paste suspicious financial message",
    placeholder="Example: Your bank KYC has expired. Click this link and enter your OTP..."
)

if st.button("🔍 Analyze Message"):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        # Agent 1: Language Detection
        detected_language = language_agent(message)

        # Agent 2: Scam Detection
        scam_indicators = scam_agent(message)

        # Agent 3: Financial Risk Detection
        financial_risks = financial_agent(message)

        # Agent 4: Overall Risk Assessment
        result = risk_agent(
            scam_indicators,
            financial_risks
        )

        st.divider()

        st.subheader("🤖 Agent Analysis")

        st.write(
            f"🌐 **Detected Language:** {detected_language}"
        )

        st.write(
            f"🕵️ **Scam Agent:** "
            f"{len(scam_indicators)} indicators detected"
        )

        st.write(
            f"💰 **Financial Agent:** "
            f"{len(financial_risks)} financial risks detected"
        )

        st.write(
            f"🧠 **Risk Agent:** "
            f"{result['total_signals']} total signals analyzed"
        )

        st.divider()

        # Final result
        if result["risk_level"] == "HIGH":
            st.error("🔴 HIGH RISK")
        elif result["risk_level"] == "MEDIUM":
            st.warning("🟠 MEDIUM RISK")
        else:
            st.success("🟢 LOW RISK")

        if scam_indicators:
            st.subheader("🚨 Suspicious Indicators")

            for indicator in scam_indicators:
                st.write("⚠️", indicator)

        if financial_risks:
            st.subheader("💰 Financial Risk Signals")

            for risk in financial_risks:
                st.write("⚠️", risk)

        st.subheader("🛡️ Recommended Action")

        if result["risk_level"] == "HIGH":
            st.write("❌ Do not click suspicious links.")
            st.write("❌ Do not share OTP, PIN or passwords.")
            st.write("❌ Do not transfer money.")
            st.write("✅ Verify the message through the official bank/service.")

        elif result["risk_level"] == "MEDIUM":
            st.write("⚠️ Be cautious before taking any action.")
            st.write("✅ Verify the sender through an official channel.")

        else:
            st.write("✅ No major scam indicators were detected.")
            st.write("⚠️ This does not guarantee that the message is safe.")