import hashlib

import numpy as np

from costryx_leq import (
    AnchorAssignment,
    compute_gci,
    compute_mhl_hash,
    extract_leq,
    extract_leq_spectrum,
    lambda_em,
    sigma_leq,
)


class SyntheticNetwork:
    nports = 2

    def __init__(self):
        self.f = np.linspace(50e9, 220e9, 401)
        phase = 0.20 * np.sin(
            (self.f - self.f.min()) / (self.f.max() - self.f.min()) * np.pi
        )
        s21 = np.exp(1j * phase)
        self.s = np.zeros((len(self.f), 2, 2), dtype=complex)
        self.s[:, 1, 0] = s21
        self.s[:, 0, 1] = s21


def test_lambda_em_positive():
    lam = lambda_em(128e9, eps_eff=3.5)
    assert lam > 0


def test_three_anchor_extraction_and_gci():
    ntwk = SyntheticNetwork()
    anchors = AnchorAssignment()

    leq_values = [
        extract_leq(ntwk, f_k=anchors.OP1[0], eps_eff=3.5),
        extract_leq(ntwk, f_k=anchors.OP2[0], eps_eff=3.5),
        extract_leq(ntwk, f_k=anchors.OP3[0], eps_eff=3.5),
    ]

    gci = compute_gci(leq_values, anchors)

    assert len(leq_values) == 3
    assert np.all(np.isfinite(leq_values))
    assert gci >= 0


def test_continuous_spectrum_extraction():
    ntwk = SyntheticNetwork()
    spectrum = extract_leq_spectrum(ntwk, f_min=110e9, f_max=220e9)

    assert "frequency" in spectrum
    assert "L_eq" in spectrum
    assert "phi_resid" in spectrum
    assert "lambda_EM" in spectrum
    assert len(spectrum["frequency"]) > 0
    assert spectrum["frequency"].min() >= 110e9
    assert spectrum["frequency"].max() <= 220e9
    assert np.all(np.isfinite(spectrum["L_eq"]))


def test_mhl_hash_matches_sha256_reference():
    observed = compute_mhl_hash(b"a", b"b", b"c", b"d")
    expected = hashlib.sha256(b"abcd").hexdigest()

    assert observed == expected
    assert len(observed) == 64


def test_sigma_leq_positive():
    sigma = sigma_leq(
        128e9,
        sigma_U1_deg=1.0,
        sigma_U2_deg=1.0,
        sigma_U3_deg=1.0,
        sigma_U4_deg=1.0,
        sigma_U5_deg=1.0,
        eps_eff=3.5,
    )

    assert sigma > 0
