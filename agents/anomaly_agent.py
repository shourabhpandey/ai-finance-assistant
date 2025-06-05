def run_anomaly_detection(transactions):
    large_txns = [t for t in transactions if abs(t["amount"]) > 10000]
    if not large_txns:
        return "No unusual transactions found."
    return f"Flagged {len(large_txns)} high-value transactions."
