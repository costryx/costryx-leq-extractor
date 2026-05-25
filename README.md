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
plot_leq_spectrum_standard(
    spectrum,
    anchors,
    title="DUT Continuous L_eq(f) Spectrum",
)
```

