"""
Reusable helpers for the Open Data notebooks.
Keep this small and dependency-light.
"""
from __future__ import annotations
from typing import Optional, Tuple
from pathlib import Path
from datetime import datetime, timedelta, timezone
import os
import math

import earthkit.data as ekd
try:
    import earthkit.plots as ekp
except Exception:
    ekp = None

# ---- Paths -------------------------------------------------------------------
def get_data_dir() -> Path:
    """Single data cache for all notebooks (repo-root /data)."""
    cwd = Path.cwd()
    root = cwd if cwd.name != "notebooks" else cwd.parent
    d = root / "data"
    d.mkdir(parents=True, exist_ok=True)
    return d

def ensure_dir(path: str | os.PathLike) -> str:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return str(p)

# ---- Data loading ------------------------------------------------------------
def load_grib(path: str):
    """Load a local GRIB/GRIB2 (or BUFR/NetCDF if supported) with earthkit-data."""
    return ekd.from_source("file", path)

# ---- Plotting ----------------------------------------------------------------
def quick_plot(field, title=None):
    if ekp is None:
        raise RuntimeError("earthkit.plots not available")
    m = ekp.Map()
    m.quickplot(field)
    if title:
        m.title(title)
    return m

def wind_quiver(u_field, v_field, title: Optional[str] = None, *, nx=40, ny=40):
    if ekp is None:
        raise RuntimeError("earthkit.plots not available; please `pip install earthkit-plots`")
    from earthkit.plots.resample import Subsample
    m = ekp.Map()
    m.quiver(u_field, v_field, resample=Subsample(nx=nx, ny=ny, mode="fixed"))
    if title:
        m.title(title)
    return m

# ---- Model run helper --------------------------------------------------------
def safe_run(model: str = "ifs") -> tuple[str, int]:
    """
    Return (YYYYMMDD, HH) for a 'safe' available run.
    IFS HRES: 00/12; AIFS-single: 00/06/12/18.
    Picks the most recent hour not in the future (UTC).
    """
    now = datetime.now(timezone.utc)
    hours = [0, 12] if model != "aifs-single" else [0, 6, 12, 18]
    hh = max([h for h in hours if h <= now.hour], default=hours[-1])
    d = now if hh <= now.hour else now - timedelta(days=1)
    return d.strftime("%Y%m%d"), hh
