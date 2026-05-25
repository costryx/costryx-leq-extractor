"""Costryx-standard L_eq(f) spectrum visualization."""
from typing import Optional, Dict
import numpy as np

COSTRYX_COLOR_GREEN = "#2ECC71"
COSTRYX_COLOR_YELLOW = "#F39C12"
COSTRYX_COLOR_RED = "#E74C3C"
ANCHOR_MARKERS = {"OP1": "o", "OP2": "s", "OP3": "^"}

def plot_leq_spectrum_standard(spectrum: Dict[str, np.ndarray], anchors, sigma_leq_band: Optional[np.ndarray] = None, mhl_hash_short: Optional[str] = None, title: Optional[str] = None, save_path: Optional[str] = None):
    """Plot continuous L_eq(f) spectrum following the Costryx visual standard."""
    import matplotlib.pyplot as plt
    f_ghz = spectrum["frequency"] / 1e9
    leq_mm = spectrum["L_eq"] * 1e3
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(f_ghz, leq_mm, color="#1F2D3D", linewidth=1.5, label="L_eq(f)", zorder=3)
    if sigma_leq_band is not None:
        sb_mm = np.asarray(sigma_leq_band) * 1e3
        if sb_mm.shape != leq_mm.shape:
            raise ValueError("sigma_leq_band shape mismatch")
        ax.fill_between(f_ghz, leq_mm - sb_mm, leq_mm + sb_mm, color="#1F2D3D", alpha=0.15, label="±sigma_Leq", zorder=2)
    for op_name, (f_anchor, lbnd) in [("OP1", anchors.OP1), ("OP2", anchors.OP2), ("OP3", anchors.OP3)]:
        ax.axhline(lbnd * 1e3, linestyle="--", linewidth=1.2, color="#7F8C8D", alpha=0.7)
        ax.text(f_ghz.max() * 0.99, lbnd * 1e3, f" {op_name}: L_eq,bnd={lbnd*1e3:.2f} mm", va="bottom", ha="right", fontsize=8, color="#7F8C8D")
    ax.axhspan(0, anchors.OP3[1] * 1e3, color=COSTRYX_COLOR_GREEN, alpha=0.08, zorder=0)
    ax.axhspan(anchors.OP3[1] * 1e3, anchors.OP3[1] * 1e3 * 1.5, color=COSTRYX_COLOR_YELLOW, alpha=0.10, zorder=0)
    ax.axhspan(anchors.OP3[1] * 1e3 * 1.5, anchors.OP3[1] * 1e3 * 3.0, color=COSTRYX_COLOR_RED, alpha=0.10, zorder=0)
    for op_name, (f_anchor, _) in [("OP1", anchors.OP1), ("OP2", anchors.OP2), ("OP3", anchors.OP3)]:
        f_anchor_ghz = f_anchor / 1e9
        if f_ghz.min() <= f_anchor_ghz <= f_ghz.max():
            idx = int(np.argmin(np.abs(f_ghz - f_anchor_ghz)))
            ax.plot(f_anchor_ghz, leq_mm[idx], marker=ANCHOR_MARKERS[op_name], markersize=10, markerfacecolor="white", markeredgecolor="#1F2D3D", markeredgewidth=1.5, label=f"{op_name} ({f_anchor_ghz:.0f} GHz)", zorder=4, linestyle="None")
    ax.set_xlabel("Frequency (GHz)", fontsize=11)
    ax.set_ylabel("L_eq (mm)", fontsize=11)
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
    if title:
        ax.set_title(title, fontsize=12)
    if mhl_hash_short:
        ax.text(0.99, 0.02, f"MHL: {mhl_hash_short}", transform=ax.transAxes, ha="right", va="bottom", fontsize=8, family="monospace", color="#7F8C8D")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=200, bbox_inches="tight")
    return fig, ax

