import streamlit as st
import pandas as pd
from orchestrator.langgraph_flow import run_all_agents
import io

st.title("AI-Powered Personal Finance Assistant")

uploaded_file = st.file_uploader("Upload a CSV of your transactions", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Transactions")
    st.dataframe(df)

    st.subheader("AI Insights")
    try:
        insights = run_all_agents(df)

        st.markdown(f"**Parsed Transactions:** {insights['Parsed Transactions']}")
        st.markdown(f"**Anomaly Detection:** {insights['Anomaly Detection']}")
        st.markdown(f"**Monthly Summary:** {insights['Monthly Summary']}")
        st.markdown("### Financial Advice")

        # Format advice into Markdown-friendly output
        formatted_advice = "\n\n".join([
            f"**{section.strip()}**" if i == 0 or section.endswith(":") else section.strip()
            for i, section in enumerate(insights['Advice'].split("\n\n"))
        ])
        st.markdown(formatted_advice, unsafe_allow_html=True)

        # Prepare text for download
        insight_text = f"""Parsed Transactions: {insights['Parsed Transactions']}
Anomaly Detection: {insights['Anomaly Detection']}
Monthly Summary: {insights['Monthly Summary']}

Advice:
{insights['Advice']}
"""

        st.download_button(
            label="Download Insights as .txt",
            data=insight_text,
            file_name="financial_insights.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error running agents: {e}")

# import streamlit as st
# import pandas as pd
# from orchestrator.langgraph_flow import run_all_agents
# from fpdf import FPDF
# import io

# st.set_page_config(page_title="AI Personal Finance Assistant", layout="centered")
# st.title("AI-Powered Personal Finance Assistant")

# st.markdown("Upload your bank statement (CSV) to get insights on spending, risks, and financial advice.")

# uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.markdown("---")
#     st.subheader("📄 Transaction Preview")
#     st.dataframe(df, use_container_width=True)

#     st.markdown("---")
#     st.subheader("🔍 AI Insights")

#     try:
#         insights = run_all_agents(df)

#         col1, col2 = st.columns(2)
#         with col1:
#             st.metric(label="Parsed Transactions", value=insights["Parsed Transactions"])
#         with col2:
#             st.metric(label="High-Value Flags", value=insights["Anomaly Detection"])

#         st.markdown("### Monthly Summary")
#         st.success(insights["Monthly Summary"])

#         st.markdown("### Financial Advice")
#         st.markdown(insights["Advice"], unsafe_allow_html=True)

#         # Prepare full text for download
#         full_text = f"""Parsed Transactions: {insights['Parsed Transactions']}
# Anomaly Detection: {insights['Anomaly Detection']}
# Monthly Summary: {insights['Monthly Summary']}
# Financial Advice:\n{insights['Advice']}"""

#         st.markdown("---")
#         st.subheader("📥 Download Insights")

#         # TXT Download
#         st.download_button(
#             label="Download as Text File",
#             data=full_text,
#             file_name="financial_insights.txt",
#             mime="text/plain"
#         )

#         # PDF Download
#         class PDF(FPDF):
#             def header(self):
#                 self.set_font("Arial", "B", 14)
#                 self.cell(0, 10, "AI Financial Insights", ln=True, align="C")
#                 self.ln(10)

#             def chapter(self, title, body):
#                 self.set_font("Arial", "B", 12)
#                 self.cell(0, 10, title, ln=True)
#                 self.set_font("Arial", "", 11)
#                 self.multi_cell(0, 8, body)
#                 self.ln()

#         pdf = PDF()
#         pdf.add_page()
#         pdf.chapter("Parsed Transactions", insights["Parsed Transactions"])
#         pdf.chapter("Anomaly Detection", insights["Anomaly Detection"])
#         pdf.chapter("Monthly Summary", insights["Monthly Summary"])
#         pdf.chapter("Financial Advice", insights["Advice"])

#         pdf_output = io.BytesIO()
#         pdf.output(pdf_output)
#         pdf_output.seek(0)

#         st.download_button(
#             label="Download as PDF",
#             data=pdf_output,
#             file_name="financial_insights.pdf",
#             mime="application/pdf"
#         )

#     except Exception as e:
#         st.error(f"❌ Error running agents: {e}")
