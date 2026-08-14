## HLR-NAV-044: VOR Input Parameter Validation

@req HLR-NAV-044
@parent SYS-NAV-021
@al 3
@status BASELINED
@baseline BL-NAV-REQ-003

**Shall Statement**: The software shall validate all input parameters to the VOR bearing
calculation before processing, and shall return an input error status without processing
when any parameter is invalid.

**Conditions**:
- Null pointer for the sample buffer or the output parameter is invalid
- A sample count of zero is invalid
- A sample count exceeding MAX_VOR_SAMPLES is invalid

**Derived Requirements**: None identified.

**Safety**: Unvalidated input could cause an out-of-bounds read and an unhandled fault in
a continuously available ground system.
