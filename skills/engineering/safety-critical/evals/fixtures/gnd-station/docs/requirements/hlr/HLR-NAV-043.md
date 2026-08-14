## HLR-NAV-043: VOR Signal Quality Rejection

@req HLR-NAV-043
@parent SYS-NAV-018
@al 3
@status BASELINED
@baseline BL-NAV-REQ-003

**Shall Statement**: The software shall reject VOR bearing calculations when the received
signal-to-noise ratio is below 20 dB, and shall report a signal quality error to the caller.

**Conditions**:
- SNR estimated over the full sample buffer presented to the calculation
- Rejection reported as return status, no bearing value written

**Boundary Conditions**:
- SNR exactly 20.0 dB shall be accepted
- SNR of 19.9 dB shall be rejected

**Derived Requirements**: None identified.

**Safety**: Accepting a bearing derived from a degraded signal could present an erroneous
bearing to the approach controller without any indication of reduced confidence.
