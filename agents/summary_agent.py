import pandas as pd
from collections import defaultdict

def run_summary(transactions):
    df = pd.DataFrame(transactions)
    
    if "date" not in df.columns:
        return "Missing 'date' column in data."

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])  # Remove rows with invalid dates
    df['month'] = df['date'].dt.to_period('M')

    summary_lines = []
    monthly_totals = defaultdict(float)

    for month, group in df.groupby('month'):
        total = group[group["amount"] < 0]["amount"].sum()
        monthly_totals[str(month)] = total
        summary_lines.append(f"{month}: ₹{abs(total):,.2f} spent")

    # Detect spending trend between last two months
    months = list(monthly_totals.keys())
    if len(months) >= 2:
        change = monthly_totals[months[-1]] - monthly_totals[months[-2]]
        if change < 0:
            trend = f"Spending decreased by ₹{abs(change):,.2f} from previous month."
        else:
            trend = f"Spending increased by ₹{abs(change):,.2f} from previous month."
        summary_lines.append(trend)

    return "\n".join(summary_lines)
