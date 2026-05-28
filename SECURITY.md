# Security Policy

This repository hosts the **Costryx Leq / GCI / MHL Enterprise API**
specification, its reference implementation, and a NIST FIPS PUB 180-4
style cryptographic manifest. Any party relying on these artifacts as
an audit anchor (per EU AI Act Article 14) is encouraged to read this
policy in full before reporting issues.

---

## 1. Supported Versions

| Layer | Artifact | Version | Status |
|---|---|---|---|
| 1 — Paper | V4.0.1 Working Report (DOI 10.5281/zenodo.20411061) | V4.0.1 | ✅ Supported |
| 2 — Software | `costryx-leq-extractor` | v0.1.0 | ✅ Supported |
| 3 — API Spec | OpenAPI 3.1 — `openapi-leq-gci-mhl-v1.2.0` | 1.2.0 (V4.0.1) | ✅ Supported |
| All earlier revisions (V4.0 paper, pre-V4.0.1 spec, mailto-Funding `pyproject.toml`) | — | deprecated | ❌ Not supported |

The `main` branch is the single source of truth. Long-term immutable
copies live on Zenodo. Any artifact retrieved from a third-party mirror
or unofficial fork is **out of scope** for this policy.

## 2. Reporting a Vulnerability

Email: **chinyu@costryx.net**

Please include the following whenever applicable:

### 2.1 For software vulnerabilities (Layer 2)

- Affected file(s) and line numbers
- Reproduction steps or proof-of-concept
- Python version (`python --version`)
- Environment (`pip freeze | grep -E "scikit-rf|numpy|scipy"`)
- Whether the issue is reachable via the public OpenAPI surface

### 2.2 For specification vulnerabilities (Layer 3)

- The exact OpenAPI path / operationId / schema name affected
- The OpenAPI 3.1 + JSON Schema 2020-12 rule that is violated, if any
- Whether the issue is in `*.yaml`, `*.json`, `*-resolved.yaml`, or
  `*-resolved.json` (or all four)

### 2.3 For provenance / manifest vulnerabilities (Layer 5)

If the four SHA-256 hashes you compute locally do **not** match the
values published in `docs/api-viewer/openapi-v1.2.0.MANIFEST.txt`,
please include:

- The four hashes you computed locally
- The output of `git log -1 --format=%H` for the commit you tested
- Operating system, distribution version, and `sha256sum --version`
- Whether you cloned via HTTPS or SSH

This is treated as the **highest-severity** class of report because the
manifest is the audit anchor cited by the white paper, the HPCA Article
14 log, and the Zenodo record.

## 3. Acknowledgement Timeline

| Step | Target |
|---|---|
| Acknowledgement of receipt | within 7 calendar days |
| Initial triage and severity classification | within 14 calendar days |
| Remediation plan or non-action explanation | within 30 calendar days |
| Public advisory (if applicable) | coordinated with reporter |

This is an independent-researcher repository without 24×7 staffing.
Please do not expect commercial-grade response times. Severe
provenance breaks (Section 2.3) are prioritised over feature bugs.

## 4. Scope and Non-Scope

### 4.1 In scope

- Source code in this repository (`src/`, `docs/`, `.github/`)
- The four OpenAPI artifacts under `docs/api-viewer/`
- The auto-generated `openapi-v1.2.0.sha256` and
  `openapi-v1.2.0.MANIFEST.txt`
- The CI workflow `.github/workflows/sha256.yml`

### 4.2 Out of scope

- Forks, mirrors, or unofficial redistributions
- Third-party dependencies (report upstream)
- Issues that require credentials this repository does not hold
- Vulnerabilities in GitHub, Zenodo, or other hosting providers
- Anything covered by the disclosure boundary in
  [`docs/DISCLOSURE_BOUNDARY.md`](docs/DISCLOSURE_BOUNDARY.md), including
  BQSGO, CBC, and OP-2 / OP-3 calibration-sequence algorithms

## 5. No Bug Bounty

This project does not offer monetary rewards. Reporters who provide
high-quality, reproducible reports may be acknowledged in the
repository changelog or in a Zenodo release note, with their consent.

## 6. Account Security Posture

- The repository is maintained by a single author with two-factor
  authentication enabled on the GitHub account `chinyu-create`.
- Auto-commits made by `github-actions[bot]` are restricted to manifest
  refresh under `.github/workflows/sha256.yml`. Any commit attributed
  to `github-actions[bot]` that does **not** carry the message
  `chore(manifest): refresh SHA-256 manifest for v1.2.0 specs` should
  be treated as suspicious and reported under Section 2.3.
- Branch protection on `main` is in effect; force-pushes by external
  contributors are not accepted.

## 7. Coordinated Disclosure

For issues that may affect downstream users (especially Layer 3
licensees), the author prefers a coordinated 30-day private window
before public disclosure. Reporters who do not wish to coordinate are
free to publish on their own schedule; this policy does not restrict
that right.

---

**SPDX-License-Identifier:** CC-BY-4.0
**Document version:** 1.0 (2026-05-28)
**Audit anchor commit:** 35ad573733ab54c8bf9acaa8f2a5548bd99fd274
