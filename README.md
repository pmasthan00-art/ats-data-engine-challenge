# Corporate ATS Relational Data Engine & Workflow Simulator

This framework implements an automated transaction generator that models an end-to-end Applicant Tracking System (ATS) pipeline under production-ready constraint logic.

## 1. Local Configuration & Executable Instructions
The environment runs on native Python standard libraries without requiring complex configuration layers or secondary database dependencies.

### Step A: Verify Dependencies
Ensure Python 3.8+ is mapped onto your shell parameters alongside data science libraries:
```bash
python -m pip install pandas numpy
```

### Step B: Trigger the Generation Pipeline
Execute the main compiler loop file directly from your terminal interface workspace root:
```bash
python generator.py
```
Upon execution, the script runs an automated validation suite, conducts parallel hashing verification tests to ensure parity, and saves all 12 compliant seed tables directly into the root folder.

---

## 2. Testing Methodology & Verification Controls
To guarantee that final deliverables fulfill the strict acceptance metrics, the architecture maintains automated constraint check functions:
* **Primary Key Uniqueness Validation:** Enforces structural data uniqueness thresholds checking `requisition_id`, `candidate_id`, and `application_id`.
* **Referential Database Integrity Checks:** Dynamically maps cross-table constraints verifying that every row inside transactional schemas references fully valid parent IDs inside base lookup tables.
* **Algorithmic Parity Validation:** Triggers parallel multi-run executions checking SHA-256 signatures to certify that output logs match perfectly.

---

## 3. Project Constraints, Trade-offs, & Strategic Limitations
* **Strategic Limitation (Volatile Memory Execution):** Data records are constructed inside memory arrays using Pandas frames to maximize execution metrics before streaming to storage. For datasets scaling above 10M rows, an explicit chunking database stream layer would be required.
* **Design Decision (Decoupled Anomaly Boundaries):** Real-world edge cases (salary cap errors, scheduling collisions, duplicated files) are isolated cleanly into a dedicated `ground_truth.csv` dataset, preventing core analytics algorithms from tracking bad features.