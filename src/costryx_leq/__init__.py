"""
costryx-leq-extractor
=====================

Official Reference Implementation of the Equivalent Spatial Length
(L_eq) extraction framework for sub-THz interconnect channel validation.

Reference:
    Hsu, C.-Y. (2026). 256 GT/s PAM4 Channel Validation Under a Fixed
    Reference Plane (V3.6). TechRxiv. DOI: [pending].

Scope: foundational L_eq + GCI + MHL extraction only.
       BQSGO, CBC, and OP-2/OP-3 calibration sequences are NOT included.
"""

from costryx_leq.extractor import extract_leq, AnchorAssignment, lambda_em
from costryx_leq.continuous import extract_leq_spectrum
from costryx_leq.gci import compute_gci, classify_decision_band
from costryx_leq.boundary import leq_bnd_from_lambda
from costryx_leq.uncertainty import (
    sigma_leq, classify_gum_components, expanded_uncertainty,
)
from costryx_leq.mhl import compute_mhl_hash, MHLBundle
from costryx_leq.visualization import (
    plot_leq_spectrum_standard, COSTRYX_COLOR_GREEN,
    COSTRYX_COLOR_YELLOW, COSTRYX_COLOR_RED,
)

__version__ = "0.1.0-foundational"
__author__ = "Chin-Yu Hsu"
__license__ = "Apache-2.0"
__doi__ = "10.5281/zenodo.PENDING"

import warnings
warnings.warn(
    "costryx-leq-extractor v{} loaded. "
    "If you use this software, please cite Hsu, C.-Y. (2026), "
    "TechRxiv DOI: 10.36227/techrxiv.PENDING. "
    "See https://github.com/costryx/costryx-leq-extractor#citation"
    .format(__version__),
    stacklevel=2,
)

__all__ = [
    "extract_leq", "extract_leq_spectrum", "AnchorAssignment",
    "lambda_em", "compute_gci", "classify_decision_band",
    "leq_bnd_from_lambda", "sigma_leq", "classify_gum_components",
    "expanded_uncertainty", "compute_mhl_hash", "MHLBundle",
    "plot_leq_spectrum_standard",
    "COSTRYX_COLOR_GREEN", "COSTRYX_COLOR_YELLOW", "COSTRYX_COLOR_RED",
]

