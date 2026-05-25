"""Continuous-spectrum L_eq(f) extractor — strategic core of v0.1.0."""
from typing import Dict, Optional
import numpy as np

from costryx_leq.extractor import _mixed_mode_scd21, lambda_em


def extract_leq_spectrum(s_params, f_min: float = 110e9,
                         f_max: float = 220e9, eps_eff: float = 3.5,
                         geom_phase_rad: Optional[np.ndarray] = None,
                         ) -> Dict[str, np.ndarray]:
    """
    Extract continuous L_eq(f) spectrum across a frequency band.

    This is the **foundational continuous-spectrum extractor**. Thermal
    drift separation (BQSGO) is NOT applied — for that, see the
    forthcoming companion publication.

    Args:
        s_params: scikit-rf Network (post-AFR).
        f_min, f_max: frequency band of interest, Hz.
        eps_eff: effective dielectric constant of DUT.
        geom_phase_rad: optional array of known geometric phase per
            frequency point (length must match the band slice).

    Returns:
        dict with keys:
            "frequency" : frequency points in Hz, shape (N,)
            "L_eq"      : extracted L_eq in meters, shape (N,)
            "phi_resid" : residual phase in radians, shape (N,)
            "lambda_EM" : EM wavelength in meters, shape (N,)
    """
    f = np.asarray(s_params.f, dtype=float)
    mask = (f >= f_min) & (f <= f_max)
    if not mask.any():
        raise ValueError(
            f"No data in band [{f_min:.2e}, {f_max:.2e}] Hz."
        )

    f_band = f[mask]
    scd21 = _mixed_mode_scd21(s_params)
    phase_unwrapped = np.unwrap(np.angle(scd21))[mask]

    if geom_phase_rad is None:
        geom_phase_rad = np.zeros_like(phase_unwrapped)
    geom_phase_rad = np.asarray(geom_phase_rad, dtype=float)
    if geom_phase_rad.shape != phase_unwrapped.shape:
        raise ValueError("geom_phase_rad shape mismatch with band slice.")

    phi_resid = phase_unwrapped - geom_phase_rad
    lam = lambda_em(f_band, eps_eff)
    leq = phi_resid / (2.0 * np.pi) * lam

    return {
        "frequency": f_band,
        "L_eq": leq,
        "phi_resid": phi_resid,
        "lambda_EM": lam,
    }

