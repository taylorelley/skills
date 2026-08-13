<!-- 
  This file is a resource loaded by safety-critical/SKILL.md.
  It is NOT a standalone skill.
  
  The main SKILL.md routes here when:
  - No AGENTS.md exists in the project root
  - AGENTS.md exists but contains unresolved {{PLACEHOLDER}} or TBD values  
  - The user explicitly requests project setup or initialization
-->

# Software Assurance — Project Setup Wizard

This skill guides the user through an interactive interview to populate and generate a project-specific `AGENTS.md` constitution file from the Software Assurance template. The generated file becomes the governing document for all AI agent activity on the project.

## Overview

Setting up a DO-178C or DO-278A project correctly at the start prevents cascading problems through every subsequent phase. This wizard collects the information needed to populate the AGENTS.md template, validates choices for consistency (e.g., DAL/AL determines verification depth, which determines required tools), and generates a ready-to-use project constitution.

The interview is organized into **5 phases**, each collecting a logical group of related decisions. The agent should complete each phase before moving to the next, but can revisit earlier phases if later answers create inconsistencies.

## Prerequisites

- The `AGENTS.md.template` file from this skill's own directory must be readable (or the agent must already have its structure in context)
- The user should have completed (or be able to answer questions about):
  - System safety assessment results (failure condition severity)
  - Target hardware platform selection
  - Toolchain selection
  - Organizational roles for gate approvals

If the user doesn't have all answers yet, the agent should note `{{TBD}}` for those fields and flag them as **open items requiring resolution before Gate 0**.

---

## Interview Protocol

### Before Starting

Greet the user and set expectations:

