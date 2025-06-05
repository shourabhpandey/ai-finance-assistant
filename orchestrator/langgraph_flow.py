from agents.ingestion_agent import run_ingestion
from agents.anomaly_agent import run_anomaly_detection
from agents.summary_agent import run_summary
from agents.advisor_agent import run_advice

def run_all_agents(df):
    results = {}
    transactions = run_ingestion(df)
    results["Parsed Transactions"] = f"{len(transactions)} transactions categorized."

    anomalies = run_anomaly_detection(transactions)
    results["Anomaly Detection"] = anomalies

    summary = run_summary(transactions)
    results["Monthly Summary"] = summary

    advice = run_advice(transactions)
    results["Advice"] = advice

    return results
