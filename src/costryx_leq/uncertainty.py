"""Closed-form sigma_Leq uncertainty propagation."""
from typing import Dict
import numpy as np
from costryx_leq.extractor import lambda_em

def sigma_leq(f: float, sigma_U1_deg: float, sigma_U2_deg: float, sigma_U3_deg: float, sigma_U4_deg: float, sigma_U5_deg: float, eps_eff: float = 3.5) -> float:
    """Compute sigma_Leq from five degree-valued phase uncertainty terms."""
    sigmas_rad = np.deg2rad([sigma_U1_deg, sigma_U2_deg, sigma_U3_deg, sigma_U4_deg, sigma_U5_deg])
    rss_rad = float(np.sqrt(np.sum(sigmas_rad ** 2)))
    return float(lambda_em(f, eps_eff) / (2.0 * np.pi) * rss_rad)

def classify_gum_components() -> Dict[str, str]:
    """Return GUM Type A / Type B classification."""
    return {
        "U1_VNA_dynamic_range": "Type B",
        "U2_calkit_characterization": "Type B",
        "U3_cable_phase_stability": "Type B",
        "U4_probe_contact_repeatability": "Type A",
        "U5_ambient_temperature_drift": "Type B",
    }

def expanded_uncertainty(sigma_leq_value: float, k: float = 2.0) -> float:
    """Expanded uncertainty U = k * sigma_Leq."""
    return float(k * sigma_leq_value)
