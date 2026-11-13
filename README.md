# AI-Assisted Banking Transaction Risk Analysis System

**Portfolio project | Business Analysis + SQL + Python + GenAI-ready workflow**

## Important
This is a portfolio prototype using **synthetic, simulated transaction data**. It is not connected to a real bank, does not establish actual fraud, and has not been deployed in a production environment. Risk flags are rule-based indicators for investigation, not fraud verdicts.

## Business problem
A bank's operations team needs a consistent way to prioritise transactions that may warrant manual review. Reviewing every transaction equally can waste investigator time and delay attention to unusual activity.

## Proposed solution
A lightweight workflow that:
1. Loads transaction records.
2. Applies transparent risk rules (large amount, unusual overnight hour, and short customer tenure).
3. Produces a risk score and Low / Medium / High priority.
4. Summarises flagged cases for an investigator.
5. Provides SQL queries and KPI definitions for operational reporting.

## Project structure
- `data/sample_transactions.csv` — 1,200 synthetic transactions.
- `sql/analysis_queries.sql` — SQL for KPIs, trends and high-risk cases.
- `src/risk_analysis.py` — runnable Python analysis and case-summary generator.
- `documentation/BRD.md` — business requirements.
- `documentation/user_stories.md` — user stories and acceptance criteria.
- `documentation/process_flow.md` — current/proposed process.
- `documentation/uat_test_cases.csv` — sample UAT scenarios.
- `dashboard/dashboard_spec.md` — Power BI page and KPI specification.

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python src/risk_analysis.py
```
Outputs are written to `outputs/` (created automatically).

## Risk logic
- Amount >= ₹50,000: +40 points
- Transaction hour between 00:00 and 04:59: +25 points
- Customer tenure < 30 days: +20 points
- Channel is UPI or Wallet: +10 points

Priority: High >= 60; Medium >= 30; otherwise Low. These are illustrative business rules, not a validated fraud model. Tune thresholds with domain experts and historical labelled data before real use.

## AI component: safe implementation boundary
This project includes an AI-ready investigation prompt template in `documentation/ai_investigation_prompt.md`. It instructs an LLM to explain only supplied signals, avoid declaring fraud, identify missing context, and recommend human review. The current runnable code generates a deterministic case summary; it does **not** call an external AI API.

## Suggested resume bullet (use only after running and reviewing it)
"Built a FinTech transaction-risk analysis prototype using Python and SQL on 1,200 synthetic banking transactions; defined transparent risk indicators, prioritisation bands, investigation summaries, KPI queries and UAT scenarios."

## Interview talking points
- Why risk flags are not fraud labels.
- How business rules were translated into measurable logic.
- How an operations analyst could use priority queues.
- What data and governance are needed before production deployment.
- How UAT validates both expected flags and false-positive handling.
