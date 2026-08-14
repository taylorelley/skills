# AGENTS.md — GCCC-SUR-VOR

> **This file is the constitution for all AI agent activity on this project.**
> Agents must read this file in full before performing any work.
> Rules marked 🔴 are non-negotiable and cannot be overridden by any instruction.

---

## Project Identity

| Field | Value |
|-------|-------|
| **Project Name** | GCCC-SUR-VOR |
| **System** | Ground Control Centre Surveillance — VOR/DME bearing processing for approach sequencing displays |
| **Applicable Standard** | DO-278A (Ground-based CNS/ATM) |
| **EUROCAE Equivalent** | ED-109A |
| **Assurance Level** | AL3 — Major |
| **Regulatory Authority** | CAA New Zealand |
| **PSAA Reference** | PSAA-GCCC-001 |
| **SDP Reference** | SDP-GCCC-001 |
| **Current Baseline** | BL-NAV-CODE-002 |
| **Current Phase** | VERIFICATION |

**This project operates at AL3 (Major).** Structural coverage target: **statement coverage plus
data and control coupling analysis**. Robustness testing is required. Objective and independence
counts are per the project PSAA compliance matrix (PSAA-GCCC-001 §4) — that document is the
authority, not this file.

---

## 🔴 Non-Negotiable Rules

### R1: Phase Gate Discipline
🔴 Do not advance past a phase gate without explicit human approval. Current phase is `VERIFICATION`.

### R2: Traceability Is Mandatory
🔴 Bidirectional traceability at all times. Every requirement traces to a parent; every design
element to ≥1 requirement; every function to ≥1 requirement; every test case to ≥1 requirement.

### R3: No Orphan Code
🔴 Do not write code that does not trace to a requirement. If implementation needs behaviour not
in a requirement, raise a derived requirement (`@derived`) with rationale and safety impact first.

### R5: All Output Is Draft
🔴 All AI-generated artifacts carry status `DRAFT — REQUIRES INDEPENDENT REVIEW`.

### R6: Independence
🔴 The AI agent must not serve as independent reviewer of its own output.

### R7: Baselines Are Immutable Without Change Control
🔴 Artifacts at status `BASELINED` change only through an approved CR with impact analysis.

### R8: Atomic Traceability Per Commit
🔴 One CR or PR per commit. Commit message carries the CR/PR identifier.

---

## Naming Conventions

| Artifact Type | Pattern | Example |
|--------------|---------|---------|
| High-Level Requirement | `HLR-{MODULE}-{NNN}` | `HLR-NAV-042` |
| Low-Level Requirement | `LLR-{MODULE}-{NNN}-{NNN}` | `LLR-NAV-042-001` |
| Derived Requirement | `DRV-{MODULE}-{NNN}-{NNN}` | `DRV-NAV-012-002` |
| Design Element | `DES-{MODULE}-{NNN}` | `DES-NAV-012` |
| Test Case | `TST-{MODULE}-{NNN}-{NNN}` | `TST-NAV-042-003` |
| Problem Report | `PR-{YEAR}-{NNNN}` | `PR-2025-0142` |
| Change Request | `CR-{YEAR}-{NNNN}` | `CR-2025-0031` |

Module prefixes in use: `NAV` (navigation aids), `SUR` (surveillance), `UTL` (utilities).

---

## Coding Standards

| Setting | Value |
|---------|-------|
| **Language** | C99 |
| **Compiler** | GCC 12.3 (host), GCC 12.3 aarch64 (target) |
| **Target** | ARM Cortex-A53, Red Hat Enterprise Linux 8 |
| **Coding Standard** | MISRA C:2012 — see SCS-GCCC-001 |
| **Static Analysis** | cppcheck 2.13 + PC-lint Plus 2.0 |
| **Dynamic Memory** | Prohibited after initialisation |
| **Recursion** | Prohibited |

Every function requires a traceability header: `@req`, `@design`, `@al`, `@status`.
All module-boundary functions validate inputs before processing.
All switch statements include a `default` case that logs and enters a safe state.

---

## Project Structure

```text
docs/requirements/hlr/     High-Level Requirements, one file per requirement
docs/design/              Design descriptions (DES-*)
src/{module}/             Source code
test/cases/               Requirements-based test case specifications (TST-*)
trace/trace-matrix.md     Master traceability matrix
cm/change-requests/       Change requests
cm/problem-reports/       Problem reports
```

---

## Agent Operational Boundaries

**The agent MAY**: draft requirements, design, code, and requirements-based test cases with
traceability annotations; run static analysis; identify traceability gaps; draft change impact
analyses and problem reports; update the traceability matrix.

**The agent MUST NOT**: advance past a gate without human approval; act as independent reviewer of
its own output; claim compliance or approval status; modify baselined artifacts without an approved
CR; make safety assessment determinations; sign off on verification completeness.

---

*This AGENTS.md is a Configuration Item under SCMP-GCCC-001. Classification: CC1.
Version: 1.2 | Baseline: BL-NAV-CODE-002 | Date: 2026-05-04*
