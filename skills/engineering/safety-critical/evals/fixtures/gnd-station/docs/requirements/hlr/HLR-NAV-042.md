## HLR-NAV-042: VOR Bearing Calculation Accuracy

@req HLR-NAV-042
@parent SYS-NAV-018
@al 3
@status BASELINED
@baseline BL-NAV-REQ-003

**Shall Statement**: The software shall calculate VOR magnetic bearing with an accuracy of
±0.1 degrees when the received signal-to-noise ratio is ≥ 20 dB.

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

**Derived Requirements**: None identified.

**Safety**: Incorrect bearing could contribute to an approach sequencing error.
Failure condition severity per SYS-NAV-018 → Major → AL3.
