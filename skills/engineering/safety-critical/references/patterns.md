# Code Patterns & Troubleshooting

Implementation patterns for safety-critical C, artifact structures, and a diagnostic table for
common verification failures.

## Contents

1. [Defensive input validation](#pattern-1--defensive-input-validation)
2. [State machine with traceable transitions](#pattern-2--state-machine-with-traceable-transitions)
3. [Traceability matrix](#pattern-3--traceability-matrix)
4. [Problem report](#pattern-4--problem-report)
5. [Practices worth keeping](#practices-worth-keeping)
6. [Troubleshooting](#troubleshooting)

---

## Pattern 1 — Defensive input validation

Every function at a module boundary validates before processing. Sequential gates keep each
rejection reason distinguishable to the caller, which matters when the caller has to decide
between retry, degrade, and alarm.

```c
/**
 * @req HLR-ILS-031: Validate all external inputs
 * @design DES-ILS-020: Input validation gate pattern
 */
ils_status_t ils_process_localizer(
    const ils_input_t *input,
    ils_output_t *output)
{
    /* Gate 1: Null pointer check */
    if ((input == NULL) || (output == NULL))
    {
        return ILS_ERR_NULL_PTR;
    }

    /* Gate 2: Range check */
    if ((input->frequency_mhz < ILS_FREQ_MIN) ||
        (input->frequency_mhz > ILS_FREQ_MAX))
    {
        return ILS_ERR_RANGE;
    }

    /* Gate 3: Freshness check */
    if (input->age_ms > ILS_MAX_DATA_AGE_MS)
    {
        return ILS_ERR_STALE;
    }

    /* All gates passed — process */
    return ils_compute_deviation(input, output);
}
```

The freshness gate is the one most often left out. In a distributed ground system, data that is
structurally valid but stale is the more common failure, and it is indistinguishable from fresh
data without an explicit age check.

## Pattern 2 — State machine with traceable transitions

Explicit states, one requirement per transition, and a `default` case that fails safe. The
`default` is not dead code in a safety argument — it is the response to memory corruption, and
it needs a derived requirement because no functional requirement asked for it.

```c
/**
 * @req HLR-ADSB-015: ADS-B track state management
 * @design DES-ADSB-008: Track lifecycle state machine
 *
 * States: TENTATIVE → CONFIRMED → COASTING → DROPPED
 * Transitions documented in DES-ADSB-008 Table 3.
 */
typedef enum {
    TRACK_TENTATIVE,   /* @req HLR-ADSB-015a: Initial detection */
    TRACK_CONFIRMED,   /* @req HLR-ADSB-015b: M of N updates received */
    TRACK_COASTING,    /* @req HLR-ADSB-015c: Updates missed, extrapolating */
    TRACK_DROPPED      /* @req HLR-ADSB-015d: Coast timeout exceeded */
} track_state_t;

/**
 * @req HLR-ADSB-015
 * @design DES-ADSB-008
 */
track_state_t track_update_state(
    track_t *track,
    bool update_received,
    uint32_t elapsed_ms)
{
    switch (track->state)
    {
        case TRACK_TENTATIVE:
            if (update_received)
            {
                track->confirm_count++;
                if (track->confirm_count >= TRACK_M_OF_N_THRESHOLD)
                {
                    /* @req HLR-ADSB-015b */
                    track->state = TRACK_CONFIRMED;
                }
            }
            else if (elapsed_ms > TRACK_TENTATIVE_TIMEOUT_MS)
            {
                /* @req HLR-ADSB-015d */
                track->state = TRACK_DROPPED;
            }
            break;

        case TRACK_CONFIRMED:
            if (!update_received && (elapsed_ms > TRACK_COAST_ENTRY_MS))
            {
                /* @req HLR-ADSB-015c */
                track->state = TRACK_COASTING;
                track->coast_start_ms = get_system_time_ms();
            }
            break;

        case TRACK_COASTING:
            if (update_received)
            {
                /* @req HLR-ADSB-015b: Re-confirmed */
                track->state = TRACK_CONFIRMED;
                track->coast_start_ms = 0U;
            }
            else if (elapsed_ms > TRACK_COAST_TIMEOUT_MS)
            {
                /* @req HLR-ADSB-015d */
                track->state = TRACK_DROPPED;
            }
            break;

        case TRACK_DROPPED:
            /* Terminal state — no transitions out */
            break;

        default:
            /* @derived DRV-ADSB-008-001: Defensive handling of an invalid
             * state value. Safety: prevents undefined behaviour arising from
             * memory corruption by forcing a known safe terminal state. */
            track->state = TRACK_DROPPED;
            log_error(ERR_INVALID_STATE, track->id);
            break;
    }

    return track->state;
}
```

## Pattern 3 — Traceability matrix

```markdown
| Requirement     | Design      | Source File      | Test Case(s)          | Status   |
|-----------------|-------------|------------------|-----------------------|----------|
| HLR-NAV-042     | DES-NAV-012 | vor_bearing.c:42 | TST-NAV-042-001..008  | VERIFIED |
| HLR-NAV-043     | DES-NAV-012 | vor_bearing.c:35 | TST-NAV-042-005..006  | VERIFIED |
| HLR-NAV-044     | DES-NAV-012 | vor_bearing.c:22 | TST-NAV-042-007..008  | VERIFIED |
| DRV-NAV-012-001 | DES-NAV-012 | vor_bearing.c:15 | TST-NAV-042-001..004  | REVIEW   |
| DRV-NAV-012-002 | DES-NAV-012 | vor_bearing.c:45 | TST-NAV-042-001..004  | REVIEW   |
```

A hand-maintained matrix drifts from the code the moment anyone is busy, and a matrix that
asserts "no gaps" is worth nothing without a check that regenerates it from the annotations.
Run `scripts/trace_check.py` before believing one — including one you just wrote.

## Pattern 4 — Problem report

```markdown
## PR-2026-0142: VOR bearing double-wrap not fully normalized

@pr PR-2026-0142
@req HLR-NAV-042
@severity MAJOR
@status OPEN
@found_in BL-NAV-CODE-002
@found_by TST-NAV-042-003 (boundary test)

**Description**: When accumulated phase correction pushes the raw bearing to 720° or
above (two full rotations — seen after repeated phase-unwrap corrections under noisy
signal conditions), the output still reports a value ≥ 360° (e.g. 362.5°) instead of
fully wrapping into [0.0, 360.0). Violates the HLR-NAV-042 post-condition.

**Root Cause**: math_normalize_angle() performs a single conditional subtraction
(`if (angle >= 360.0f) angle -= 360.0f;`). That correctly resolves a value that has
wrapped once (360.0° → 0.0°, 360.5° → 0.5°), but a value needing two wraps still sits
at or above 360° afterward — the `if` never runs a second time. The function also has
no lower-bound handling: a negative raw_bearing (possible depending on how
vor_phase_extract() resolves quadrants) passes through unmodified, violating the same
[0.0, 360.0) contract from the other direction.

**Impact Assessment**:
- HLR-NAV-042: directly violated — output can fall outside its stated range in either
  direction, positive over-wrap or negative underflow.
- Downstream: navigation display may show an out-of-range or discontinuous bearing.
- Safety: momentary display anomaly, no loss of navigation function once corrected.
  Failure condition: Minor.

**Proposed Fix**: Replace the single conditional subtraction with `fmodf(angle, 360.0f)`
followed by `if (angle < 0.0f) angle += 360.0f;` — fmodf handles any number of wraps in
one call, and the guard brings a negative result (fmodf's sign follows its first
argument) back into range.

**Regression Scope**: TST-NAV-042-001..008 (full suite), including new cases for
raw_bearing ≥ 720° and raw_bearing < 0°.
TST-MATH-UTIL-015..020 (angle normalization).
```

---

## Practices worth keeping

**Do**

- Write requirements before design, design before code
- Give every requirement, design element, test case, and problem report a unique ID
- Trace bidirectionally — forward completeness and backward justification
- Flag every derived requirement with rationale and safety impact
- Validate all inputs, check all return values, handle all error paths
- Write deterministic code — the same inputs always produce the same outputs
- Document assumptions and constraints where the reader will hit them
- Run static analysis early and continuously
- Test on the target; host testing cannot replace HW/SW integration testing
- Keep the SAS current as a living document rather than writing it at the end

**Don't**

- Write code with no traced requirement — orphan code is a finding
- Use dynamic allocation in flight-critical software (fragmentation, non-determinism)
- Use recursion without provable termination and a bounded stack depth
- Skip change impact analysis because a change looks trivial
- Treat code coverage as requirements coverage — they measure different things
- Let the agent serve as independent reviewer
- Merge generated code without human review
- Chase coverage targets with code-directed tests
- Defer CM baselining — late baselining is the most reliable schedule risk there is
- Confuse SQA with testing — SQA audits the process
- Ignore deactivated code — verify it to the same level or isolate it demonstrably
- Commingle DAL levels without architectural partitioning

---

## Troubleshooting

| Issue | Likely cause | Resolution |
|-------|--------------|------------|
| Orphan code found in coverage analysis | Code traces to no requirement | Raise a derived requirement with safety justification, or remove it as dead code |
| Requirements-based tests reach low statement coverage | Requirements incomplete, or tests exercise only one facet each | Review requirements for completeness; add boundary and robustness cases; analyse uncovered code for unstated derived requirements |
| MC/DC gap on a complex boolean | Test vectors do not independently toggle each condition | Build the MC/DC truth table, identify the minimum N+1 vectors; may need additional requirement-level conditions |
| Matrix has forward gaps (requirement → no test) | Test case missing | Write a requirements-based case. Never close the gap with a code-directed test |
| Matrix has backward gaps (code → no requirement) | Implementation went beyond the spec | Decide: derived requirement (annotate and safety-assess) or dead code (remove under a PR) |
| Change impact analysis cascades to 50+ artifacts | Normal for safety-critical systems | Scope the regression precisely; consider architectural partitioning to bound future changes |
| COTS vendor supplies no lifecycle data | Normal for commercial software | Integrator black-box testing plus a DO-278A Section 12 assurance case; AL4 is the usual target |
| Static analysis reports hundreds of violations | Rule set does not match the project SCS | Configure the tool to the project standard; triage by severity; safety-relevant violations first |
| Coverage differs between host and target | Compiler optimisation and differing execution paths | Target coverage is authoritative; analyse host-only paths for compiler-introduced dead code |
| AI-generated code fails independence review | The agent made design decisions absent from the spec | Reject and regenerate against a tighter spec; check whether the design element was underspecified |
| Traceability matrix claims completeness but an audit finds gaps | Matrix maintained by hand, drifted from the source | Regenerate from annotations with `scripts/trace_check.py`; treat the stale matrix as a PR against CM records |
