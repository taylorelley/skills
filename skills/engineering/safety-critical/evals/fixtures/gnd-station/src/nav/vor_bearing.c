/**
 * @file    vor_bearing.c
 * @brief   VOR magnetic bearing calculation module
 *
 * @req     HLR-NAV-042, HLR-NAV-043, HLR-NAV-044
 * @design  DES-NAV-012
 * @al      3
 * @status  BASELINED
 * @baseline BL-NAV-CODE-002
 *
 * Copyright (c) 2026 Airways Ground Systems. All rights reserved.
 * CONFIDENTIAL — Company Confidential
 */

#include "vor_bearing.h"
#include "math_utils.h"
#include "signal_proc.h"
#include "site_config.h"

#define VOR_MIN_SNR_DB    (20.0F)
#define MAX_VOR_SAMPLES   (256U)

static float last_snr_db = 0.0F;

/**
 * @brief   Apply the site-specific magnetic station declination bias
 *
 * @param[in] raw_bearing  Uncorrected bearing in degrees [0.0, 360.0)
 * @return  Bearing corrected for the configured station declination
 */
static float vor_apply_station_bias(float raw_bearing)
{
    const float declination = site_config_get_declination_deg();
    return raw_bearing + declination;
}

/**
 * @brief   Calculate VOR magnetic bearing from I/Q samples
 * @req     HLR-NAV-042
 * @design  DES-NAV-012
 *
 * @param[in]  iq_samples    Pointer to I/Q sample buffer (30 Hz)
 * @param[in]  sample_count  Number of samples in buffer
 * @param[out] bearing_deg   Calculated bearing in degrees magnetic [0.0, 360.0)
 * @return  VOR_OK on success, VOR_ERR_SNR if SNR < 20 dB, VOR_ERR_INPUT if invalid params
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

    /* @req HLR-NAV-042: Calculate bearing with +/-0.1 deg accuracy */
    float raw_bearing = vor_phase_extract(iq_samples, sample_count);

    raw_bearing = vor_apply_station_bias(raw_bearing);

    *bearing_deg = math_normalize_angle(raw_bearing);

    last_snr_db = snr_db;

    return VOR_OK;
}

/**
 * @brief   Return the SNR estimate from the most recently accepted bearing calculation
 * @req     HLR-NAV-045
 *
 * @return  SNR in dB from the last successful call to vor_calculate_bearing()
 */
float vor_get_last_snr_db(void)
{
    return last_snr_db;
}
