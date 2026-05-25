"""L_eq,bnd boundary computation.

This module implements only the public λ_EM/ratio boundary rule.
It does not implement OP-2/OP-3 calibration-sequence algorithms.
"""

from typing import Dict
import numpy as np

from costryx_leq.extractor import AnchorAssignment, lambda_em


def leq_bnd_from_lambda(
    f,
    eps_eff: float = 3.5,
    ratio: float = 5.0,
):
    """Compute L_eq,bnd from the public λ_EM/ratio rule.

    Args:
        f: Frequency in Hz, scalar or numpy-compatible array.
        eps_eff: Effective dielectric constant.
        ratio: Boundary divisor. Default 5.0 corresponds to λ_EM/5.

    Returns:
        L_eq,bnd in meters, scalar or numpy array matching f.
    """
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    return lambda_em(f, eps_eff) / ratio


def leq_bnd_spectrum(
    frequency_hz,
    eps_eff: float = 3.5,
    ratio: float = 5.0,
) -> Dict[str, np.ndarray]:
    """Compute L_eq,bnd(f) across a frequency array.

    This is a convenience wrapper for plotting or comparing
    continuous-spectrum L_eq(f) against the public λ_EM/ratio boundary.
    """
    frequency_hz = np.asarray(frequency_hz, dtype=float)
    if frequency_hz.ndim != 1:
        raise ValueError("frequency_hz must be a one-dimensional array")
    return {
        "frequency": frequency_hz,
        "L_eq_bnd": np.asarray(leq_bnd_from_lambda(frequency_hz, eps_eff, ratio)),
        "eps_eff": np.asarray([eps_eff]),
        "ratio": np.asarray([ratio]),
    }


def op_anchor_boundaries(
    anchors: AnchorAssignment | None = None,
) -> Dict[str, float]:
    """Return declared OP-1/OP-2/OP-3 anchor boundary values in meters.

    These values are declaration-level anchor boundaries and do not
    disclose instrument-specific OP-2/OP-3 calibration sequences.
    """
    anchors = anchors or AnchorAssignment()
    return {
        "OP1": anchors.OP1[1],
        "OP2": anchors.OP2[1],
        "OP3": anchors.OP3[1],
    }

