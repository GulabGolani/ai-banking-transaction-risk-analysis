# Business Requirements Document (BRD)

## 1. Project overview
**Name:** AI-Assisted Banking Transaction Risk Analysis System  
**Domain:** Retail banking / FinTech operations  
**Type:** Portfolio prototype using synthetic data

## 2. Business problem
Operations investigators need to prioritise unusual transactions consistently. A manual, unstructured review process can lead to inconsistent prioritisation and inefficient use of investigation capacity.

## 3. Business objective
Create a prototype that applies transparent risk indicators to transaction records, groups cases by priority, and provides concise evidence summaries for human review.

## 4. Stakeholders
- Fraud Operations Analyst: reviews flagged transactions.
- Operations Team Lead: monitors volumes and priority distribution.
- Business Analyst: gathers requirements, defines rules and validates outcomes.
- Data / Engineering Team: implements data processing and reporting.
- Risk / Compliance: reviews policy, governance and escalation requirements.

## 5. Scope
**In scope**
- Read a standard transaction CSV.
- Calculate illustrative risk scores.
- Assign Low / Medium / High priority.
- Produce a prioritised case file and summary metrics.
- Define SQL reporting queries and UAT scenarios.

**Out of scope**
- Real-time payment blocking.
- Production banking integration.
- Confirming fraud or making customer-impacting decisions.
- Training a production ML model.
- Regulatory or compliance certification.

## 6. Business requirements
| ID | Requirement | Priority |
|---|---|---|
| BR-01 | System shall ingest transaction records with required fields. | Must |
| BR-02 | System shall calculate a transparent risk score using approved prototype rules. | Must |
| BR-03 | System shall assign a priority band based on score thresholds. | Must |
| BR-04 | System shall provide the signals contributing to each score. | Must |
| BR-05 | System shall produce summary metrics by channel, city and priority. | Should |
| BR-06 | System shall retain human investigator review as the final decision point. | Must |

## 7. Assumptions and dependencies
- Input data is synthetic and has the expected schema.
- Thresholds are illustrative and require validation by risk stakeholders.
- Production use would require secure data handling, access controls, audit logging, model/rule governance and formal approval.

## 8. Success measures for the prototype
- All valid input rows are processed.
- Each output row contains a score, priority and reason codes.
- Summary metrics reconcile to the input row count.
- UAT cases pass for boundary values and missing data.
