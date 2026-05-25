"""L_eq,bnd boundary computation."""
from costryx_leq.extractor import lambda_em

def leq_bnd_from_lambda(f: float, eps_eff: float = 3.5, ratio: float = 5.0) -> float:
    """Compute L_eq,bnd at frequency f using lambda_EM/ratio rule."""
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    return float(lambda_em(f, eps_eff) / ratio)

