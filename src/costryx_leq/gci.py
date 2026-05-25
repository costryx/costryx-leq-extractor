"""Geometric Convergence Index (GCI) per §III.A, Eq. 3-1."""
from typing import List, Tuple
import numpy as np

from costryx_leq.extractor import AnchorAssignment


def compute_gci(leq_values: List[float],
                anchors: AnchorAssignment) -> float:
    """
    Compute GCI = max{ L_eq(f_k) / L_eq,bnd(f_k), k=1,2,3 }   (Eq. 3-1)

    Args:
        leq_values: [L_eq(OP1), L_eq(OP2), L_eq(OP3)] in meters.
        anchors: AnchorAssignment instance.

    Returns:
        GCI scalar (dimensionless).
    """
    if len(leq_values) != 3:
        raise ValueError("Expected exactly 3 L_eq values (OP-1/OP-2/OP-3).")
    bnds = [anchors.OP1[1], anchors.OP2[1], anchors.OP3[1]]
    ratios = [abs(l) / b for l, b in zip(leq_values, bnds)]
    return float(max(ratios))


def classify_decision_band(gci: float) -> str:
    """
    Classify GCI per §V.E boundary decision criteria:

        GCI ≤ 1.0  →  "satisfied"
        1.0 < GCI ≤ 1.5  →  "boundary_zone"
        GCI > 1.5  →  "design_correction_required"
    """
    if gci <= 1.0:
        return "satisfied"
    if gci <= 1.5:
        return "boundary_zone"
    return "design_correction_required"
