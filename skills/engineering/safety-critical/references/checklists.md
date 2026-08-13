# Phase Gate Checklists

Exit criteria per phase. These are the software-side checks an agent can meaningfully assess or
prepare; the gate itself is approved by a named human, and the project `AGENTS.md` names who.

Use these to answer "is this phase actually finished?" — and report honestly when it isn't. A
checklist run that always comes back clean is not doing anything.

---

## Gate 1 — Requirements

- [ ] Every requirement has a unique ID per the project convention
- [ ] Every requirement traces to a parent system requirement, or is flagged `@derived`
- [ ] Every requirement is a single atomic testable "shall" statement
- [ ] All derived requirements carry rationale and a safety impact assessment, and have been
      routed to the system safety process
- [ ] Requirements reviewed for unambiguity, completeness, consistency, verifiability,
      traceability
- [ ] Forward completeness: every allocated system requirement has ≥1 software requirement
- [ ] `scripts/trace_check.py` reports no dangling parent references
- [ ] Requirements baseline established in CM

## Gate 2 — Design

- [ ] Architecture describes all components, interfaces, data flow, control flow
- [ ] Every design element traces to ≥1 requirement
- [ ] Partitioning strategy documented for mixed-criticality components
- [ ] Data coupling and control coupling identified
- [ ] Design reviewed against requirements in both directions
- [ ] Derived design decisions flagged and safety-assessed
- [ ] Design baseline established in CM

## Gate 3 — Code

- [ ] Every function carries its own traceability annotations (`@req`, `@design`) — not only the
      file header
- [ ] All derived implementation decisions flagged `@derived` with safety impact
- [ ] Coding standard compliance verified by static analysis, findings triaged
- [ ] Dynamic memory policy honoured per `AGENTS.md`
- [ ] No unbounded recursion
- [ ] All inputs validated, all return values checked, all error paths handled
- [ ] `scripts/trace_check.py` reports no orphan functions
- [ ] Independent human code review completed — the agent cannot supply this
- [ ] Code baseline established in CM
- [ ] `DRAFT — REQUIRES INDEPENDENT REVIEW` cleared only after that human review

## Gate 4 — Integration

- [ ] Executable object code built from baselined source
- [ ] Build is reproducible: same source produces the same binary
- [ ] Integration tests pass on target hardware, not only on host
- [ ] No unresolved linker warnings or errors

## Gate 5 — Verification

- [ ] Requirements-based test cases exist for 100% of requirements
- [ ] Every requirement facet covered — range, tolerance, timing, error handling — not just one
      case per requirement
- [ ] All test cases executed with results recorded
- [ ] Normal range tests: 100% pass
- [ ] Robustness tests: 100% pass (DAL C / AL3 and above)
- [ ] HW/SW integration tests executed on target: 100% pass
- [ ] Structural coverage meets the cumulative target for the level (see `SKILL.md`)
- [ ] Coverage gaps resolved by an approved method, with analysis justifications recorded
- [ ] All problem reports dispositioned — closed, or deferred with safety justification
- [ ] `scripts/trace_check.py` clean in both directions
- [ ] Verification results baseline established in CM

## Gate 6 — CM audit

- [ ] All lifecycle data items at the correct CC1/CC2 status
- [ ] All baselines verified: requirements, design, code, test
- [ ] All problem reports closed or deferred with justification
- [ ] All change requests closed
- [ ] CM records complete and auditable
- [ ] SQA records confirm process compliance across the project, not just at the end

## Gate 7 — Certification / approval

- [ ] SAS documents planned versus accomplished for every applicable objective
- [ ] All deviations from the plans documented and justified
- [ ] Open problem reports assessed for safety impact and agreed with the authority
- [ ] CM records complete and auditable
- [ ] PSAC/PSAA compliance matrix complete, with objective counts confirmed against the
      project's own Annex A tables rather than any secondary source
- [ ] Release baseline established
