# Power BI Dashboard Specification

## Page 1 — Risk Operations Overview
KPI cards:
- Total Transactions = count of transaction_id
- Risk-Flagged Transactions = count where priority is Medium or High
- High-Priority Cases = count where priority is High
- High-Priority Value = sum(amount_inr) where priority is High

Visuals:
- Column chart: transaction count by priority
- Bar chart: risk-flagged count by channel
- Bar chart: high-priority amount by city
- Line chart: transaction count by transaction date
- Slicers: date, city, channel, priority

## Page 2 — Investigation Queue
Table columns:
transaction_id, customer_id, transaction_date, amount_inr, channel, city, risk_score, priority, risk_reasons

## Data model
One fact table: transaction_risk (one row per transaction).
Use transaction_date as the date field; create a calendar table in Power BI for time intelligence.

## Governance note
Label metrics as "risk flagged" / "priority cases", not confirmed fraud. Do not present simulated results as real operational savings or fraud capture.
