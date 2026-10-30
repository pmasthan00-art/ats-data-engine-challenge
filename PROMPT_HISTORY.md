# AI Collaboration Record & Prompt History Directory

In strict alignment with **Guideline 03 (Use LLMs Transparently)** of the candidate project guidelines, this tracking log registers the programmatic prompts, conversational refinements, and human code corrections utilized during development.

## 1. LLM Assistance Scope & Acceleration Metrics
* **Scaffold Generation:** AI tools accelerated development by automatically structuring boilerplate Pandas dictionary builders, data row counting loops, and relational foreign key lists.
* **Document Compilation:** Assisted in organizing markdown layout tables and converting technical system specs into cleanly grouped definitions within `DATA_DICTIONARY.md`.
* **Human Engineering Auditing:** Every mathematical range, index increment, array state, file path handler, and data type transformation was hand-verified and checked locally via Windows execution shells to confirm zero structural defects.

## 2. Interactive Prompt History Registries

### Prompt Sequence 01: Core Architecture Definition
> **User Command Context:**
> "Build an end-to-end synthetic data generation pipeline simulating an enterprise ATS workflow across 12 relational models. Generate exactly 100 requisitions, 2,000 candidates, 3,000 applications, 600 interviews, and 150 offers. Enforce strict padded identity patterns like REQ-2026-000001. System must run deterministically via seed managers and match hashes over multiple executions. Inject 5 distinct exception routes (salary boundaries anomalies, duplicated pairs, blocked timelines) and track them inside an isolated ground_truth logging framework."

### Prompt Sequence 02: Relational Exception Rectification
> **User Command Context:**
> "The post-processing anomaly method throws a runtime error because pandas `.iloc` calls are trying to search column names via string lookups instead of utilizing standard numeric indices. Fix the dictionary mutation statements to index elements using valid syntax layout parameters."

### Prompt Sequence 03: Pathing Realignment
> **User Command Context:**
> "Refactor the file generation export paths at the bottom of the main execution block. Instead of isolating datasets within subfolders, configure the file writer to output all 12 compiled `.csv` documents directly onto the primary workspace root directory next to generator.py."
