# Disclosure Boundary of `costryx-leq-extractor`

This document explicitly delineates the **scope** and **boundary**
of what this repository discloses and implements, in strict alignment
with §V.G and §X.C of the source paper:

> Hsu, C.-Y. (2026). *256 GT/s PAM4 Channel Validation Under a Fixed
> Reference Plane: Differential-Mode Phase-Residual Analytical Theory
> of Equivalent Spatial Length and Its Application to Sub-THz
> Interconnect Characterization* (V4.0). Zenodo. DOI: [10.5281/zenodo.20382496](https://doi.org/10.5281/zenodo.20382496).

---

## ✅ IN SCOPE — Disclosed and Implemented

| # | Capability | Source Section | Module |
|---|-----------|----------------|--------|
| 1 | L_eq(f_k) at three anchors (64/96/128 GHz) | §III, §V.A | `extractor.py` |
| 2 | L_eq(f) continuous spectrum (e.g., 110–220 GHz) | §V.G | `continuous.py` |
| 3 | GCI = max-ratio decision scalar | §III.A, Eq. 3-1 | `gci.py` |
| 4 | L_eq,bnd = λ_EM/5 boundary computation | §V.A | `boundary.py` |
| 5 | σ_Leq RSS uncertainty propagation | §V.F | `uncertainty.py` |
| 6 | GUM Type A / Type B classification | §V.F.1 | `uncertainty.py` |
| 7 | MHL SHA-256 hash chain (Eq. 6-1) | §VI.A | `mhl.py` |
| 8 | Standard L_eq(f) spectrum visualization | (companion paper) | `visualization.py` |
| 9 | Touchstone 2.1 ingestion (via `scikit-rf`) | §V.G | `extractor.py` |
| 10 | Mixed-mode S-parameter conversion (S_CD21) | (publicly known) | `extractor.py` |

---

## ❌ OUT OF SCOPE — NOT Disclosed in This Repository

The following implementation-level content is **explicitly excluded**
from this repository per §X.C of the source paper, and is reserved
for a coordinated companion publication:

### (i) BQSGO Thermal-Drift Separation
- **What it is**: numerical methods for separating geometric
  steady-state phase from thermal-transient phase in dual-state
  acquisition (M-1 cold-start vs M-2 thermal-equilibrium).
- **Why excluded**: this involves ms-level coupling with the SerDes
  DSP adaptive loop and contains proprietary numerical know-how
  beyond the scope of a foundational reference implementation.

### (ii) CBC Under Non-Ideal SCD21 Profiles
- **What it is**: concrete implementation of capture-basin
  classification (Stable / Marginal / Trap-Adjacent) when the SCD21
  magnitude profile deviates from ideal symmetry.
- **Why excluded**: this involves topological trajectory analysis
  in the L_eq–GCI phase plane requiring specialized algorithms
  reserved for the companion publication.

### (iii) OP-2/OP-3 Boundary Calibration Sequences
- **What it is**: instrument-specific calibration-sequence algorithms
  optimized for the 96 GHz and 128 GHz operating-point boundaries.
- **Why excluded**: this involves measurement-specific know-how
  closely tied to particular VNA classes and probe configurations.

---

## 🛡️ Pull Request Policy

Pull requests touching items (i), (ii), or (iii) above will be
**deferred** pending the companion publication. Contributors are
encouraged to focus on:

- Performance optimization of the foundational extractor
- Additional test coverage on synthetic / open DUT datasets
- Documentation improvements
- Cross-platform compatibility (Linux / macOS / Windows)
- Visualization enhancements within the standard color-code framework

---

## 📚 Companion Publications (Forthcoming)

The author plans to release the following companion publications,
each accompanied by an extension to this repository under a separate
versioning track:

1. **Continuous-Spectrum L_eq(f) Visualization Standard** (~Q3 2026)
   — locks in the visual language for cross-laboratory spectrum
   comparison.

2. **BQSGO + CBC Implementation Paper** (~Q1 2027)
   — discloses the numerical methods for thermal-drift separation
   and capture-basin classification, contingent upon completion of
   the three-stage empirical validation program.

3. **OP-2/OP-3 Calibration-Sequence Disclosure** (timing TBD)
   — release contingent upon instrument-class evolution and
   commercial considerations.

---

## 🔗 Related Repositories by the Author

The author also maintains an **independent IP track** focused on
Layer 0 physical sovereignty and 1.8T extreme-compute interconnect
architecture:

- `l24observer-alt/0128-Layer0-Manifesto`
  — operates under a distinct license model (0128 Physical Sovereignty
  License) and is independently licensed from this repository.

The two tracks are **complementary but independently licensed**:
- This repo: Apache 2.0 (foundational extractor, encourages reuse)
- 0128 repo: 0128 Physical Sovereignty License (closed physics)

Cross-citation between repositories is informational only and does
not constitute joint licensing or shared IP authorization.

---

*Last updated: 2026-05-26*  
*Aligned with paper V4.0 (Zenodo DOI: [10.5281/zenodo.20382496](https://doi.org/10.5281/zenodo.20382496))*  
*Maintained by Costryx*
