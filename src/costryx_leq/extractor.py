"""Three-anchor L_eq extraction (§III, §V.A of source paper)."""
from dataclasses import dataclass
from typing import Tuple
import numpy as np

C_VACUUM = 2.998e8  # m/s


@dataclass(frozen=True)
class AnchorAssignment:
    """Three-anchor operating structure per §V.A."""
    OP1: Tuple[float, float] = (64.0e9, 0.50e-3)   # (f_k [Hz], L_eq,bnd [m])
    OP2: Tuple[float, float] = (96.0e9, 0.35e-3)
    OP3: Tuple[float, float] = (128.0e9, 0.25e-3)

    def as_list(self):
        return [self.OP1, self.OP2, self.OP3]


def lambda_em(f, eps_eff: float = 3.5):
    """
    Equivalent EM wavelength in DUT dielectric.

        λ_EM(f) = c / (f · √ε_eff)         (§III)

    Args:
        f: frequency in Hz (scalar or numpy array).
        eps_eff: effective dielectric constant (default 3.5).

    Returns:
        wavelength in meters.
    """
    f = np.asarray(f, dtype=float)
    return C_VACUUM / (f * np.sqrt(eps_eff))


def _mixed_mode_scd21(s_params):
    """
    Convert 4-port single-ended S-parameters to mixed-mode and return SCD21.

    Standard mixed-mode transformation; common-to-differential conversion
    follows the convention of Eisenstadt & Eo (1992). For 2-port single-mode
    measurements, the differential-mode S21 is returned directly.
    """
    import skrf as rf

    if s_params.nports == 2:
        return s_params.s[:, 1, 0]

    if s_params.nports != 4:
        raise ValueError(
            f"Expected 2- or 4-port network; got {s_params.nports}-port."
        )

    mm = s_params.copy()
    mm.se2gmm(p=2)  # convert single-ended to generalized mixed-mode
    return mm.s[:, 2, 0]   # CD21 in standard mixed-mode ordering


def extract_leq(s_params, f_k: float, eps_eff: float = 3.5,
                geom_phase_rad: float = 0.0) -> float:
    """
    Extract Equivalent Spatial Length L_eq at anchor frequency f_k.

        L_eq(f_k) = φ_resid(f_k) / (2π) · λ_EM(f_k)        (§III)

    NOTE: this function assumes that AFR de-embedding (T-3 of §V.C)
    has been applied externally; `s_params` should be post-AFR data.

    Args:
        s_params: scikit-rf Network (Touchstone 2.1, 2-port or 4-port).
        f_k: anchor frequency in Hz (e.g., 64e9, 96e9, 128e9).
        eps_eff: effective dielectric constant of DUT.
        geom_phase_rad: known geometric propagation phase to subtract.

    Returns:
        L_eq in meters.
    """
    f_array = np.asarray(s_params.f, dtype=float)
    if not (f_array.min() <= f_k <= f_array.max()):
        raise ValueError(
            f"Anchor f_k={f_k:.2e} Hz outside data range "
            f"[{f_array.min():.2e}, {f_array.max():.2e}] Hz."
        )

    idx = int(np.argmin(np.abs(f_array - f_k)))
    scd21 = _mixed_mode_scd21(s_params)
    phase_unwrapped = np.unwrap(np.angle(scd21))
    phi_resid = phase_unwrapped[idx] - geom_phase_rad
    return float(phi_resid / (2.0 * np.pi) * lambda_em(f_k, eps_eff))
