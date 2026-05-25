"""L_eq,bnd boundary computation (§V.A: λ_EM/5 physical robustness)."""
from costryx_leq.extractor import lambda_em


def leq_bnd_from_lambda(f: float, eps_eff: float = 3.5,
                        ratio: float = 5.0) -> float:
    """
    Compute L_eq,bnd at frequency f using λ_EM/ratio rule (§V.A).

    Default ratio = 5 corresponds to ±π/5 phase margin of the four-level
    PAM4 voltage structure.

    Args:
        f: frequency in Hz.
        eps_eff: effective dielectric constant (default 3.5).
        ratio: divisor (default 5.0).

    Returns:
        L_eq,bnd in meters.
    """
    return float(lambda_em(f, eps_eff) / ratio)
