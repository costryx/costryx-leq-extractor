# costryx-leq-extractor

[![Python tests](https://img.shields.io/badge/Python%20tests-passing-brightgreen)](https://github.com/costryx/costryx-leq-extractor/actions)
[![DOI Paper](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20411061-blue)](https://doi.org/10.5281/zenodo.20411061)
[![DOI Software](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20384916-blue)](https://doi.org/10.5281/zenodo.20384916)
[![DOI API](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20405124-blue)](https://doi.org/10.5281/zenodo.20405124)
[![License](https://img.shields.io/badge/license-Apache--2.0-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-foundational--reference-orange)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()

**Official Reference Implementation** of the Equivalent Spatial Length (L_eq) extraction framework for sub-THz interconnect channel validation under a fixed reference plane.

This repository implements the foundational extractor disclosed in:

> Hsu, C.-Y. (2026). *256 GT/s PAM4 Channel Validation Under a Fixed Reference Plane: Differential-Mode Phase-Residual Analytical Theory of Equivalent Spatial Length and Its Application to Sub-THz Interconnect Characterization* (V4.0.1). Zenodo. DOI: [10.5281/zenodo.20411061](https://doi.org/10.5281/zenodo.20411061).

---

## 🎯 Scope of This Repository

This is the foundational reference implementation covering:

| Capability | Status |
|---|---|
| L_eq(f_k) three-anchor extraction (§III) | ✅ Implemented |
| L_eq(f) continuous-spectrum extraction (110–220 GHz) | ✅ Implemented |
| GCI = max{ L_eq / L_eq,bnd } decision indicator (§III.A) | ✅ Implemented |
| L_eq,bnd = λ_EM/5 boundary computation (§V.A) | ✅ Implemented |
| σ_Leq RSS uncertainty propagation (§V.F) | ✅ Implemented |
| MHL SHA-256 hash chain (§VI.A, Eq. 6-1) | ✅ Implemented |
| Standard L_eq(f) spectrum visualization (§V.G) | ✅ Implemented |
| Touchstone 2.1 ingestion via scikit-rf | ✅ Implemented |
| Mixed-mode S-parameter conversion (S_CD21) | ✅ Implemented |
| BQSGO thermal-drift separation | ❌ Out of scope |
| CBC under non-ideal S_CD21 profiles | ❌ Out of scope |
| OP-2/OP-3 calibration-sequence algorithms | ❌ Out of scope |

See [docs/DISCLOSURE_BOUNDARY.md](docs/DISCLOSURE_BOUNDARY.md) for explicit disclosure boundary. Items marked ❌ are reserved for a coordinated companion publication and are NOT included here.

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/costryx/costryx-leq-extractor.git
cd costryx-leq-extractor
pip install -e .
```

### Minimal Example

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

leq_op1 = extract_leq(ntwk, f_k=anchors.OP1, eps_eff=3.5)
leq_op2 = extract_leq(ntwk, f_k=anchors.OP2, eps_eff=3.5)
leq_op3 = extract_leq(ntwk, f_k=anchors.OP3, eps_eff=3.5)

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
T-1: TRL calibration
T-2: SOLT/LRRM
T-3: AFR (IEEE 370 §5)
T-4: Post-AFR de-embedding (TDR or equivalent)

This package assumes T-1 through T-4 have been completed externally prior to invocation. The extractor operates on the post-de-embedded S-parameter file (Touchstone 2.1, `.s2p` or `.s4p`).

For AFR de-embedding, we recommend the open-source `scikit-rf` implementation of IEEE 370 §5.

---

## 🗺️ Roadmap

- **v0.1.0** (current): Foundational reference implementation aligned with paper V4.0
- **v0.1.x**: Bug fixes and documentation improvements
- **v0.2.x** (planned): Optional synthetic demo datasets for users without sub-THz VNA hardware (release timing TBD)
- **v1.0.0** (future, ~Q3 2026): Aligned with companion publication on continuous-spectrum L_eq(f) visualization standard

---

## 🌐 Layer 3 — Enterprise API Specification

This repository's reference implementation underpins a formal **OpenAPI 3.1 specification** for enterprise integration:

- 📐 **Interactive Viewer** (self-hosted on GitHub Pages + Redoc):
  https://costryx.github.io/costryx-leq-extractor/api-viewer/
- 📚 **Zenodo Citation**: [10.5281/zenodo.20405124](https://doi.org/10.5281/zenodo.20405124)
- 📊 **Specification**: 22 paths / 33 operations / 48 schemas / 11 tags
- 🔐 **SHA-256 Manifest**: NIST FIPS PUB 180-4 aligned
- ⚖️ **License**: Proprietary (Layer 3 only — software remains Apache-2.0)

### Three-Layer IP Architecture

| Layer | Artifact | License | DOI |
|---|---|---|---|
| 1️⃣ Paper | V4.0.1 Working Report | CC-BY-4.0 | [10.5281/zenodo.20411061](https://doi.org/10.5281/zenodo.20411061) |
| 2️⃣ Software | This repository (v0.1.0) | **Apache-2.0** | [10.5281/zenodo.20384916](https://doi.org/10.5281/zenodo.20384916) |
| 3️⃣ API Contract | OpenAPI 3.1 v1.2.0 | Proprietary | [10.5281/zenodo.20405124](https://doi.org/10.5281/zenodo.20405124) |

---

## 📚 Citation

If you use this software, please cite both the methodology paper and this repository.

```bibtex
@misc{Hsu2026Leq256,
  author    = {Hsu, Chin-Yu},
  title     = {256 GT/s PAM4 Channel Validation Under a Fixed Reference Plane:
               Differential-Mode Phase-Residual Analytical Theory of Equivalent Spatial Length
               and Its Application to Sub-THz Interconnect Characterization},
  year      = {2026},
  publisher = {Zenodo},
  version  = {V4.0.1},
  doi       = {10.5281/zenodo.20411061},
  url       = {https://doi.org/10.5281/zenodo.20411061}
}

@software{Costryx2026LeqExtractor,
  author    = {Hsu, Chin-Yu},
  title     = {costryx-leq-extractor: Official Reference Implementation of the L_eq Extraction Framework},
  year      = {2026},
  publisher = {Zenodo},
  version   = {v0.1.0},
  doi       = {10.5281/zenodo.20384916},
  url       = {https://doi.org/10.5281/zenodo.20384916}
}
```

Software archived on Zenodo: [10.5281/zenodo.20384916](https://doi.org/10.5281/zenodo.20384916) (v0.1.0, May 2026).

A [CITATION.cff](CITATION.cff) file is provided for GitHub's native "Cite this repository" feature.

---

## 📜 License

This software is released under the **Apache License 2.0**. See [LICENSE](LICENSE).

The Apache-2.0 §3 patent grant clause protects downstream users from reverse-patent claims on the foundational extractor disclosed herein. This grant covers **only the contributions made by the licensor in the released code** and does **not** waive the broader Costryx patent portfolio (USPTO Provisional × 6, TIPO × 6+, PCT × 2, 153 countries) outside the scope of the released code.

### Three-Layer Licensing at a Glance

| Layer | Asset | License | Commercial Use? |
|-------|-------|---------|-----------------|
| 1️⃣ Paper | V4.0.1 / V2.4.1 Working Reports | CC-BY-4.0 | ✅ With attribution |
| 2️⃣ Software | costryx-leq-extractor v0.1.0 | Apache-2.0 | ✅ With Apache-2.0 compliance |
| 3️⃣ API Spec | OpenAPI 3.1 v1.2.0 | Proprietary (Costryx) | ⚠️ Requires written license |

> **Public visibility ≠ free commercial use.** Reading and evaluation are free across all three layers; commercial deployment of Layer 3 requires a written license from Costryx.

### 📜 Full Licensing Documentation

For the **authoritative source** on all licensing questions — including detailed Layer 1/2/3 terms, Apache-2.0 §3 patent grant scope, patent termination clause, Costryx patent portfolio cross-reference, license compatibility matrix (MIT / GPL-3.0 / GPL-2.0 / proprietary), and 8 frequently asked questions (Q1: commercial use; Q2: API implementation; Q4: patent grant scope; Q6: version citation; Q8: V2.4.1 metadata-only revision) — please see:

➡️ **[docs/LICENSING.md](docs/LICENSING.md)**

### Commercial Inquiries

For Layer 3 API licensing, FRAND terms for standards-essential implementations, or any commercial use that may touch the broader Costryx patent portfolio, please contact:

📩 **chinyu@costryx.net** (standard turnaround: 5-7 business days)

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

- **Author**: Chin-Yu Hsu
- **ORCID**: [0009-0009-6267-7897](https://orcid.org/0009-0009-6267-7897)
- **Email**: [chinyu@costryx.net](mailto:chinyu@costryx.net)
- **Location**: New Taipei City, Taiwan

---

*Maintained by **Costryx** — establishing fixture-invariant metrology for the sub-THz era.*
