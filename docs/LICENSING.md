# Licensing — Costryx Three-Layer IP Architecture

**Last updated:** 2026-05-27  
**Maintainer:** Chin-Yu Hsu (chinyu@costryx.net)  
**ORCID:** [0009-0009-6267-7897](https://orcid.org/0009-0009-6267-7897)

---

## TL;DR (Three-Sentence Summary)

The Costryx Leq/GCI/MHL framework is published under a **three-layer licensing structure**: the **methodology paper** (Layer 1) is **CC-BY-4.0** for academic reuse, the **reference implementation software** (Layer 2) is **Apache-2.0** with explicit patent grant, and the **enterprise API specification** (Layer 3) is **Proprietary** with reading-and-evaluation permitted but commercial deployment requiring license.

**Public visibility ≠ free commercial use.** Reading and evaluation are free across all three layers; commercial deployment requires layer-appropriate licensing.

This document is the **authoritative source** for all licensing questions related to the Costryx IP portfolio.

---

## Three-Layer Architecture Overview

| Layer | Asset | License | DOI | Commercial Use? |
|-------|-------|---------|-----|-----------------|
| 1️⃣ Paper | V4.0.1 Working Report (latest) | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) | [10.5281/zenodo.20411061](https://doi.org/10.5281/zenodo.20411061) | ✅ With attribution |
| 1️⃣ Paper | V2.4.1 Foundation | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) | [10.5281/zenodo.20341571](https://doi.org/10.5281/zenodo.20341571) | ✅ With attribution |
| 2️⃣ Software | costryx-leq-extractor v0.1.0 | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) | [10.5281/zenodo.20384916](https://doi.org/10.5281/zenodo.20384916) | ✅ With Apache-2.0 compliance |
| 3️⃣ API Spec | OpenAPI 3.1 v1.2.0 | Proprietary (Costryx) | [10.5281/zenodo.20405124](https://doi.org/10.5281/zenodo.20405124) | ⚠️ Requires written license |

**Concept DOIs** (always resolve to the latest version):
- V4.0/V4.0.1 series: [10.5281/zenodo.20382495](https://doi.org/10.5281/zenodo.20382495)
- V2.4/V2.4.1 series: [10.5281/zenodo.20341570](https://doi.org/10.5281/zenodo.20341570)

---

## Layer 1 — Methodology Paper (CC-BY-4.0)

### Scope
Academic publications describing the Differential-Mode Phase-Residual Analytical Theory, the three-anchor Leq + GCI decision framework, the closed-form σLeq uncertainty propagation model, and the MHL SHA-256 hash chain formalization.

### Version Lineage
- **V2.4 (2026-05-22)** → **V2.4.1 (2026-05-27, metadata-only revision)**: Foundation paper for fixture-invariant Leq extraction at 110–220 GHz. DOI [10.5281/zenodo.20341571](https://doi.org/10.5281/zenodo.20341571) (stable; metadata updated in V2.4.1 to add three-layer IP cross-references without changing scientific content or DOI).
- **V4.0 (2026-05-26)** → **V4.0.1 (2026-05-27, new DOI)**: 256 GT/s PAM4 application paper. V4.0.1 corrects a software DOI typo in V4.0 and adds Layer 3 API reference. DOI of V4.0.1: [10.5281/zenodo.20411061](https://doi.org/10.5281/zenodo.20411061). Concept DOI (always latest): [10.5281/zenodo.20382495](https://doi.org/10.5281/zenodo.20382495).

### What You Can Do
- ✅ Read, download, archive
- ✅ Quote, cite, reference in your own work
- ✅ Translate (with attribution)
- ✅ Build derivative academic work (with attribution)
- ✅ Use in commercial documentation (with attribution)
- ✅ Redistribute in original or modified form (with attribution)

### What You Must Do
- 🛡️ Provide attribution: cite the latest paper version as
  > Hsu, C.-Y. (2026). 256 GT/s PAM4 Channel Validation Under a Fixed Reference Plane (V4.0.1). Zenodo. https://doi.org/10.5281/zenodo.20411061

- 🛡️ Include a link to the CC-BY-4.0 license
- 🛡️ Indicate if changes were made

### What's Not Granted
- ❌ Patent rights (paper does not transfer patent license)
- ❌ Trademark rights (Costryx name and marks remain reserved)

---

## Layer 2 — Reference Implementation Software (Apache-2.0)

### Scope
The `costryx-leq-extractor` Python package (v0.1.0 and later releases), including source code, configuration files, documentation, and example notebooks hosted at https://github.com/costryx/costryx-leq-extractor.

### What You Can Do
- ✅ Use commercially (free of charge)
- ✅ Modify, fork, distribute (original or modified)
- ✅ Embed in proprietary products (no copyleft contagion)
- ✅ Sublicense under more restrictive terms (for your derivative)

### What You Must Do (Apache-2.0 Compliance)
- 🛡️ Preserve copyright notices
- 🛡️ Include a copy of the Apache-2.0 license
- 🛡️ Document significant changes in modified versions (NOTICE file)
- 🛡️ Retain trademark notices (Costryx name and marks remain protected)

### Patent Grant (Apache-2.0 §3)
> Each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work.

**Implication:** Apache-2.0 §3 grants a patent license **only for the contributions made by the licensor**. It does **not** waive Costryx's separate patent portfolio (USPTO Provisional × 6, TIPO × 6+, PCT × 2, 153 countries) outside the scope of the released code.

### Patent Termination Clause (Apache-2.0 §3)
If you initiate patent litigation against any entity alleging that the Work infringes patents, all patent licenses granted to you under Apache-2.0 §3 **terminate as of the date such litigation is filed**.

### Development Series
- **v0.1.0** — immutable Zenodo reference snapshot (May 26, 2026)
- **V3.5 series** — active internal development on `main` branch (not yet released)

---

## Layer 3 — Enterprise API Specification (Proprietary)

### Scope
The Leq/GCI/MHL Enterprise API Specification (OpenAPI 3.1) v1.2.0, including all 22 paths, 33 operations, 48 schemas, 11 tags, 4 server profiles, 4 security schemes, and 1 webhook definition. Hosted at:
- Zenodo DOI: [10.5281/zenodo.20405124](https://doi.org/10.5281/zenodo.20405124)
- Interactive Viewer: https://costryx.github.io/costryx-leq-extractor/api-viewer/

### What You Can Do (Without License)
- ✅ Read the specification
- ✅ Evaluate for internal feasibility studies
- ✅ Quote brief excerpts in academic publications (with attribution)
- ✅ Reference the DOI in technical documentation

### What Requires Written License
- ⚠️ Implementing a backend server that conforms to this API
- ⚠️ Building a client SDK against this API
- ⚠️ Commercial deployment of any system that conforms to this API
- ⚠️ Public claims of "compliant with Leq/GCI/MHL API"
- ⚠️ Redistribution of the specification (modified or unmodified)
- ⚠️ Use of the SHA-256 manifest schema in commercial products

### Why Proprietary?
This is the standard contract-licensing model used by PCIe-SIG, Visa, SWIFT, and other industry standards bodies:
- **Specification transparency** — clients can pre-evaluate before commitment
- **Quality control** — Costryx ensures interoperability across implementations
- **Commercial sustainability** — funding ongoing development and audit infrastructure

### Licensing Inquiry
Please contact: **chinyu@costryx.net**

Standard turnaround: 5-7 business days for initial response.

---

## Patent Portfolio (Cross-Reference)

The Costryx patent portfolio covers underlying physical compensation, thermodynamic interlock, and topological geometric offload mechanisms. **It is separate from and not waived by** the Layer 2 Apache-2.0 license:

| Jurisdiction | Filings | Status |
|--------------|---------|--------|
| USPTO Provisional | × 6 | Filed |
| TIPO Invention Patent (Taiwan) | × 6+ | Filed / Pending |
| PCT International | × 2 (153 countries) | Filed |
| Earliest Priority Date | 2026-02-02 | — |

For patent licensing inquiries (including FRAND terms for standards-essential implementations), please contact: **chinyu@costryx.net**

---

## License Compatibility Matrix

| Combination | Compatible? | Notes |
|-------------|-------------|-------|
| Cite Layer 1 in your CC-BY paper | ✅ Yes | Standard CC-BY attribution |
| Use Layer 2 in MIT-licensed project | ✅ Yes | Apache-2.0 is permissive |
| Use Layer 2 in GPL-3.0 project | ✅ Yes (one-way) | Apache-2.0 → GPL-3.0 allowed |
| Use Layer 2 in GPL-2.0 project | ⚠️ Generally no | Apache-2.0 patent clause conflict |
| Embed Layer 2 in proprietary product | ✅ Yes | Must preserve NOTICE / LICENSE |
| Implement Layer 3 API commercially | ❌ Requires license | Contact Costryx |
| Quote Layer 3 schema in paper | ✅ Yes | Brief quote with attribution |

---

## Frequently Asked Questions

### Q1: Can I use the software (Layer 2) in my commercial product without paying?
**A:** Yes. Apache-2.0 permits commercial use free of charge. You must preserve copyright notices, the LICENSE file, and the NOTICE file. The Costryx patent portfolio outside the released code scope is **not** waived.

### Q2: Can I implement the API specification (Layer 3) in my own backend without paying?
**A:** Not for commercial deployment. You may read and evaluate the specification freely. Building a conformant implementation for commercial use requires a written license from Costryx.

### Q3: What if I only use the API specification for internal R&D, not commercial deployment?
**A:** Internal R&D and feasibility evaluation are permitted without a written license. The boundary triggers when:
- You deploy to production (internal or external users)
- You make public claims of conformance
- You distribute conformant code to third parties

### Q4: How does the patent grant in Apache-2.0 §3 relate to the Costryx patent portfolio?
**A:** Apache-2.0 §3 grants a patent license **only for the contributions in the released code**. The broader Costryx patent portfolio (covering physical compensation, thermodynamic interlock, etc.) is **separate** and not granted by the Apache-2.0 license. For uses that may touch the broader portfolio, contact Costryx for licensing.

### Q5: Can I fork the software and rebrand it?
**A:** Yes (under Apache-2.0), but you must:
- Preserve original copyright and license notices
- Document your changes in the NOTICE file
- Not use the "Costryx" name or marks for your fork without permission

### Q6: Which paper version should I cite?
**A:** Cite the **latest version**:
- For the 256 GT/s PAM4 application paper: V4.0.1, DOI [10.5281/zenodo.20411061](https://doi.org/10.5281/zenodo.20411061) (Concept DOI [10.5281/zenodo.20382495](https://doi.org/10.5281/zenodo.20382495))
- For the 110–220 GHz foundation paper: V2.4.1 metadata revision (DOI unchanged from V2.4: [10.5281/zenodo.20341571](https://doi.org/10.5281/zenodo.20341571); Concept DOI [10.5281/zenodo.20341570](https://doi.org/10.5281/zenodo.20341570))

### Q7: Where can I see the API specification interactively?
**A:** https://costryx.github.io/costryx-leq-extractor/api-viewer/ (self-hosted on GitHub Pages with Redoc; no third-party platform dependency).

### Q8: Why does V2.4 keep the same DOI after the V2.4.1 metadata revision?
**A:** V2.4 → V2.4.1 is a metadata-only revision performed under Zenodo's edit policy: scientific content (the PDF) is identical, only metadata (description, related identifiers, version label) was updated to cross-reference the V4.0.1 application paper, Layer 2 software, and Layer 3 API specification. The DOI [10.5281/zenodo.20341571](https://doi.org/10.5281/zenodo.20341571) remains stable so that all prior citations of V2.4 continue to resolve correctly.

---

## Contact

- **Licensing & Commercial Inquiries:** chinyu@costryx.net
- **Author / Maintainer:** Chin-Yu Hsu
- **ORCID:** [0009-0009-6267-7897](https://orcid.org/0009-0009-6267-7897)
- **GitHub:** [costryx/costryx-leq-extractor](https://github.com/costryx/costryx-leq-extractor)
- **Affiliation:** Independent Researcher, New Taipei City, Taiwan

---

## Document History

| Date | Version | Notes |
|------|---------|-------|
| 2026-05-27 | 1.0 | Initial publication aligned with V4.0.1 Paper release and V2.4.1 metadata revision |

---

*This document is provided for clarity and is not legal advice. For binding terms, refer to the actual LICENSE files (LICENSE, individual layer DOIs) and any executed commercial license agreement.*
