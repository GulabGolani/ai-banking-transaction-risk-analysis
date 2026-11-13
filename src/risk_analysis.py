from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "sample_transactions.csv"
OUT = ROOT / "outputs"

REQUIRED = {
    "transaction_id", "customer_id", "transaction_date", "amount_inr",
    "channel", "city", "transaction_hour", "customer_tenure_days"
}

def assess_risk(df: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    result = df.copy()
    result["risk_score"] = 0
    result["risk_reasons"] = ""

    rules = [
        (result["amount_inr"] >= 50000, 40, "High amount (>= INR 50,000)"),
        (result["transaction_hour"].between(0, 4), 25, "Overnight transaction (00:00–04:59)"),
        (result["customer_tenure_days"] < 30, 20, "New customer (<30 days)"),
        (result["channel"].isin(["UPI", "Wallet"]), 10, "UPI / Wallet channel"),
    ]
    reason_lists = [[] for _ in range(len(result))]
    for mask, points, reason in rules:
        result.loc[mask, "risk_score"] += points
        for idx in result.index[mask]:
            reason_lists[result.index.get_loc(idx)].append(reason)

    result["risk_reasons"] = ["; ".join(items) if items else "No configured risk indicators" for items in reason_lists]
    result["priority"] = pd.cut(
        result["risk_score"],
        bins=[-1, 29, 59, 10_000],
        labels=["Low", "Medium", "High"]
    ).astype(str)
    return result.sort_values(["risk_score", "amount_inr"], ascending=[False, False])

def main():
    OUT.mkdir(exist_ok=True)
    raw = pd.read_csv(INPUT)
    assessed = assess_risk(raw)
    assessed.to_csv(OUT / "prioritised_transactions.csv", index=False)

    summary = (assessed.groupby("priority", observed=False)
               .agg(transaction_count=("transaction_id", "count"),
                    total_value_inr=("amount_inr", "sum"))
               .reset_index())
    summary["total_value_inr"] = summary["total_value_inr"].round(2)
    summary.to_csv(OUT / "priority_summary.csv", index=False)

    flagged = assessed[assessed["priority"].isin(["Medium", "High"])]
    print(f"Processed transactions: {len(assessed):,}")
    print(f"Risk-flagged transactions (Medium + High): {len(flagged):,}")
    print(f"High-priority cases: {(assessed['priority'] == 'High').sum():,}")
    print(f"Outputs saved to: {OUT}")

if __name__ == "__main__":
    main()
