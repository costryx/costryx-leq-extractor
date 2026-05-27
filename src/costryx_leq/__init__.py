"""Official Reference Implementation of the Equivalent Spatial Length framework.

This is the costryx-leq-extractor package — the canonical open-source
reference implementation supporting the Costryx three-layer IP architecture:

  Layer 1 (Paper):    V4.0 Working Report — 10.5281/zenodo.20382496
  Layer 2 (Software): This package v0.1.0  — 10.5281/zenodo.20384916
  Layer 3 (API):      OpenAPI 3.1 v1.2.0   — 10.5281/zenodo.20405124

The public Zenodo release (v0.1.0) is the immutable, citable reference
snapshot aligned with the V4.0 paper. Active development continues under
the V3.5 internal series on the GitHub `main` branch.

Quick reference:
    >>> import costryx_leq
    >>> costryx_leq.__version__
    '0.1.0'
    >>> costryx_leq.__software_doi__
    '10.5281/zenodo.20384916'
    >>> costryx_leq.__paper_doi__
    '10.5281/zenodo.20382496'
"""
from costryx_leq.extractor import extract_leq, AnchorAssignment, lambda_em
from costryx_leq.continuous import extract_leq_spectrum
from costryx_leq.gci import compute_gci, classify_decision_band
from costryx_leq.boundary import leq_bnd_from_lambda
from costryx_leq.uncertainty import sigma_leq, classify_gum_components, expanded_uncertainty
from costryx_leq.mhl import compute_mhl_hash, verify_mhl_hash, MHLBundle
from costryx_leq.visualization import (
    plot_leq_spectrum_standard,
    COSTRYX_COLOR_GREEN,
    COSTRYX_COLOR_YELLOW,
    COSTRYX_COLOR_RED,
)

# ─────────────────────────────────────────────────────────────────
# Package metadata
# ─────────────────────────────────────────────────────────────────
__version__ = "0.1.0"
__dev_series__ = "V3.5"
__variant__ = "foundational"
__status__ = "stable-with-active-development"

# ─────────────────────────────────────────────────────────────────
# Author & licensing
# ─────────────────────────────────────────────────────────────────
__author__ = "Chin-Yu Hsu"
__email__ = "chinyu@costryx.net"
__orcid__ = "https://orcid.org/0009-0009-6267-7897"
__license__ = "Apache-2.0"

# ─────────────────────────────────────────────────────────────────
# DOI references (Costryx three-layer IP architecture)
# ─────────────────────────────────────────────────────────────────
# Layer 1 — V4.0 Working Report (the methodology)
__paper_doi__ = "10.5281/zenodo.20382496"
__paper_concept_doi__ = "10.5281/zenodo.20382495"
__paper_url__ = "https://doi.org/10.5281/zenodo.20382496"

# Layer 2 — Reference Software (this package)
__software_doi__ = "10.5281/zenodo.20384916"
__software_url__ = "https://doi.org/10.5281/zenodo.20384916"

# Layer 3 — Enterprise API Contract
__api_doi__ = "10.5281/zenodo.20405124"
__api_concept_doi__ = "10.5281/zenodo.20405123"
__api_viewer_url__ = "https://costryx.github.io/costryx-leq-extractor/api-viewer/"

# Default __doi__ refers to this software (per Python community convention)
__doi__ = __software_doi__

__all__ = [
    # Core extraction
    "extract_leq", "extract_leq_spectrum", "AnchorAssignment", "lambda_em",
    # GCI
    "compute_gci", "classify_decision_band",
    # Boundary
    "leq_bnd_from_lambda",
    # Uncertainty (GUM)
    "sigma_leq", "classify_gum_components", "expanded_uncertainty",
    # MHL (manifest hash)
    "compute_mhl_hash", "verify_mhl_hash", "MHLBundle",
    # Visualization
    "plot_leq_spectrum_standard",
    "COSTRYX_COLOR_GREEN", "COSTRYX_COLOR_YELLOW", "COSTRYX_COLOR_RED",
]
