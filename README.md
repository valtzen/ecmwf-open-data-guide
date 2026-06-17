# ECMWF Open Data: Interactive Guide

Practical Jupyter notebooks for accessing and working with ECMWF forecast data and Copernicus climate services.

## Notebooks

**A: ECMWF Open Data** (no credentials)
- `A01`: Catalog & access mechanisms (50r1 naming, browse live index, download GRIB2)
- `A02`: Retrieval & plotting with earthkit (IFS vs AIFS, ENS spread, Africa maps, sounding)
- `A03`: Cloud endpoints (AWS S3 HTTP Range, Azure STAC, Google Cloud)

**B: Copernicus CDS / ADS** (free account)
- `B01`: ERA5 reanalysis via CDS
- `B02`: SEAS5 seasonal forecasts (Africa precipitation anomalies)
- `B03`: CAMS dust (West Africa, ADS)

**C: SOFF** (WMO members, pre-executed)
- `C01`: WMO NMHS operational data access, model levels, WRF/LAM initialisation

## Setup

```bash
conda env create -f env/environment.yml
conda activate ecmwf-open-data-guide
jupyter lab
```

## Build the JupyterBook

```bash
jupyter-book build book
# open book/_build/html/index.html
```

## Support

- Issues & questions: https://support.ecmwf.int
- Open Data docs: https://confluence.ecmwf.int/display/DAC/ECMWF+open+data
- SEWA programme: https://www.ecmwf.int/en/about/media-centre/focus/2022/ecmwf-lead-eu-funded-project-strengthen-early-warning-systems-africa
