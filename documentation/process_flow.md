# Process Flow

## As-is (illustrative)
Transaction received → Analyst checks available details manually → Analyst decides review order → Case notes created → Team lead monitors workload separately.

## To-be prototype
CSV transaction feed
    ↓
Input schema validation
    ↓
Rule-based risk scoring
    ↓
Priority band + reason codes
    ↓
Prioritised investigation queue
    ↓
Investigator reviews supporting context
    ↓
Human disposition / escalation

## Business analysis notes
- The prototype supports prioritisation, not automated blocking.
- A flagged transaction may be legitimate (false positive).
- In a production design, investigator disposition should be captured with timestamp, user ID, reason and audit history.
