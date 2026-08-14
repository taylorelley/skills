# Standards Reference — DO-178C / DO-278A

Reference detail behind the main skill. Read the section you need.

## Contents

1. [Standards & regulatory framework](#1-standards--regulatory-framework)
2. [Software lifecycle processes](#2-software-lifecycle-processes)
3. [Assurance levels and objective counts](#3-assurance-levels-and-objective-counts)
4. [Requirements engineering](#4-requirements-engineering)
5. [Design & architecture](#5-design--architecture)
6. [Verification & testing](#6-verification--testing)
7. [Structural coverage analysis](#7-structural-coverage-analysis)
8. [Traceability & the lifecycle data items](#8-traceability--the-lifecycle-data-items)
9. [Configuration management](#9-configuration-management)
10. [Tool qualification (DO-330)](#10-tool-qualification-do-330)
11. [COTS & service experience (DO-278A)](#11-cots--service-experience-do-278a)
12. [Ground-based CNS/ATM operations (DO-278A)](#12-ground-based-cnsatm-operations-do-278a)
13. [Terminology translation](#13-terminology-translation)

---

## 1. Standards & regulatory framework

DO-178C (airborne) and DO-278A (ground-based CNS/ATM) with their EUROCAE equivalents ED-12C and
ED-109A; the DO-178C supplements DO-330 (tool qualification), DO-331 (model-based), DO-332
(object-oriented), DO-333 (formal methods); and the system-level processes they sit under,
ARP4754A (development) and ARP4761 (safety assessment).

Regulatory recognition comes through FAA AC 20-115D and EASA AMC 20-115D. Other authorities
(CAA New Zealand, CASA Australia) determine which guidance material they accept — establish this
during planning, not at the first Stage of Involvement review.

The relationship that governs everything downstream: the **system** safety assessment determines
failure condition severity, which determines the software assurance level, which determines
which objectives apply and how many require independence. Software does not choose its own DAL.

## 2. Software lifecycle processes

Six processes: Planning, Development (requirements → design → coding → integration),
Verification, Configuration Management, Quality Assurance, and Certification/Approval Liaison.

The standards are lifecycle-model-agnostic — V-model, iterative, and incremental are all
acceptable, and Agile is explicitly workable provided gate discipline, continuous traceability,
defined baselines, and verification independence survive contact with the sprint cadence. What
the standards require is defined entry and exit criteria per phase, not a waterfall.

Verification runs concurrently with development but never ahead of it: you cannot verify an
artifact that does not exist yet.

## 3. Assurance levels and objective counts

DO-178C defines 5 DALs (A–E) across 10 Annex A tables. DO-278A defines 6 ALs (1–6), where AL4 is
an intermediate level with no DO-178C equivalent — it exists because ground-based systems often
sit between Major and Minor, and it is the usual target for COTS-heavy subsystems.

| DAL / AL | Failure condition | Approx. objectives | Approx. with independence |
|----------|-------------------|--------------------|---------------------------|
| A / AL1 | Catastrophic | 71 | ~30–33 |
| B / AL2 | Hazardous / Severe-Major | 69 | ~18–21 |
| C / AL3 | Major | 62 | ~5–8 |
| AL4 (DO-278A only) | Between Major and Minor | tailored, ~40–50 | ~6 |
| D / AL5 | Minor | 26 | ~2–5 |
| E / AL6 | No safety effect | 0 | 0 |

> **Treat these as planning aids for scoping effort, never as compliance data.** Published
> secondary sources disagree on the independence counts in particular, and the objective totals
> shift between DO-178B and DO-178C. Before any of these numbers reach a PSAC, an SOI package, or
> a compliance matrix, confirm them against the project's own copy of the Annex A tables. An
> authority holds you to the standard, not to a table you found in a tool.

The steepest cost cliff in the standard is DAL D → DAL C: 26 objectives to 62. Plan for it during
system safety assessment, when the allocation is still negotiable, rather than discovering it
during verification.

## 4. Requirements engineering

High-Level Requirements decompose from allocated system requirements. Low-Level Requirements
refine HLRs to the point where code can be written directly from them. Derived requirements are
those introduced by the software process itself, traceable to no parent — they matter
disproportionately because the system safety assessment never saw them, so they must be fed back
to that process for review.

Every requirement needs: a unique ID, a single atomic testable "shall" statement, unambiguity
(one possible reading), verifiability by test/review/analysis, an explicit parent trace,
completeness (all conditions, tolerances, timing stated), and consistency with its siblings.

The practical test for verifiability: can you write a test case with concrete inputs, expected
outputs, and a pass/fail criterion straight from the requirement text? If not, the requirement is
not finished, whatever it says.

## 5. Design & architecture

Software architecture covers component decomposition, interfaces, data flow, and control flow.
Detailed design covers algorithms, data structures, and state machines. Both must be traceable
to requirements in both directions.

Safety-critical concerns that belong in the design, not in code review: architectural
partitioning for mixed criticality (lower-DAL code must not be able to corrupt higher-DAL
functions), data coupling and control coupling, resource contention, deactivated code strategy,
determinism, and worst-case execution time.

## 6. Verification & testing

Requirements-based testing in three flavours: normal range, robustness (abnormal inputs,
boundaries), and — where the level demands it — full robustness including overflow, timing, and
capacity anomalies. Verification also includes reviews and analyses, which carry objectives of
their own; testing is not the whole of verification.

Every test case needs inputs, expected results, pass/fail criteria, and a requirement trace. A
test that does not trace to a requirement is not verification evidence, whatever it finds.

Verification independence is not organisational theatre: it exists because the person who wrote
the artifact shares its blind spots. The same reasoning is why an AI agent cannot verify its own
output for independence credit.

Host-based testing does not substitute for hardware/software integration testing on the target.
Compiler behaviour, timing, and memory layout all differ.

## 7. Structural coverage analysis

Coverage is **cumulative** — see the table in `SKILL.md`. Statement coverage from DAL C, adding
decision coverage at DAL B, adding MC/DC and source-to-object-code traceability at DAL A.

Data coupling and control coupling coverage is its own objective and applies at **DAL A, B and C**
— not DAL A alone. It is the one most often mis-scoped, because it sits in the same Annex A table
as MC/DC and gets mentally filed alongside it. It is also the hardest to retrofit: it is satisfied
from the architecture and interface definitions, not by adding test cases.

MC/DC requires that each condition in a decision independently affect the outcome; the minimum
test vector count is N+1 for N conditions.

Coverage is measured *after* requirements-based testing to reveal what those tests did not
reach. Gaps resolve in this order of preference:

1. **Additional requirements-based tests** — identify which requirement facet the uncovered code
   implements and test it from the requirements perspective.
2. **Dead code removal** — code that can never execute, removed under a problem report.
3. **Deactivated code analysis** — intentionally inactive in this configuration; document why and
   verify it is safely isolated.
4. **Analysis justification** — for code unreachable by test (defensive handlers for hardware
   faults, for instance), written analysis justifying the gap, recorded in the SAS.

Target coverage is authoritative where host and target results disagree; the difference is
usually compiler optimisation and is itself worth analysing.

## 8. Traceability & the lifecycle data items

The chain, forward and backward:

```
System requirements → HLR → LLR → Source code → Executable object code
                                              → (DAL A) source-to-object traceability
Requirements (HLR + LLR) → Test cases & procedures → Test results → Structural coverage
```

Forward completeness: every requirement is implemented and tested. Backward justification: every
piece of code and every test traces to a requirement. Gaps either way are findings.

DO-178C Section 11 defines 22 lifecycle data items:

- **Planning** — PSAC (PSAA under DO-278A), SDP, SVP, SCMP, SQAP
- **Standards** — Software Requirements Standards, Software Design Standards, Software Code
  Standards. Note the collision hazard: these are *standards* documents, not the Software
  Requirements *Specification*. Write them out rather than abbreviating "SRS" in a project where
  both exist.
- **Development** — Software Requirements Data, Design Description, Source Code, Executable
  Object Code
- **Verification** — Verification Cases & Procedures, Verification Results
- **CM** — SCI, SLECI/SECI, CM Records, Problem Reports
- **QA** — QA Records
- **Certification liaison** — Software Accomplishment Summary
- **Added in DO-178C** — Trace Data, Parameter Data Item File

Confirm the exact enumeration against Section 11 of the project's copy before building a
compliance matrix from this list.

Common tooling: DOORS, Jama, Codebeamer. The annotations in `SKILL.md` plus
`scripts/trace_check.py` give you machine-checkable traceability without a tool licence, which is
usually enough for the software layer even when the requirements layer lives in DOORS.

## 9. Configuration management

Configuration identification, baselines (functional, allocated, product), change control,
problem reporting, change impact assessment, build and release management, environment control.

CC1 versus CC2 is the control-category distinction: CC1 data carries the full set of CM
objectives (change control, baselines, traceability, retrieval, protection), CC2 a reduced set.
Which data items land in which category varies by assurance level — check the Annex A tables.

Late baselining is the most reliable schedule risk in safety-critical projects. The pressure to
defer it is strongest exactly when the artifacts are churning, which is when the audit trail
becomes most valuable.

## 10. Tool qualification (DO-330)

A tool needs qualification when its use eliminates, reduces, or automates a process required by
the standard, and its failure could go undetected. Classification:

- **Criterion 1** — output becomes part of the deliverable software (code generators; compilers
  whose optimisation changes behaviour)
- **Criterion 2** — automates verification and its output justifies eliminating or reducing
  another process
- **Criterion 3** — could fail to detect an error within its intended use (coverage analysers,
  static analysis tools)
- **No qualification** — used for convenience, with output independently verified

| | DAL A / AL1 | DAL B / AL2 | DAL C / AL3 | DAL D / AL5 |
|---|---|---|---|---|
| Criterion 1 | TQL-1 | TQL-2 | TQL-3 | TQL-4 |
| Criterion 2 | TQL-4 | TQL-4 | TQL-5 | TQL-5 |
| Criterion 3 | TQL-5 | TQL-5 | TQL-5 | TQL-5 |

**AI coding agents specifically.** An LLM-based agent producing deliverable code is a Criterion 1
tool, which at DAL A implies TQL-1 — not achievable for a non-deterministic tool. The workable
path is compensating verification: treat all agent output as untrusted developer output subject
to 100% of the verification that would apply to human-written artifacts. No process is
eliminated or reduced, so no process credit is claimed, so qualification is not triggered. This
argument only holds while it is actually true — the moment someone starts skipping review
because "the agent already checked it", the tool has taken process credit and the qualification
question reopens.

## 11. COTS & service experience (DO-278A)

DO-278A Section 12 governs COTS integration, which is unavoidable in ground systems (operating
systems, databases, middleware, network stacks).

Gap analysis compares available vendor evidence against the objectives for the target AL:
requirements documentation, design or architecture description, test procedures and results, CM
process, defect and patch history.

Service experience under the CAST-1 attributes can substitute for missing development evidence:
duration and breadth of operational deployment, problem report history and resolution rate,
configuration stability, and — the one most often glossed over — similarity of the fielded
operational environment to the intended use. In-service hours from a different usage profile
prove much less than the raw number suggests.

Typical gap mitigations: missing vendor evidence → integrator black-box requirements-based
testing; no source access → monitoring wrappers and defensive architecture (partitioning,
watchdogs, graceful degradation); unknown internals → architectural containment so the COTS
component cannot violate a higher-AL function's assumptions.

The assurance case is claims / arguments / evidence: the claim that the component meets its AL
objectives for the intended function, argued from vendor evidence plus integrator testing plus
service experience, evidenced by specific named documents and data. Where objectives cannot be
met conventionally, document an Alternate Means of Compliance and agree it with the authority
early.

## 12. Ground-based CNS/ATM operations (DO-278A)

What genuinely differs from airborne work:

- **Approval, not certification.** The plan is a PSAA, the authority is an approval authority.
- **Continuous availability.** 24/7 operation means upgrades happen by hot-swap or cutover on a
  live system; the cutover procedure and its rollback path are themselves safety-relevant and
  need requirements and testing.
- **Distributed systems.** Data integrity across network links between sites, and protection
  between components at different ALs sharing infrastructure.
- **Security.** Networked ground infrastructure has an exposure profile that a federated avionics
  bus does not.
- **Operational procedures as mitigation.** Ground systems can credit controller procedures as
  part of the mitigation argument in a way airborne software usually cannot — but the procedure
  then becomes part of the assurance case and must be specified and validated, not assumed.

## 13. Terminology translation

| Collaborator says | Standards term | Why it matters |
|-------------------|----------------|----------------|
| "Unit test" | Requirements-based test case | Tests must trace to requirements, not to functions |
| "Code review" | Source code verification (review method) | Uses checklists aligned to objectives |
| "Bug" | Problem Report | Formal CM artifact with severity, status, resolution |
| "Feature request" | Change Request → derived requirement | Must be impact-assessed and traced |
| "Ship it" | Configuration baseline + SAS completion | Release is a CM event, not a decision |
| "Refactor" | Change impact analysis + regression testing | The change must be traced through every artifact |
| "Code coverage" | Structural coverage analysis | Measured after requirements-based testing, never a target |
| "QA testing" | Software Quality Assurance | SQA audits process and product; it does not execute tests |
| "Peer review" | Review with or without independence | At DAL A/B, reviewer independence is required |
| "Automated testing" | Tool-assisted verification | The tool may need DO-330 qualification |
| "Approved" / "certified" | Two different regulatory outcomes | DO-178C certifies; DO-278A approves |
| "Safety analysis" | System safety assessment (ARP4761) | Performed at system level, not by software |
| "Version control" | Configuration Management | CM adds identification, status accounting, audit |
| "Sprint" | Development phase with entry/exit criteria | Agile is permitted; gates and traceability are not optional |

### Context-aware shorthand

**Airborne (DO-178C)**: "what level?" → DAL A–E · "authority" → certification authority ·
"the plan" → PSAC · "final report" → SAS

**Ground-based (DO-278A)**: "what level?" → AL1–AL6 · "authority" → approval authority ·
"the plan" → PSAA · "COTS question" → Section 12 gap analysis · "can we hot-swap?" → cutover
procedure and regression scope
