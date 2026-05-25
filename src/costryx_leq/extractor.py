"""Three-anchor L_eq extraction."""
from dataclasses import dataclass
from typing import Tuple
import numpy as np

C_VACUUM = 2.998e8

@dataclass(frozen=True)
class AnchorAssignment:
    """Three-anchor operating structure."""
    OP1: Tuple[float, float] = (64.0e9, 0.50e-3)
    OP2: Tuple[float, float] = (96.0e9, 0.35e-3)
    OP3: Tuple[float, float] = (128.0e9, 0.25e-3)

    def as_list(self):
        return [self.OP1, self.OP2, self.OP3]

def lambda_em(f, eps_eff: float = 3.5):
    """Equivalent EM wavelength in DUT dielectric."""
    f = np.asarray(f, dtype=float)
    if np.any(f <= 0):
        raise ValueError("frequency must be positive")
    if eps_eff <= 0:
        raise ValueError("eps_eff must be positive")
    return C_VACUUM / (f * np.sqrt(eps_eff))

def _mixed_mode_scd21(s_params):
    """Return differential/common-to-differential transfer term.

    For 2-port objects, returns S21 directly. For 4-port scikit-rf Networks,
    converts single-ended data to generalized mixed-mode and returns CD21.
    """
    if getattr(s_params, 'nports', None) == 2:
        return s_params.s[:, 1, 0]
    if getattr(s_params, 'nports', None) != 4:
        raise ValueError(f"Expected 2- or 4-port network; got {getattr(s_params, 'nports', None)}-port.")
    mm = s_params.copy()
    mm.se2gmm(p=2)
    return mm.s[:, 2, 0]

def extract_leq(s_params, f_k: float, eps_eff: float = 3.5, geom_phase_rad: float = 0.0) -> float:
    """Extract Equivalent Spatial Length L_eq at anchor frequency f_k."""
    f_array = np.asarray(s_params.f, dtype=float)
    if not (f_array.min() <= f_k <= f_array.max()):
        raise ValueError(f"Anchor f_k={f_k:.2e} Hz outside data range [{f_array.min():.2e}, {f_array.max():.2e}] Hz.")
    idx = int(np.argmin(np.abs(f_array - f_k)))
    scd21 = _mixed_mode_scd21(s_params)
    phase_unwrapped = np.unwrap(np.angle(scd21))
    phi_resid = phase_unwrapped[idx] - geom_phase_rad
    return float(phi_resid / (2.0 * np.pi) * lambda_em(f_k, eps_eff))
