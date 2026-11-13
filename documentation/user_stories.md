# User Stories and Acceptance Criteria

## US-01 — Ingest transaction data
**As an** operations analyst, **I want** transaction data loaded from a standard CSV, **so that** I can analyse a consistent dataset.

Acceptance criteria:
- Given a CSV with all required columns, when the analysis runs, then every valid row is processed.
- Given a missing required column, when the analysis runs, then a clear validation error is shown.

## US-02 — Prioritise unusual transactions
**As an** investigator, **I want** transactions assigned a transparent risk score, **so that** I can focus review effort.

Acceptance criteria:
- Amount >= ₹50,000 contributes 40 points.
- Transaction hour 00:00–04:59 contributes 25 points.
- Customer tenure < 30 days contributes 20 points.
- UPI or Wallet contributes 10 points.
- The output displays each triggered reason.

## US-03 — Review priority queue
**As an** investigator, **I want** high-priority cases listed first, **so that** I can review the strongest indicators first.

Acceptance criteria:
- High priority is score >= 60.
- Medium priority is score >= 30 and < 60.
- Low priority is score < 30.
- Sorting is descending by score.

## US-04 — Monitor operational trends
**As a** team lead, **I want** counts and amounts by priority, channel and city, **so that** I can monitor workload patterns.

Acceptance criteria:
- Summary counts reconcile with the source transaction count.
- Dashboard specification defines total volume, flagged volume, high-priority count and channel breakdown.

## US-05 — Human review and auditability
**As a** risk operations lead, **I want** risk indicators and a human review step, **so that** automated flags are not treated as final fraud decisions.

Acceptance criteria:
- Output uses the term "risk flag" and not "confirmed fraud".
- Each case contains reason codes.
- Final disposition is left to an authorised human reviewer.
