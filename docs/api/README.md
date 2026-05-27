# Leq / GCI / MHL Enterprise API Specification

**Multi-tenant enterprise API for sub-THz interconnect metrology — the public contract layer of the Costryx three-layer IP architecture.**

[![Zenodo DOI](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.20405124-blue.svg)](https://doi.org/10.5281/zenodo.20405124)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1.0-green.svg)](https://spec.openapis.org/oas/v3.1.0)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](./LICENSE.md)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--6267--7897-A6CE39.svg)](https://orcid.org/0009-0009-6267-7897)

---

## 🌐 Overview

This directory hosts the **public OpenAPI 3.1 contract** for the Leq / GCI / MHL enterprise platform — a multi-tenant API that operationalizes the Equivalent Spatial Length (`Leq`) metrology framework for 1.6 T – 3.2 T sub-THz interconnects, including PCIe 8.0 PAM4 (256 GT/s) channel validation under a fixed reference plane.

The specification is intentionally published as a **transparent contract surface** to enable:

- Procurement evaluation by OSAT, Hyperscaler, Fabless, and EDA partners
- Pre-integration design review without requiring NDA execution
- Third-party audit of compliance with NIST FIPS PUB 180-4, JCGM 100:2008, and ISO/IEC 17025 §7.5
- Academic citation and reproducibility verification

Confidential implementation details — proprietary calibration matrices, DUT routing coordinates, stack-up parameters, and vendor-specific settings — are **deliberately excluded** and remain subject to NDA / MSA negotiation.

---

## 🏗️ Three-Layer IP Architecture

| Layer | Artifact | Permanent Identifier | License |
|---|---|---|---|
| **1 (Paper)** | V4.0 Working Report — *256 GT/s PAM4 Channel Validation Under a Fixed Reference Plane* | [10.5281/zenodo.20382496](https://doi.org/10.5281/zenodo.20382496) | CC-BY-4.0 |
| **1 (Paper)** | V2.4 Foundation — *Equivalent Spatial Length in 1.6T-3.2T Interconnects* | [10.5281/zenodo.20341571](https://doi.org/10.5281/zenodo.20341571) | CC-BY-4.0 |
| **2 (Software)** | `costryx-leq-extractor` v0.1.0 (reference implementation) | [10.5281/zenodo.20384916](https://doi.org/10.5281/zenodo.20384916) | MIT |
| **3 (API)** ⭐ | **OpenAPI 3.1 Specification v1.2.0** | **[10.5281/zenodo.20405124](https://doi.org/10.5281/zenodo.20405124)** | **Proprietary** |
| 3 (API) | Concept DOI (all versions) | [10.5281/zenodo.20405123](https://doi.org/10.5281/zenodo.20405123) | — |
| Live Documentation | SwaggerHub interactive console | [app.swaggerhub.com/.../1.2.0](https://app.swaggerhub.com/apis/chinyuorganization/leq-gci-mhl-enterprise-api/1.2.0) | — |

> 🔐 **License gradient by design**: academic openness (Layer 1) → community adoption (Layer 2) → commercial contract (Layer 3). The closer to deployment, the tighter the license.

---

## 📐 Specification at a Glance

| Item | Value |
|---|---|
| OpenAPI version | **3.1.0** (with JSON Schema 2020-12) |
| API version | **1.2.0** |
| Verification | **0 errors / 0 warnings** on `editor.swagger.io` |
| Paths | 22 |
| Operations | 33 (across `GET` / `POST` / `PATCH` / `DELETE`) |
| Tags | 11 (Projects / DUTs / Files / Calibration / Measurements / Anchors / Uncertainty / Hash / MHL / Audit / Webhooks) |
| Schemas | 48 (all with `additionalProperties: false`) |
| Reusable parameters / responses / headers | 16 / 7 / 5 |
| Servers | 4 (production / sandbox / audit-readonly / tenant-isolated) |
| Security schemes | 4 (OAuth2 / OIDC / mTLS / API Key) |
| Webhooks | 1 (`analysisCompleted`, OAS 3.1 native) |
| Cryptographic anchor | SHA-256 (NIST FIPS PUB 180-4) |

---

## 🧬 Key Schemas

| Schema | Purpose |
|---|---|
| `AnchorPlan` | PCIe 8.0 three-anchor (64 / 96 / 128 GHz) decision rule for sub-THz channel validation |
| `UncertaintyModel` | σ_Leq five-source GUM Type A/B propagation per JCGM 100:2008 |
| `HashChainNode` | SHA-256 chain element aligned with NIST FIPS PUB 180-4 |
| `CalibrationStep` | Calibration step definition: `TRL` / `MULTILINE_TRL` / `SOLT` / `LRRM` / `AFR` / `AFR_2X_THRU` / `TDR` |
| `Measurement` | Full measurement lifecycle compliant with ISO/IEC 17025 §7.5 audit-trail requirements |
| `MhlPackage` | Immutable manifest with cryptographic chain anchor (Measurement Hash Ledger) |
| `Project` / `Dut` / `File` | Top-level resource hierarchy for tenant-isolated metrology workflows |

---

## 🛡️ Security Model

The API is designed for **defense-in-depth deployment** in regulated industries (semiconductor, aerospace, financial-grade audit):

| Layer | Mechanism |
|---|---|
| Transport | TLS 1.3 mandatory; mTLS for tenant-isolated server |
| Authentication | OAuth2 (client_credentials, authorization_code) and OIDC (with PKCE) |
| Authorization | Scope-based access (`projects.read`, `measurements.write`, `audit.read`, `mhl.append`, …) |
| Data residency | Tenant-isolated server endpoint with subdomain templating (`{tenantSubdomain}.api.example.com`) |
| Audit immutability | Append-only `MhlPackage` with SHA-256 chain anchor; verifiable via `audit-readonly` server |
| Tamper evidence | Every mutating operation produces a `HashChainNode` recorded in the MHL |
| Service contract | `termsOfService` and `license` declared in `info` block; SLA via separate MSA |

---

## 🌍 Server Topology

| Server | URL pattern | Use case |
|---|---|---|
| Production | `https://api.example.com/v1` | Multi-tenant, full read/write |
| Sandbox | `https://sandbox.api.example.com/v1` | Testing, ephemeral data, no SLA |
| Audit (read-only) | `https://audit-readonly.api.example.com/v1` | Restricted to `audit.read` scope; immutable history view |
| Tenant-isolated | `https://{tenantSubdomain}.api.example.com/v1` | Data-sovereignty deployments (e.g. EU-only, TW-only) |

> ℹ️ All URLs above use `example.com` as a placeholder. Actual endpoint hostnames are provided in the commercial deployment package.

---

## 📂 Directory Contents

| File | Size | SHA-256 (truncated) | Purpose |
|---|---|---|---|
| `openapi-leq-gci-mhl-v1.2.0.yaml` | 55.8 KB | `39918495…7ee1` | **Primary specification (YAML)** |
| `openapi-leq-gci-mhl-v1.2.0.json` | 80.4 KB | `9253c0c3…c035` | Primary specification (JSON) |
| `openapi-leq-gci-mhl-v1.2.0-resolved.yaml` | 331.8 KB | `af4e2337…383a` | Fully resolved (no `$ref`) — for codegen tools |
| `openapi-leq-gci-mhl-v1.2.0-resolved.json` | 441.2 KB | `099e2098…1303` | Fully resolved (no `$ref`) — for codegen tools |
| `openapi-v1.2.0.sha256` | 412 B | — | SHA-256 hashes of the four spec files |
| `openapi-v1.2.0.MANIFEST.txt` | 1.2 KB | — | Cryptographic manifest with timestamp + ORCID + companion DOIs |
| `LICENSE.md` | — | — | Proprietary license terms |
| `README.md` | — | — | This file |

> 🔐 To verify integrity: `sha256sum -c openapi-v1.2.0.sha256` should report `OK` for all four spec files.

---

## 🚀 Quick Start

### Validate locally

```bash
# Using Redocly CLI
npx @redocly/cli lint openapi-leq-gci-mhl-v1.2.0.yaml

# Using Spectral
npx @stoplight/spectral-cli lint openapi-leq-gci-mhl-v1.2.0.yaml

# Using openapi-generator
openapi-generator validate -i openapi-leq-gci-mhl-v1.2.0.yaml
```

### Generate a client SDK

```bash
# Python client
openapi-generator generate \
  -i openapi-leq-gci-mhl-v1.2.0-resolved.yaml \
  -g python \
  -o ./client-python

# TypeScript client
openapi-generator generate \
  -i openapi-leq-gci-mhl-v1.2.0-resolved.yaml \
  -g typescript-axios \
  -o ./client-ts
```

### Browse interactively

Open the [SwaggerHub console](https://app.swaggerhub.com/apis/chinyuorganization/leq-gci-mhl-enterprise-api/1.2.0) for live, navigable documentation with try-it-out support.

---

## 🏛️ Standards Alignment

This specification is designed to interoperate with the following standards out of the box:

| Domain | Standard |
|---|---|
| API description | OpenAPI 3.1.0 (W3C / OAI) |
| Schema | JSON Schema 2020-12 |
| Cryptographic hashing | NIST FIPS PUB 180-4 (SHA-256) |
| Measurement uncertainty | JCGM 100:2008 (GUM) |
| Laboratory quality | ISO/IEC 17025 §7.5 (audit trail) |
| De-embedding | IEEE Std 370-2020 (AFR / 2X-THRU) |
| Channel modeling | IEEE 802.3 / OIF-CEI-224G / PCIe 8.0 |
| Security | OAuth 2.0 (RFC 6749), OIDC 1.0, TLS 1.3 (RFC 8446) |

---

## 💼 Use Cases

### For OSAT and Foundry Partners
Pre-integration validation of sub-THz channel measurement workflows; immutable audit-trail compliance for customer reporting.

### For Hyperscaler Procurement
Vendor-agnostic measurement contract enabling supplier comparison without requiring vendor-specific tooling lock-in.

### For Fabless Design Teams
Reference contract for internal SI/PI dashboards integrating Leq, σ_Leq, and three-anchor decision logic.

### For EDA Vendors
Stable interface to inject calibration matrices and uncertainty models into existing simulation pipelines.

### For Academic Researchers
Reproducibility anchor: any published measurement can be replayed against the specified schema and verified via SHA-256 manifest.

---

## 🔐 License

This specification is **proprietary**. See [`LICENSE.md`](./LICENSE.md) for full terms.

**Permitted without separate license**: reading, reviewing, citing, and assessing interoperability.

**Requires a commercial license**: production deployment, redistribution, modification, derivative API specifications, or any use that materially competes with the author's own commercial offerings.

> 📩 **Commercial inquiries**: [chinyu@costryx.net](mailto:chinyu@costryx.net)

---

## 🛡️ Intellectual Property Notice

The methodology, calibration framework, hash chain protocol, and geometric compensation system underlying this API specification are protected by:

- **USPTO Provisional Applications**: 63/989,277 / 63/973,642 / 64/032,845 / 64/032,859 / 64/037,254 / 64/037,256
- **TIPO Invention Applications**: 115110956 / 115112738 / 115115336 / 115111414 / 115112090 / 115115905
- **PCT International**: PCT/US26/25316 / PCT/US26/25323 (153 contracting states)

**Earliest priority date**: 2026-02-02. **PCT applicant**: PhysLayer IP Holdings LLC.

Implementation of any commercial system using the underlying methodology requires both (a) a commercial license under the terms above, and (b) a separate patent license from the rights holder.

---

## 📚 Citation

If you reference this specification in academic work or technical documentation, please cite:

```bibtex
@software{hsu_leq_api_2026,
  author       = {Hsu, Chin-Yu},
  title        = {{Leq / GCI / MHL Enterprise API Specification 
                   (OpenAPI 3.1) v1.2.0}},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.2.0},
  doi          = {10.5281/zenodo.20405124},
  url          = {https://doi.org/10.5281/zenodo.20405124},
  orcid        = {0009-0009-6267-7897}
}
```

**APA format**:

> Hsu, C.-Y. (2026). *Leq / GCI / MHL Enterprise API Specification (OpenAPI 3.1) v1.2.0* (Version: 1.2.0). Zenodo. https://doi.org/10.5281/zenodo.20405124

---

## ❓ FAQ

**Q: Why is the license proprietary if the specification is public?**  
A: Public visibility ≠ free use. Reading and evaluating the contract is free; deploying or commercializing it requires a license. This pattern is standard for industry consortium APIs (e.g. Visa, Swift, PCIe-SIG).

**Q: Can I generate a server stub from this YAML?**  
A: Yes, for evaluation. Production deployment requires a commercial license — see `LICENSE.md`.

**Q: Where is the actual production endpoint?**  
A: All `example.com` hostnames in the spec are placeholders. Real endpoints are provisioned through the commercial deployment package after license execution.

**Q: How do I verify the file integrity?**  
A: Run `sha256sum -c openapi-v1.2.0.sha256`. All four spec files should report `OK`. The hashes are also recorded in the Zenodo DOI page.

**Q: Will there be a v1.2.1 or v1.3.0?**  
A: Yes. Future versions will be published under the same Concept DOI ([10.5281/zenodo.20405123](https://doi.org/10.5281/zenodo.20405123)). Subscribe to the GitHub repository for release notifications.

**Q: Is the underlying physics open?**  
A: The high-level theory is published in the V4.0 paper (CC-BY-4.0). The reference implementation is open-source under MIT (Layer 2). The commercial calibration matrices and stack-up parameters are NDA-only.

---

## 👤 Author

**Chin-Yu Hsu** — Independent Researcher  
ORCID: [0009-0009-6267-7897](https://orcid.org/0009-0009-6267-7897)  
Email: [chinyu@costryx.net](mailto:chinyu@costryx.net)  
LinkedIn: *(profile)*  

---

## 🗓️ Changelog

| Version | Date | Notes |
|---|---|---|
| **1.2.0** | 2026-05-27 | First public Zenodo release. 22 paths / 48 schemas / 4 servers / 1 webhook. SHA-256 manifest. |
| 1.1.x | 2026-05 | Internal SwaggerHub iterations |
| 1.0.0 | 2026-04 | Initial draft (private) |

---

*Last updated: 2026-05-27 · Layer 3 of the Costryx three-layer IP architecture · Powered by OpenAPI 3.1.*
