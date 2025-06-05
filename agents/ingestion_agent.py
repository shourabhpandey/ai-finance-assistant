import pandas as pd

def run_ingestion(df: pd.DataFrame):
    # Example: Basic normalization & tagging
    df["amount"] = df["amount"].astype(float)
    df["category"] = df["description"].apply(lambda x: "food" if "restaurant" in x.lower() else "misc")
    return df.to_dict(orient="records")
