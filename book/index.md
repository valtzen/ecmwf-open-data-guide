# ECMWF Open Data — Interactive Guide

**A practical introduction to ECMWF forecast data and Copernicus climate services.**  
Notebooks run standalone in Jupyter or as a rendered JupyterBook.

---

## What this guide covers

### A — ECMWF Open Data

Free, globally accessible weather forecast data — no credentials needed.

| Notebook | What you learn |
|---|---|
| **A01** Catalog & access mechanisms | What's in the catalogue, 50r1 naming, browse the live index, download GRIB2 |
| **A02** Retrieval & plotting with earthkit | `ecmwf-opendata` client, IFS vs AIFS comparison, ENS spread, Africa maps, vertical profile |
| **A03** Cloud endpoints | AWS S3 HTTP Range, Azure STAC, Google Cloud — single-parameter slicing |

### B — Copernicus Services (CDS / ADS)

Free climate reanalysis, seasonal forecasts, and atmosphere monitoring via the Copernicus Data Store.

| Notebook | What you learn |
|---|---|
| **B01** ERA5 reanalysis | `cdsapi` + `earthkit.data`, ERA5 download, Africa climate baseline |
| **B02** Seasonal forecasts | SEAS5 monthly precipitation anomalies, ensemble spread, Africa domain |
| **B03** CAMS dust | Atmosphere Data Store (ADS), dust aerosol optical depth, West Africa |

### C — SOFF (WMO Members)

Higher-resolution operational data for WMO National Meteorological Services. Pre-executed notebook — no credentials required to view.

| Notebook | What you learn |
|---|---|
| **C01** SOFF access | FTP structure, filename convention, model levels for WRF/LAM init, CCSDS conversion |

---

## Getting started

**Run in Jupyter (recommended):**

```bash
conda env create -f env/environment.yml
conda activate ecmwf-open-data-guide
jupyter lab
```

**Run in browser (no install):**  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valtzen/ecmwf-open-data-guide/main)

---

## Data access summary

| Tier | Credentials | Grid | Best for |
|---|---|---|---|
| ECMWF Open Data | None | 0.25° (9km late 2026) | Explore, prototype, train |
| Copernicus CDS/ADS | Free account | 0.25° (ERA5) / varies | Reanalysis, seasonal, CAMS |
| SOFF | WMO account (`wmo_xx`) | 0.1°, 137 model levels | Operational LAM/WRF init |

---

*Part of the [SEWA programme](https://www.ecmwf.int/en/about/media-centre/focus/2022/ecmwf-lead-eu-funded-project-strengthen-early-warning-systems-africa) data and infrastructure support.*  
*Questions: [support.ecmwf.int](https://support.ecmwf.int)*
