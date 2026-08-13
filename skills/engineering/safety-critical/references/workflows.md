# Development Workflows

Step-by-step procedures for producing lifecycle artifacts. Read the one that matches the task.
All of these assume DEVELOPMENT MODE — the project's `AGENTS.md` has been read and its assurance
level, phase, and naming conventions are loaded.

## Contents

1. [Write a software requirement (HLR or LLR)](#workflow-1--write-a-software-requirement)
2. [Implement code from a design specification](#workflow-2--implement-code-from-a-design-specification)
3. [Generate requirements-based test cases](#workflow-3--generate-requirements-based-test-cases)
4. [Perform change impact analysis](#workflow-4--perform-change-impact-analysis)
5. [Evaluate a COTS component (DO-278A)](#workflow-5--evaluate-a-cots-component-do-278a)
6. [Assess DO-330 tool qualification need](#workflow-6--assess-do-330-tool-qualification-need)

---

## Workflow 1 — Write a software requirement

1. **Identify the source.** Which system requirement or HLR drives this? Record the trace. If you
   cannot name a parent, you are writing a derived requirement — go to step 4 first.
2. **Confirm the DAL/AL** from `AGENTS.md`. It sets verification rigour and therefore how much
   detail the requirement must pin down.
3. **Write it** against the attributes checklist: unique ID per project convention; single atomic
   testable "shall" statement; unambiguous; verifiable; explicitly traced; complete with all
   conditions, tolerances and timing; consistent with siblings.
4. **Identify derived requirements.** Does this introduce behaviour absent from the parent spec?
   Flag `@derived`, document rationale, and route it to the system safety process — derived
   requirements are the ones the safety assessment has not seen.
5. **Validate testability** by drafting the test case in your head. Concrete inputs, expected
   outputs, pass/fail criterion. If you cannot, the requirement is not finished.

### Template

```markdown
## HLR-NAV-042: VOR Bearing Calculation Accuracy

@req HLR-NAV-042
@parent SYS-NAV-018
@dal C
@status DRAFT
@baseline —

**Shall Statement**: The software shall calculate VOR magnetic bearing with an
accuracy of ±0.1 degrees when the received signal-to-noise ratio is ≥ 20 dB.

**Conditions**:
- Input: VOR receiver I/Q samples at 30 Hz update rate
- Operating range: 0.0 to 359.9 degrees magnetic
- SNR threshold: 20 dB minimum

**Tolerances**:
- Accuracy: ±0.1 degrees (normal conditions)
- Latency: ≤ 100 ms from sample to output
- Update rate: 30 Hz ± 1 Hz

**Boundary Conditions**:
- Bearing wrap-around at 360°/0° boundary
- SNR at exactly 20 dB threshold
- Maximum slew rate: 15°/second

**Derived Requirements**: None identified.

**Safety**: Incorrect bearing could contribute to navigation error. Failure
condition severity determined by parent system safety assessment
(SYS-NAV-018 → Major → DAL C).
```

---

## Workflow 2 — Implement code from a design specification

1. **Verify the design is baselined.** Coding against a draft design means reworking the code
   when the design settles, and re-verifying it.
2. **Identify every requirement traced to the design element.** The code must satisfy all of them.
3. **Check the coding standard** named in `AGENTS.md` (MISRA C, CERT C, project SCS).
4. **Implement with traceability headers** at file and function level.
5. **Run static analysis** before asking for review.
6. **Flag for independent review** — you cannot supply it yourself.
7. **Record in CM**, associated with the change request.

```c
/**
 * @file vor_bearing.c
 * @brief VOR magnetic bearing calculation module
 *
 * @req    HLR-NAV-042, HLR-NAV-043, HLR-NAV-044
 * @design DES-NAV-012
 * @dal    C
 * @status DRAFT — REQUIRES INDEPENDENT REVIEW
 *
 * @derived DRV-NAV-012-001: Internal 32-bit fixed-point representation
 *          selected for deterministic timing on the target processor.
 *          Safety impact: no new failure mode — accuracy validated by
 *          TST-NAV-042-001 through TST-NAV-042-008.
 */

#include "vor_bearing.h"
#include "math_utils.h"   /* @design DES-MATH-001 */
#include "signal_proc.h"  /* @design DES-SIG-003 */

/**
 * @brief Calculate VOR magnetic bearing from I/Q samples
 * @req HLR-NAV-042
 * @design DES-NAV-012
 *
 * @param[in]  iq_samples    Pointer to I/Q sample buffer (30 Hz)
 * @param[in]  sample_count  Number of samples in buffer
 * @param[out] bearing_deg   Bearing in degrees magnetic [0.0, 360.0)
 * @return VOR_OK, VOR_ERR_SNR if SNR < 20 dB, VOR_ERR_INPUT if params invalid
 *
 * @pre  iq_samples != NULL
 * @pre  sample_count > 0 && sample_count <= MAX_VOR_SAMPLES
 * @post bearing_deg in range [0.0, 360.0) if return == VOR_OK
 */
vor_status_t vor_calculate_bearing(
    const iq_sample_t *iq_samples,
    uint16_t sample_count,
    float *bearing_deg)
{
    /* @req HLR-NAV-044: Validate all inputs before processing */
    if ((iq_samples == NULL) || (bearing_deg == NULL))
    {
        return VOR_ERR_INPUT;
    }

    if ((sample_count == 0U) || (sample_count > MAX_VOR_SAMPLES))
    {
        return VOR_ERR_INPUT;
    }

    /* @req HLR-NAV-043: Reject signal when SNR < 20 dB */
    const float snr_db = signal_estimate_snr(iq_samples, sample_count);
    if (snr_db < VOR_MIN_SNR_DB)
    {
        return VOR_ERR_SNR;
    }

    /* @req HLR-NAV-042: Calculate bearing with ±0.1° accuracy */
    const float raw_bearing = vor_phase_extract(iq_samples, sample_count);

    /* @derived DRV-NAV-012-002: Normalize bearing to [0.0, 360.0).
     * Safety: prevents wrap-around error at the 360°/0° boundary. */
    *bearing_deg = math_normalize_angle(raw_bearing);

    return VOR_OK;
}
```

Note that every function carries its own `@req`, not just the file header. Traceability is
established per code component; a module-level annotation does not justify each function inside
it, and `scripts/trace_check.py` will report functions that lack their own.

---

## Workflow 3 — Generate requirements-based test cases

1. **Analyse the requirement** for testable conditions, boundary values, and error conditions.
2. **Determine required test categories** from the level: normal range at every level;
   robustness (abnormal inputs, boundaries) from DAL C / AL3; full robustness including overflow,
   timing and capacity anomalies at DAL A / AL1.
3. **Write structured cases** — see the three shapes below.
4. **Verify completeness.** Every requirement needs at least one case, and every *facet* of a
   requirement (range, tolerance, timing, error handling) needs coverage. A requirement with one
   happy-path test is not covered.
5. **Update the traceability matrix** and re-run `scripts/trace_check.py`.

### Normal range

```markdown
## TST-NAV-042-001: VOR Bearing Normal Range — Cardinal Points

@test    TST-NAV-042-001
@req     HLR-NAV-042
@type    Normal Range
@dal     C
@status  DRAFT

**Objective**: Verify bearing calculation accuracy at cardinal points under
normal SNR conditions.

**Pre-conditions**:
- VOR receiver initialized and operational
- Test signal generator configured for specified bearings
- SNR set to 30 dB (well above the 20 dB threshold)

| Step | Input Bearing (°) | SNR (dB) | Expected Output (°) | Tolerance |
|------|-------------------|----------|---------------------|-----------|
| 1    | 0.0               | 30       | 0.0                 | ±0.1°     |
| 2    | 90.0              | 30       | 90.0                | ±0.1°     |
| 3    | 180.0             | 30       | 180.0               | ±0.1°     |
| 4    | 270.0             | 30       | 270.0               | ±0.1°     |

**Pass/Fail Criteria**: All calculated bearings within ±0.1° of expected.
Output in range [0.0, 360.0). Return status VOR_OK.

**Post-conditions**: No error flags set. Module ready for next calculation.
```

### Boundary / robustness

```markdown
## TST-NAV-042-005: VOR Bearing Robustness — SNR at Threshold

@test    TST-NAV-042-005
@req     HLR-NAV-042, HLR-NAV-043
@type    Robustness / Boundary
@dal     C
@status  DRAFT

**Objective**: Verify correct behaviour at the 20 dB SNR acceptance boundary.

| Step | Input Bearing (°) | SNR (dB) | Expected Behaviour          |
|------|-------------------|----------|-----------------------------|
| 1    | 45.0              | 20.0     | Bearing calculated, VOR_OK  |
| 2    | 45.0              | 19.9     | Rejected, VOR_ERR_SNR       |
| 3    | 45.0              | 20.1     | Bearing calculated, VOR_OK  |

**Pass/Fail Criteria**: Steps 1 and 3 return VOR_OK with bearing within ±0.1°
of 45.0°. Step 2 returns VOR_ERR_SNR with no bearing output.
```

### Error handling

```markdown
## TST-NAV-042-007: VOR Bearing Robustness — Invalid Inputs

@test    TST-NAV-042-007
@req     HLR-NAV-044
@type    Robustness / Error
@dal     C
@status  DRAFT

**Objective**: Verify defensive behaviour for invalid input parameters.

| Step | iq_samples | sample_count | Expected Return |
|------|-----------|--------------|-----------------|
| 1    | NULL      | 30           | VOR_ERR_INPUT   |
| 2    | valid     | 0            | VOR_ERR_INPUT   |
| 3    | valid     | MAX+1        | VOR_ERR_INPUT   |
| 4    | valid     | 30           | VOR_OK          |

**Pass/Fail Criteria**: Steps 1–3 return VOR_ERR_INPUT without processing.
Step 4 returns VOR_OK. No undefined behaviour in any case.
```

---

## Workflow 4 — Perform change impact analysis

Required before any modification to a baselined artifact. The analysis is the deliverable; the
edit happens after it is approved.

1. **Identify the change** and its CR/PR number.
2. **Trace forward** — which design elements, code modules, and test cases implement the changed
   requirement?
3. **Trace backward** — which system requirements flow into it? Are they changing too?
4. **Assess lateral impact** — which requirements at the same level share data, interfaces, or
   resources? This is the direction people miss.
5. **Assess safety impact** — does failure condition severity change? Could this introduce a new
   failure mode? Does it touch a derived requirement?
6. **Determine regression scope** — at minimum every test traced to the changed requirement, plus
   tests for requirements sharing interfaces with the changed area.
7. **Document it.**

```markdown
## CIA-NAV-2026-017: Change Impact Analysis

@cr CR-NAV-2026-017
@baseline BL-NAV-REQ-003

**Change Description**: Modify HLR-NAV-042 to tighten bearing accuracy from
±0.1° to ±0.05° at SNR ≥ 25 dB.

**Upstream Impact**: SYS-NAV-018 updated to reflect tighter accuracy. System
safety assessment unchanged — failure condition remains Major.

**Downstream Impact**:
- DES-NAV-012: algorithm may require higher-precision arithmetic. REVIEW REQUIRED.
- vor_bearing.c: may need double precision or a Q-format change. REWORK LIKELY.
- TST-NAV-042-001..008: all tolerances change. RE-EXECUTE ALL.
- TST-NAV-042-005: SNR threshold moves 20 → 25 dB. REWRITE.

**Lateral Impact**:
- HLR-NAV-043 (SNR threshold): threshold value changes. MUST UPDATE.
- HLR-NAV-050 (DME coupling): no impact — independent data path.

**Safety Impact**: No new failure mode. Accuracy improvement reduces risk. The
SNR threshold increase may reduce availability in marginal signal conditions —
flagged for operational assessment.

**Regression Scope**: Full VOR bearing suite (TST-NAV-042-*). Partial navigation
integration tests (TST-NAV-INT-010, 011, 015).
```

---

## Workflow 5 — Evaluate a COTS component (DO-278A)

1. **Determine the target AL** the component must satisfy in its intended function.
2. **Gap analysis** against the objectives for that AL: requirements documentation, design or
   architecture description, test procedures and results, CM process, defect and patch history.
3. **Evaluate service experience** using the CAST-1 attributes: deployment duration and breadth,
   problem report history and resolution rate, configuration stability, and similarity of the
   fielded environment to the intended use.
4. **Identify gaps and mitigations** — missing vendor evidence → integrator testing; no source
   access → black-box requirements-based testing plus monitoring wrappers; unknown internals →
   defensive architecture with partitioning, watchdogs, graceful degradation.
5. **Build the assurance case** as claims / arguments / evidence, with evidence naming specific
   documents, test results, and operational data.
6. **Document Alternate Means of Compliance** where objectives cannot be met conventionally, and
   agree them with the authority early rather than at the final review.

---

## Workflow 6 — Assess DO-330 tool qualification need

1. **Classify the tool's role**:
   - Output becomes part of the deliverable → **Criterion 1**
   - Automates verification, and its output justifies eliminating or reducing another process →
     **Criterion 2**
   - Could fail to detect an error within its intended use → **Criterion 3**
   - Convenience only, output independently verified → **no qualification needed**
2. **Determine TQL** from the criterion × DAL matrix in `competencies.md`.
3. **Choose an approach**: full DO-330 qualification; compensating verification (verify all tool
   output independently, claim no process credit); or a combination.
4. **For AI coding agents**: Criterion 1, which at DAL A implies TQL-1 and is not achievable for
   a non-deterministic tool. Use compensating verification — all agent output treated as
   untrusted developer output under 100% normal verification, no process eliminated, no credit
   claimed, qualification not triggered. This argument depends on the practice actually matching
   it; if review starts getting skipped because the agent "already checked", the tool has taken
   process credit and the question reopens.
