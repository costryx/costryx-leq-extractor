"""Closed-form σ_Leq uncertainty propagation (§V.F, §V.F.1)."""
from typing import Dict, Tuple
import numpy as np

from costryx_leq.extractor import lambda_em


def sigma_leq(f: float,
              sigma_U1_deg: float, sigma_U2_deg: float,
              sigma_U3_deg: float, sigma_U4_deg: float,
              sigma_U5_deg: float, eps_eff: float = 3.5) -> float:
    """
    σ_Leq(f) = λ_EM(f)/(2π) · √(ΣᵢσUiÂ²)                  (§V.F)

    All σUi inputs are in DEGREES; converted internally to radians.

    Returns σ_Leq in meters.
    """
    sigmas_rad = np.deg2rad([sigma_U1_deg, sigma_U2_deg, sigma_U3_deg,
                             sigma_U4_deg, sigma_U5_deg])
    rss_rad = float(np.sqrt(np.sum(sigmas_rad ** 2)))
    return float(lambda_em(f, eps_eff) / (2.0 * np.pi) * rss_rad)


def classify_gum_components() -> Dict[str, str]:
    """GUM Type A / Type B classification (§V.F.1)."""
    return {
        "U1_VNA_dynamic_range":           "Type B",
        "U2_calkit_characterization":      "Type B",
        "U3_cable_phase_stability":        "Type B",
        "U4_probe_contact_repeatability":  "Type A",
        "U5_ambient_temperature_drift":    "Type B",
    }


def expanded_uncertainty(sigma_leq_value: float, k: float = 2.0) -> float:
    """
    Expanded uncertainty U = k · σ_Leq.

    Default k=2 corresponds to ~95% confidence interval (§V.F.1).
    """
    return float(k * sigma_leq_value)
