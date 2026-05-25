"""MHL SHA-256 hash chain per §VI.A, Eq. 6-1."""
import hashlib
from dataclasses import dataclass
from typing import Optional


@dataclass
class MHLBundle:
    """Five-element MHL disclosure bundle (§VI)."""
    mhl1_touchstone_bytes: bytes      # raw .s2p / .s4p + metadata
    mhl2_calibration_history: bytes   # T-1..T-4 procedural declaration
    mhl3_variance_statistics: bytes   # ≥3 independent measurements
    mhl4_tdr_boundary: bytes          # TDR boundary verification
    laboratory_identifier: str        # MHL-5 lab ID

    def compute_hash(self) -> str:
        return compute_mhl_hash(
            self.mhl1_touchstone_bytes,
            self.mhl2_calibration_history,
            self.mhl3_variance_statistics,
            self.mhl4_tdr_boundary,
        )


def compute_mhl_hash(mhl1: bytes, mhl2: bytes,
                     mhl3: bytes, mhl4: bytes) -> str:
    """
    H_MHL = SHA-256( MHL-1 ‖ MHL-2 ‖ MHL-3 ‖ MHL-4 )    (Eq. 6-1)

    Per NIST FIPS PUB 180-4. Returns 64-character hex digest.
    """
    h = hashlib.sha256()
    for blob in (mhl1, mhl2, mhl3, mhl4):
        if not isinstance(blob, (bytes, bytearray)):
            raise TypeError("MHL elements must be bytes-like.")
        h.update(blob)
    return h.hexdigest()


def verify_mhl_hash(bundle: MHLBundle, claimed_hash: str) -> bool:
    """A-1 SHA-256 integrity verification step."""
    return bundle.compute_hash().lower() == claimed_hash.lower()