> This wizard will walk you through setting up your project's AGENTS.md — the constitution that governs all AI agent activity on this project. I'll ask questions in five groups: project identity, assurance level, development environment, team and workflow, and project-specific context.
>
> Some questions have bounded choices (I'll give you options to pick from). Others are open-ended. If you don't have an answer yet, say "TBD" and we'll flag it as an open item.
>
> Ready to start?

---

### Phase 1: Project Identity

**Goal**: Establish the project name, system context, applicable standard, and regulatory framework.

**Questions to ask** (use `AskUserQuestion` for bounded choices, prose for open-ended):

#### Q1.1 — Project Name (open-ended)
> What is the project name? This will be used as the primary identifier throughout all documentation.

*Example: "ADSB-GND-NZ", "ILS-MON-V2", "GCCC-FDP-UPGRADE"*

#### Q1.2 — System Name and Description (open-ended)
> What system does this software belong to? Give me a short name and a one-line description.

*Example: "ADS-B Ground Station — Receives and processes ADS-B surveillance messages for air traffic display"*

#### Q1.3 — Applicable Standard (bounded)
Options: `DO-178C (Airborne)`, `DO-278A (Ground-based CNS/ATM)`, `Both (mixed system)`

**Follow-up logic**:
- If DO-178C → EUROCAE equivalent is ED-12C, planning doc is PSAC
- If DO-278A → EUROCAE equivalent is ED-109A, planning doc is PSAA
- If Both → clarify which components are airborne vs ground-based

#### Q1.4 — Regulatory Authority (bounded)
Options: `FAA`, `EASA`, `CAA New Zealand`, `CASA (Australia)`, `Other (specify)`

**Follow-up logic**:
- FAA → reference AC 20-115D
- EASA → reference AMC 20-115D
- CAA NZ / CASA → determine which guidance material they accept
- Other → ask user to specify the authority and accepted means of compliance

#### Q1.5 — Existing Planning Documents (open-ended)
> Do you have existing PSAC/PSAA, SDP, SVP, SCMP, or SQAP document identifiers? If yes, provide their document IDs. If these haven't been created yet, say "Not yet" and we'll generate placeholder IDs.

---

### Phase 2: Assurance Level Determination

**Goal**: Establish the DAL or AL, which determines verification rigor for the entire project.

#### Q2.1 — Failure Condition Severity (bounded)
> What is the most severe failure condition that the system safety assessment has allocated to this software?

For DO-178C:
Options: `Catastrophic (DAL A)`, `Hazardous (DAL B)`, `Major (DAL C)`, `Minor (DAL D)`, `No Safety Effect (DAL E)`

For DO-278A:
Options: `Catastrophic (AL1)`, `Hazardous/Severe (AL2)`, `Major (AL3)`, `Between Major and Minor (AL4)`, `Minor (AL5)`, `No Effect (AL6)`

**Follow-up**: Display the implications of the selected level:

After the user selects a level, confirm by summarizing what it means:

> **You selected {{LEVEL}} — {{FAILURE_CONDITION}}.**
>
> This means:
> - Roughly **{{N}} objectives** apply, of which about **{{M}}** require independent verification
>   — planning estimates only, to be confirmed against your Annex A tables before they reach the
>   PSAC/PSAA
> - **Structural coverage target** (cumulative): {{statement / statement+decision / statement+decision+MC/DC / none}}
> - **Robustness testing**: {{Full / Partial / Normal range only / None}}
> - **Estimated verification overhead**: {{High / Moderate / Low / Minimal}}
>
> Does this match your expectations from the system safety assessment?

Take the counts from `references/competencies.md` and carry its caveat with them. Quoting an
unverified independence count into a compliance matrix is the kind of error that surfaces at an
SOI review, when it is expensive to correct.

#### Q2.2 — Mixed Criticality (conditional — only if relevant)
> Does this project contain software components at different assurance levels? If yes, describe the partitioning strategy (e.g., "Navigation processing at DAL B, display rendering at DAL D, partitioned via memory protection unit").

---

### Phase 3: Development Environment

**Goal**: Establish the language, toolchain, target platform, and tool qualification posture.

#### Q3.1 — Programming Language (bounded)
Options: `C99`, `C11`, `C17`, `C++ (restricted subset — specify standard)`, `Ada (SPARK subset)`, `Ada 2012`, `Other (specify)`

#### Q3.2 — Coding Standard (bounded, multi-select)
Options: `MISRA C:2012`, `CERT C`, `MISRA C++:2023`, `Project-specific (will define)`, `Other (specify)`

#### Q3.3 — Target Platform (open-ended)
> What is the target processor and board? Include processor family, specific part number if known, and any real-time operating system.

*Example: "PowerPC MPC8548E on custom SBC, VxWorks 7.0"*
*Example: "ARM Cortex-A53 on Raspberry Pi CM4, bare-metal"*
*Example: "x86-64 server, Red Hat Enterprise Linux 8 (ground-based)"*

#### Q3.4 — Host Development Platform (open-ended)
> What is the host development platform (OS and architecture)?

*Example: "Ubuntu 22.04 x86-64", "Windows 11 with WSL2"*

#### Q3.5 — Compiler (open-ended)
> What compiler and version will be used? Include both host and target compilers if different.

*Example: "GCC 12.3 (host), Wind River Diab 5.9 (target)"*

#### Q3.6 — Static Analysis Tool (bounded + open-ended)
Options: `PC-lint Plus`, `Polyspace Bug Finder / Code Prover`, `Coverity`, `cppcheck`, `LDRA TBmisra`, `Other (specify)`, `Not yet selected`

#### Q3.7 — Coverage Tool (bounded + open-ended)
Options: `LDRA TBrun`, `VectorCAST`, `Rapita RapiCover`, `gcov/lcov (host only)`, `Other (specify)`, `Not yet selected`

#### Q3.8 — Test Framework (open-ended)
> What test execution framework will be used? (e.g., "VectorCAST", "LDRA TBrun", "custom harness", "Unity + CMock", "Google Test (host)")

#### Q3.9 — Build System (open-ended)
> What build system will be used? (e.g., "CMake 3.28", "Make with project Makefiles", "Wind River Workbench")

#### Q3.10 — Dynamic Memory Policy (bounded)
Options: `Prohibited (no malloc/calloc/realloc/free)`, `Permitted during initialization only`, `Permitted with bounded pool allocator`, `Permitted with constraints (specify)`

#### Q3.11 — Recursion Policy (bounded)
Options: `Prohibited`, `Permitted with provable termination and bounded stack depth`

---

### Phase 4: Team and Workflow

**Goal**: Establish gate approvers, branching strategy, and team conventions.

#### Q4.1 — Gate Approver Roles (open-ended)
> Who approves each phase gate? Provide role titles (not individual names — roles are more stable). Use the same role for multiple gates if appropriate.

Default suggestion:
```
Gate 0 (Planning):      Project Lead + DER/CVE (if applicable)
Gate 1 (Requirements):  Software Lead
Gate 2 (Design):        Software Lead
Gate 3 (Code):          Software Lead + Independent Reviewer
Gate 4 (Integration):   Software Lead
Gate 5 (Verification):  Verification Lead
Gate 6 (CM Audit):      CM Manager + QA Lead
Gate 7 (Approval):      Project Lead + Authority Representative
```

> Do you want to use these defaults, or customize?

#### Q4.2 — Branching Strategy (bounded)
Options: `Standard Software Assurance (main → develop → feature branches per CR/PR)`, `Trunk-based with short-lived branches`, `Custom (specify)`

#### Q4.3 — ID Prefix Convention (open-ended)
> What module prefix codes will this project use for requirement, design, and test IDs?

*Example: "NAV for navigation, SUR for surveillance, COM for communications, UTL for utilities"*

Default pattern: `HLR-{{PREFIX}}-NNN`, `LLR-{{PREFIX}}-NNN-NNN`, `DES-{{PREFIX}}-NNN`, `TST-{{PREFIX}}-NNN-NNN`

#### Q4.4 — Problem Report and Change Request Numbering (bounded)
Options: `Year-sequential (PR-2025-0001, CR-2025-0001)`, `Project-sequential (PR-{{PROJECT}}-0001)`, `Custom (specify)`

#### Q4.5 — Classification and Handling (bounded)
Options: `Unclassified / Public`, `Company Confidential`, `Export Controlled (ITAR/EAR)`, `Other (specify)`

---

### Phase 5: Project-Specific Context

**Goal**: Capture any unique constraints, COTS components, reuse, or authority agreements.

#### Q5.1 — COTS Components (conditional — DO-278A or systems with COTS)
> Does this project integrate any commercial off-the-shelf software components? If yes, list each one with its name, version, function, and current assurance status.

*Example: "Red Hat Enterprise Linux 8.9 — Operating system — No formal assurance — Gap analysis pending"*

#### Q5.2 — Reused Components
> Are any previously certified/approved software components being reused? If yes, provide their identification, original DAL/AL, and any delta requirements.

#### Q5.3 — Target Hardware Constraints (open-ended)
> Are there specific hardware constraints the agent should know about? (memory limits, timing budgets, I/O constraints, WCET requirements)

*Example: "256 KB RAM, 1 MB Flash, 100 MHz clock. WCET budget for main loop: 8ms. No floating-point unit — use fixed-point only."*

#### Q5.4 — Interface Agreements (open-ended)
> Does this software interface with other systems that have their own assurance requirements? If yes, describe the interfaces and any ICD (Interface Control Document) references.

#### Q5.5 — Known Deviations (open-ended)
> Are there any planned deviations from the standard process that have been agreed with the authority? (e.g., "MC/DC not required for lookup tables per SOI #1 agreement")

#### Q5.6 — Additional Notes (open-ended)
> Anything else the agent should know about this project? (security requirements, multi-site development, subcontractor involvement, legacy system migration, etc.)

---

## Generation Process

After all phases are complete, generate the AGENTS.md by following these steps:

### Step 1: Validate Consistency

Before generating, check for internal consistency:

| Check | Rule |
|-------|------|
| Standard ↔ Level terminology | DO-178C uses DAL A–E; DO-278A uses AL1–AL6. Don't mix. |
| Level ↔ Coverage target | DAL A = MC/DC, DAL B = Decision, DAL C = Statement, DAL D = HLR-only, DAL E = None |
| Level ↔ Robustness | DAL C+ requires robustness testing; DAL D does not |
| Level ↔ Independence count | Must match the standard's Annex A table for the selected level |
| Dynamic memory ↔ Level | If DAL A/B and dynamic memory permitted, flag for discussion |
| Recursion ↔ Level | If DAL A/B and recursion permitted, flag for discussion |
| COTS ↔ Standard | COTS gap analysis process is DO-278A Section 12; for DO-178C COTS is treated as developed code |
| AL4 ↔ Standard | AL4 only exists in DO-278A. If DO-178C selected with AL4, this is an error |

If any inconsistency is found, stop and resolve with the user before generating.

### Step 2: Resolve TBD Items

List all fields marked TBD and present them as a summary:

> **Open items requiring resolution before Gate 0:**
> 1. {{Field}} — Marked TBD because {{reason}}
> 2. ...
>
> These will be recorded as `{{TBD — [reason]}}` in the generated AGENTS.md. They must be resolved before the project can pass Gate 0 (Planning Complete).

### Step 3: Generate the AGENTS.md

Read `AGENTS.md.template` from this skill's own directory and perform the following substitutions:

1. **Replace all `{{PLACEHOLDER}}` tokens** with collected values
2. **Delete inapplicable assurance level rows** from tables — keep only the row matching the project's level, plus headers
3. **Delete inapplicable standard references** — if DO-178C only, remove AL/PSAA references; if DO-278A only, remove DAL/PSAC references
4. **Populate the tool register** with all tools from Phase 3, including the AI agent entry
5. **Fill the verification strategy table** — check only the applicable cells for the project's level
6. **Populate project-specific notes** from Phase 5 answers
7. **Set all gate approver roles** from Phase 4 answers
8. **Generate placeholder document IDs** for any planning documents not yet created, using the pattern: `{{DOCTYPE}}-{{PROJECT}}-001`
9. **Set the current phase** to `PLANNING` (the project is being set up, so it cannot be past Gate 0)
10. **Set the baseline** to `—` (no baseline exists yet)
11. **Set the version** to `0.1-DRAFT`
12. **Set `{{SKILL_PATH}}`** to this skill's directory as reachable from the project root, so the
    generated file's references to `references/` and `scripts/trace_check.py` actually resolve.
    Leave the objective/independence confirmation rows as `{{TBD}}` — they are a deliberate open
    item for the team to close against their own Annex A tables, not something to guess.

### Step 4: Write the File

Write the generated AGENTS.md to the project root directory. Present it to the user for review.

### Step 5: Generate Companion Scaffolding

After the AGENTS.md is generated, offer to scaffold the project directory structure:

> Your AGENTS.md is ready. Would you like me to also create the project directory structure with placeholder files for:
> - Planning documents (PSAC/PSAA, SDP, SVP, SCMP, SQAP stubs)
> - Standards documents (SRS, SDS, SCS stubs)
> - Requirements directory structure
> - Design directory structure
> - Test directory structure
> - Traceability matrix template
> - CM directory with CR/PR templates
> - Tool register

If the user agrees, generate the directory tree and stub files with appropriate headers and TBD content. Each stub should include the file's purpose, required content per the standard, and placeholder sections.

The scaffolded layout is what `scripts/trace_check.py` expects by default
(`docs/requirements/**`, `test/cases/**`, `src/**`). Run it once against the fresh scaffold and
show the user the output — on an empty project it reports zero of everything, which is a useful
demonstration of what it will tell them later and confirms the paths line up.

---

## Handling Edge Cases

### User doesn't know their DAL/AL yet
> The assurance level is determined by the system safety assessment (ARP4761) flowing through the system development process (ARP4754A). If this hasn't been completed yet, I'll mark the level as TBD. However, **almost nothing else in this AGENTS.md can be finalized without a level** — it determines verification depth, coverage targets, independence requirements, and tool qualification needs. I'd recommend resolving this before proceeding with development.

### User wants to start coding immediately
> I understand the urgency, but the DO-178C/DO-278A framework is explicitly phase-gated. Writing code before requirements and design are baselined means that code will need to be reworked and re-verified when the upstream artifacts stabilize. This is consistently the most expensive mistake in safety-critical projects. Let's get the foundation right — it will save significant time downstream.
>
> If you need to explore feasibility or prototype, I can help with that in a clearly separated prototype workspace that is **not** part of the certification/approval evidence. Prototype code must never be promoted to production without going through the full lifecycle.

### User's project spans both DO-178C and DO-278A
> Mixed airborne/ground-based systems are common (e.g., a ground station with some software that runs on an aircraft). Each software component must be assigned to either DO-178C or DO-278A based on where it executes. I'll create a single AGENTS.md with a component table that maps each module to its applicable standard and level. The shared processes (CM, QA) can cover both, but verification objectives must be tracked separately per standard.

### User asks about Agile/Scrum compatibility
> DO-178C and DO-278A are lifecycle-model-agnostic — they do not mandate waterfall. Agile methods are permitted provided that: (1) phase gate discipline is maintained (sprints can iterate within a phase, but cannot skip gates), (2) traceability is maintained continuously, not retrofitted, (3) baselines are established at defined points with formal change control thereafter, and (4) verification activities maintain required independence. Several organizations have successfully combined Agile with DO-178C — the key is that "working software" in the Agile sense is replaced by "verified, traced, baselined software" in the DO-178C sense.

### User is working on a modification to existing certified/approved software
> Modifications to previously certified/approved software require change impact analysis before any development begins. I'll configure the AGENTS.md with the existing baseline as the starting point and set the current phase based on where the modification enters the lifecycle. The key question is: does this modification require re-verification of only the changed areas (regression scope), or does it affect the overall assurance argument? The PSAC/PSAA amendment will define the scope.

---

## Quick Start Mode

If the user says something like "just give me a quick setup for a DAL C ground-based radar project", the agent should:

1. **Fill in sensible defaults** for everything not specified
2. **Present the completed AGENTS.md** with all assumptions highlighted
3. **List all assumptions** the user should review and confirm
4. **Flag critical assumptions** that could affect certification/approval

Quick-start defaults:

| Field | Default |
|-------|---------|
| Standard | DO-278A (if "ground-based" mentioned), DO-178C (if "airborne" mentioned) |
| Authority | Infer from user's locale if known |
| Language | C99 |
| Coding Standard | MISRA C:2012 |
| Dynamic Memory | Prohibited |
| Recursion | Prohibited |
| Branching | Standard Software Assurance pattern |
| Numbering | Year-sequential |
| Classification | Company Confidential |
| Gate Approvers | Default role assignments |
| Current Phase | PLANNING |

---

## Post-Setup Checklist

After the AGENTS.md is generated and accepted, remind the user:

> **Your project is now initialized.** Here's what happens next:
>
> 1. **Review the AGENTS.md** — Every field, every rule. This is your project's constitution.
> 2. **Resolve all TBD items** — These must be closed before Gate 0.
> 3. **Baseline the AGENTS.md itself** — It is a CC1 Configuration Item.
> 4. **Begin Planning Phase** — Draft your PSAC/PSAA, SDP, SVP, SCMP, SQAP.
> 5. **Register your tools** — Especially the AI agent, compiler, and any analysis tools.
> 6. **Schedule SOI #1** — Planning review with the certification/approval authority.
>
> I'm ready to help with any of these. What would you like to tackle first?

---

## Summary

The Software Assurance Setup wizard ensures every DO-178C/DO-278A project starts with a properly configured AGENTS.md that encodes the right assurance level, verification depth, traceability conventions, and process discipline from day one. By collecting decisions through a structured interview rather than letting them emerge ad-hoc during development, the setup process prevents the most common and expensive mistakes in safety-critical software projects: wrong assurance level application, missing traceability, inadequate tool qualification, and bypassed phase gates.

**Remember**: The ten minutes spent in this setup wizard save hundreds of hours of rework during verification and certification. Get the foundation right.
