"""MHL SHA-256 hash chain."""
import hashlib
from dataclasses import dataclass

@dataclass
class MHLBundle:
    """Five-element MHL disclosure bundle."""
    mhl1_touchstone_bytes: bytes
    mhl2_calibration_history: bytes
    mhl3_variance_statistics: bytes
    mhl4_tdr_boundary: bytes
    laboratory_identifier: str

    def compute_hash(self) -> str:
        return compute_mhl_hash(self.mhl1_touchstone_bytes, self.mhl2_calibration_history, self.mhl3_variance_statistics, self.mhl4_tdr_boundary)

def compute_mhl_hash(mhl1: bytes, mhl2: bytes, mhl3: bytes, mhl4: bytes) -> str:
    """Compute SHA-256 over four MHL byte elements."""
    h = hashlib.sha256()
    for blob in (mhl1, mhl2, mhl3, mhl4):
        if not isinstance(blob, (bytes, bytearray)):
            raise TypeError("MHL elements must be bytes-like.")
        h.update(blob)
    return h.hexdigest()

def verify_mhl_hash(bundle: MHLBundle, claimed_hash: str) -> bool:
    """Verify claimed MHL hash."""
    return bundle.compute_hash().lower() == claimed_hash.lower()
