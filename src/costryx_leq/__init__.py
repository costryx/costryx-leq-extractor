"""Official Reference Implementation of the Equivalent Spatial Length framework."""
from costryx_leq.extractor import extract_leq, AnchorAssignment, lambda_em
from costryx_leq.continuous import extract_leq_spectrum
from costryx_leq.gci import compute_gci, classify_decision_band
from costryx_leq.boundary import leq_bnd_from_lambda
from costryx_leq.uncertainty import sigma_leq, classify_gum_components, expanded_uncertainty
from costryx_leq.mhl import compute_mhl_hash, verify_mhl_hash, MHLBundle
from costryx_leq.visualization import plot_leq_spectrum_standard, COSTRYX_COLOR_GREEN, COSTRYX_COLOR_YELLOW, COSTRYX_COLOR_RED

__version__ = "0.1.0"
__variant__ = "foundational"
__author__ = "Chin-Yu Hsu"
__license__ = "Apache-2.0"
__doi__ = "10.5281/zenodo.20382496"
__concept_doi__ = "10.5281/zenodo.20382495"
__paper_url__ = "https://doi.org/10.5281/zenodo.20382496"

__all__ = [
    "extract_leq", "extract_leq_spectrum", "AnchorAssignment", "lambda_em",
    "compute_gci", "classify_decision_band", "leq_bnd_from_lambda",
    "sigma_leq", "classify_gum_components", "expanded_uncertainty",
    "compute_mhl_hash", "verify_mhl_hash", "MHLBundle",
    "plot_leq_spectrum_standard", "COSTRYX_COLOR_GREEN", "COSTRYX_COLOR_YELLOW", "COSTRYX_COLOR_RED",
]


