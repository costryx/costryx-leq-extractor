"""Geometric Convergence Index (GCI)."""
from typing import List
from costryx_leq.extractor import AnchorAssignment

def compute_gci(leq_values: List[float], anchors: AnchorAssignment) -> float:
    """Compute max-ratio GCI across OP-1/OP-2/OP-3."""
    if len(leq_values) != 3:
        raise ValueError("Expected exactly 3 L_eq values (OP-1/OP-2/OP-3).")
    bnds = [anchors.OP1[1], anchors.OP2[1], anchors.OP3[1]]
    ratios = [abs(l) / b for l, b in zip(leq_values, bnds)]
    return float(max(ratios))

def classify_decision_band(gci: float) -> str:
    """Classify GCI into satisfied, boundary_zone, or design_correction_required."""
    if gci <= 1.0:
        return "satisfied"
    if gci <= 1.5:
        return "boundary_zone"
    return "design_correction_required"

