# costryx-leq-extractor
[![Python tests](https://github.com/costryx/costryx-leq-extractor/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/costryx/costryx-leq-extractor/actions/workflows/python-tests.yml)

[![DOI](https://img.shields.io/badge/DOI-pending-blue.svg)](https://doi.org/10.36227/techrxiv.PENDING)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-foundational--reference-orange.svg)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()

Official Reference Implementation of the Equivalent Spatial Length (L_eq) extraction framework for sub-THz interconnect channel validation.

This repository implements the foundational extractor disclosed in:

> Hsu, C.-Y. (2026). *256 GT/s PAM4 Channel Validation Under a Fixed Reference Plane: Differential-Mode Phase-Residual Analytical Theory of Equivalent Spatial Length and Its Application to Sub-THz Interconnect Characterization* (V3.6). TechRxiv. DOI: [pending].

---

## 🎯 Scope of This Repository

This is the foundational reference implementation covering:

| Capability | Status |
|---|---|
| L_eq(f_k) three-anchor extraction (§III) | ✅ Implemented |
| L_eq(f) continuous-spectrum extraction | ✅ Implemented |
| GCI = max{ L_eq / L_eq,bnd } decision indicator (§III.A) | ✅ Implemented |
| σ_Leq RSS uncertainty propagation (§V.F) | ✅ Implemented |
| MHL SHA-256 hash chain (§VI.A, Eq. 6-1) | ✅ Implemented |
| Standard L_eq(f) spectrum visualization | ✅ Implemented |
| BQSGO thermal-drift separation | ❌ Out of scope |
| CBC under non-ideal SCD21 profiles | ❌ Out of scope |
| OP-2/OP-3 calibration-sequence algorithms | ❌ Out of scope |

> See [`docs/DISCLOSURE_BOUNDARY.md`](docs/DISCLOSURE_BOUNDARY.md) for explicit disclosure boundary.
> Items marked ❌ are reserved for a coordinated companion publication and are NOT included here.

---

## 🚀 Quick Start

```bash
git clone https://github.com/costryx/costryx-leq-extractor.git
cd costryx-leq-extractor
pip install -e .
```

```python
import skrf as rf
from costryx_leq import (
    extract_leq,
    extract_leq_spectrum,
    compute_gci,
    AnchorAssignment,
    plot_leq_spectrum_standard,
)

ntwk = rf.Network("examples/synthetic_dut_256GTs.s4p")
anchors = AnchorAssignment()  # OP-1: 64 GHz, OP-2: 96 GHz, OP-3: 128 GHz

leq_op1 = extract_leq(ntwk, f_k=anchors.OP1[0], eps_eff=3.5)
leq_op2 = extract_leq(ntwk, f_k=anchors.OP2[0], eps_eff=3.5)
leq_op3 = extract_leq(ntwk, f_k=anchors.OP3[0], eps_eff=3.5)

gci = compute_gci([leq_op1, leq_op2, leq_op3], anchors)

spectrum = extract_leq_spectrum(ntwk, f_min=110e9, f_max=220e9)
plot_leq_spectrum_standard(
    spectrum,
    anchors,
    title="DUT Continuous L_eq(f) Spectrum",
)
```

---

## 📐 Methodology Reference

The four-step reference-plane transfer protocol (§V.C of the source paper) is:

```text
T-1: TRL calibration
T-2: SOLT/LRRM
T-3: AFR (IEEE 370 §5)
T-4: TDR
```

This package assumes T-1 through T-4 have been completed externally prior to invocation. The extractor operates on the post-de-embedded S-parameter file (Touchstone 2.1, `.s2p` or `.s4p`).

For AFR de-embedding, we recommend the open-source `scikit-rf` implementation of IEEE 370 §5.

---

## 📚 Citation

If you use this software, please cite both the methodology paper and this repository.

```bibtex
@article{Hsu2026Leq256,
  author  = {Hsu, Chin-Yu},
  title   = {256 GT/s PAM4 Channel Validation Under a Fixed Reference Plane: Differential-Mode Phase-Residual Analytical Theory of Equivalent Spatial Length and Its Application to Sub-THz Interconnect Characterization},
  journal = {TechRxiv preprint},
  year    = {2026},
  doi     = {10.36227/techrxiv.PENDING},
  version = {V3.6}
}

@software{Costryx2026LeqExtractor,
  author    = {Hsu, Chin-Yu},
  title     = {costryx-leq-extractor: Official Reference Implementation of the L_eq Extraction Framework},
  year      = {2026},
  publisher = {Zenodo},
  version   = {v0.1.0-foundational},
  doi       = {10.5281/zenodo.PENDING},
  url       = {https://github.com/costryx/costryx-leq-extractor}
}
```

A [`CITATION.cff`](CITATION.cff) file is provided for GitHub's native "Cite this repository" feature.

---

## 📜 License

This software is released under the Apache License 2.0. See [`LICENSE`](LICENSE).

The patent grant clause protects downstream users from reverse-patent claims on the foundational extractor disclosed herein.

---

## 🛡️ Non-Assertion

This repository, in alignment with §X.E of the source paper:

- Does not assert that any particular vendor's channel exhibits a defect.
- Does not assert that this implementation constitutes the sole valid methodology.
- Does not assert that this software has been formally adopted by any standardization organization.
- Does not assert endorsement by any cited author, entity, or affiliated institution.

This software is provided for theoretical metrology research and engineering measurement coordination. It does not constitute legal opinion, patent license, or product-compliance commitment.

---

## 🤝 Contributing

Pull requests within the foundational extractor scope are welcome.

Contributions touching BQSGO, CBC, or OP-2/OP-3 calibration-sequence algorithms will be deferred pending the companion publication.

---

## 📧 Contact

- Author: Chin-Yu Hsu
- ORCID: 0009-0009-6267-7897
- Email: chinyu@costryx.net
- Location: New Taipei City, Taiwan

Maintained by Costryx — establishing fixture-invariant metrology for the sub-THz era.
