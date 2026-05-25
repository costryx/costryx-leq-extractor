# costryx-leq-extractor

[![DOI](https://img.shields.io/badge/DOI-pending-blue.svg)](https://doi.org/10.36227/techrxiv.PENDING)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-foundational--reference-orange.svg)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()

**Official Reference Implementation** of the Equivalent Spatial Length
(L_eq) extraction framework for sub-THz interconnect channel validation.

This repository implements the **foundational extractor** disclosed in:

> Hsu, C.-Y. (2026). *256 GT/s PAM4 Channel Validation Under a Fixed
> Reference Plane: Differential-Mode Phase-Residual Analytical Theory
> of Equivalent Spatial Length and Its Application to Sub-THz
> Interconnect Characterization* (V3.6). TechRxiv. DOI: [pending].

---

## 🎯 Scope of This Repository

This is the **foundational reference implementation** covering:

| Capability | Status |
|-----------|--------|
| L_eq(f_k) three-anchor extraction (§III) | ✅ Implemented |
| L_eq(f) continuous-spectrum extraction | ✅ Implemented |
| GCI = max{ L_eq / L_eq,bnd } decision indicator (§III.A) | ✅ Implemented |
| σ_Leq RSS uncertainty propagation (§V.F) | ✅ Implemented |
| MHL SHA-256 hash chain (§VI.A, Eq. 6-1) | ✅ Implemented |
| Standard L_eq(f) spectrum visualization | ✅ Implemented |
| **BQSGO thermal-drift separation** | ❌ Out of scope |
| **CBC under non-ideal SCD21 profiles** | ❌ Out of scope |
| **OP-2/OP-3 calibration-sequence algorithms** | ❌ Out of scope |

> **See [`docs/DISCLOSURE_BOUNDARY.md`](docs/DISCLOSURE_BOUNDARY.md)
> for explicit disclosure boundary.** Items marked ❌ are reserved
> for a coordinated companion publication and are NOT included here.

---

## 🚀 Quick Start

```bash
git clone https://github.com/costryx/costryx-leq-extractor.git
cd costryx-leq-extractor
pip install -e .

import skrf as rf
from costryx_leq import (
    extract_leq, extract_leq_spectrum,
    compute_gci, AnchorAssignment,
    plot_leq_spectrum_standard,
)

ntwk = rf.Network("examples/synthetic_dut_256GTs.s4p")
anchors = AnchorAssignment()  # OP-1: 64 GHz, OP-2: 96 GHz, OP-3: 128 GHz

leq_op1 = extract_leq(ntwk, f_k=anchors.OP1, eps_eff=3.5)
leq_op2 = extract_leq(ntwk, f_k=anchors.OP2, eps_eff=3.5)
leq_op3 = extract_leq(ntwk, f_k=anchors.OP3, eps_eff=3.5)
gci = compute_gci([leq_op1, leq_op2, leq_op3], anchors)

spectrum = extract_leq_spectrum(ntwk, f_min=110e9, f_max=220e9)
plot_leq_spectrum_standard(spectrum, anchors,
                           title="DUT Continuous L_eq(f) Spectrum")

