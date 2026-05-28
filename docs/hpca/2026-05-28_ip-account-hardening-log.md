# IP Account Hardening Log — 2026-05-28

**Project:** Costryx Leq / GCI / MHL Enterprise API
**Repository:** https://github.com/costryx/costryx-leq-extractor
**Author:** Chin-Yu Hsu (Independent Researcher) — ORCID 0009-0009-6267-7897
**HPCA Reference:** V1.6 (EU AI Act Article 14 — Human Oversight)
**Companion White Paper:** V3.0 Seven Walls (Wall 5 — Gradient-origin Provenance)

---

## 1. Purpose

This log documents a single-day hardening session that brings an
independent inventor's public IP account to a minimum viable audit
profile (MVAP) consistent with EU AI Act Article 14 expectations on
human oversight, traceability, and provenance.

It is not a generic security checklist. It is a worked example showing
how a single individual, without enterprise SOC support, can establish
five reinforcing layers of provenance for an OpenAPI specification that
is already cited via Zenodo DOI.

## 2. Five Layers Established

### Layer 1 — Account

- Two-factor authentication enabled on GitHub account `chinyu-create`
- Recovery codes downloaded and stored offline
- Hardware security key (FIDO2) recommended as next-step backup factor

### Layer 2 — OpenAPI Specification (V4.0.1)

| File | SHA-256 | Size |
|---|---|---|
| openapi-leq-gci-mhl-v1.2.0.yaml | 345d2fc465eb93aac43d7a58a7a97191bca7755654232223a0605de2071ab9a9 | 56.0 KB |
| openapi-leq-gci-mhl-v1.2.0-resolved.yaml | e948e61b56b57bc2c03473c2560e0559177bc0c5e2f2dfd7f3371d48bb730b68 | 332.0 KB |
| openapi-leq-gci-mhl-v1.2.0.json | 07b93b581cf3f87cb4e3445e188a811e2c65cdfcc34c25506422b619b3a22cd8 | 84.0 KB |
| openapi-leq-gci-mhl-v1.2.0-resolved.json | 3538ff4c07125b813454879b17a6aefbe8d28755ce7622c84aad19a03aafcac7 | 444.0 KB |

Changes from V4.0:
- Contact email unified to `chinyu@costryx.net`
- Deprecated support URL removed
- "Swagger Editor ready" wording replaced with "Enterprise API"
- Companion artifact reference bumped to V4.0.1

### Layer 3 — Build Configuration

- `pyproject.toml` — `project.urls.Funding` corrected from
  `mailto:api-support@costryx.net` (invalid per PEP 621) to a valid URL
- All `api-support@costryx.net` references unified to `chinyu@costryx.net`
- `pip install -e .` now passes validate-pyproject

### Layer 4 — CI / CD

- GitHub Pages build & deploy: successful
- pytest on Python 3.10 / 3.11 / 3.12: all pass
- `.github/workflows/sha256.yml` workflow added
  - Triggers on push to `docs/api-viewer/openapi-leq-gci-mhl-v1.2.0*`
  - Computes SHA-256 of all four spec artifacts
  - Renders NIST FIPS PUB 180-4 style manifest
  - Auto-commits refreshed manifest as `github-actions[bot]`

### Layer 5 — Provenance

- `openapi-v1.2.0.sha256` — auto-refreshed by CI
- `openapi-v1.2.0.MANIFEST.txt` — auto-refreshed by CI
- Manifest commit: `35ad573733ab54c8bf9acaa8f2a5548bd99fd274`
- Manifest generated at: `2026-05-28T22:13:14+0800 (CST)`

## 3. Mapping to EU AI Act Article 14

| Article 14 Requirement | Evidence in This Log |
|---|---|
| Human oversight throughout AI system lifecycle | Single human author with documented account control + 2FA |
| Tools and environment enable understanding of system | Self-hosted Redoc viewer + Zenodo permanent record |
| Ability to remain aware of automation bias | Manual review of CI run logs prior to acceptance |
| Decide not to use the system in given situation | Account holder retains exclusive merge rights to main |
| Intervene and reverse output | Auto-commits identifiable as `github-actions[bot]`; revertible |
| Stop the system | Workflow can be disabled via Actions tab; specs immutable on Zenodo |

## 4. Mapping to White Paper V3.0 Seven Walls

| Wall | Mapping |
|---|---|
| Wall 4 — Semantic Audit | OpenAPI spec is a high-consequence low-bit semantic contract; SHA-256 + Zenodo DOI provide downstream audit anchor |
| Wall 5 — Gradient Provenance | CI-generated manifest is a software-layer audit trail demonstrating that even individual researchers can implement repo-pinned, third-party-verifiable provenance |
| Wall 6 — Safety Integrity | `Require signed commits` + branch protection + `chore(manifest)` automation collectively form a minimum institutional memory of provenance practice |

## 5. Open Issues for Future Work

- Migrate to FIDO2 hardware key as primary 2FA factor
- Add commit signing (GPG or sigstore) and `Require signed commits` branch rule
- Add `cosign sign-blob` to manifest workflow for keyless cryptographic attestation
- Mirror manifest to Zenodo on every release (currently V4.0.1 manual)

## 6. Changelog

- 2026-05-27 — V4.0 spec uploaded to Zenodo (DOI 10.5281/zenodo.20382496)
- 2026-05-28 19:00 — White paper V3.0 audit completed
- 2026-05-28 21:00 — V4.0.1 spec corrections committed
- 2026-05-28 21:30 — pyproject.toml Funding URL fix
- 2026-05-28 22:13 — SHA-256 workflow v2 (NIST FIPS style) deployed; manifest commit `35ad573`

---

*This log is reproducible. Any third party can clone the repository at
commit `35ad573` and re-compute the four SHA-256 values listed above to
verify the integrity of the V4.0.1 OpenAPI specification corpus.*
