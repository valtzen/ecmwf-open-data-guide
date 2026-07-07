# ECMWF Open Data: Interactive Guide

Practical Jupyter notebooks for accessing and working with ECMWF forecast data and Copernicus climate services, with a focus on applications for Africa.

> **Status (July 2026):** Written against the mid-2026 catalogue (IFS cycle 50r1, 0.25 degree grid). The Free and Open Data update to 0.1 degree resolution expected later in 2026 may require revisiting the open-data examples (notebooks 01-04). All notebooks last fully verified July 2026.

## Notebooks

Notebooks are ordered by access mechanism, from fully open (no credentials) to registered access, ending with an applied case study.

| # | Notebook | What it covers | Access needed |
|---|----------|----------------|---------------|
| 01 | `01_opendata_catalog` | ECMWF Open Data catalogue: 50r1 naming conventions, browsing the live index, downloading raw GRIB2 | None |
| 02 | `02_opendata_download_methods` | Download methods compared: direct HTTP, the `ecmwf-opendata` client, scripted patterns | None |
| 03 | `03_opendata_earthkit_plots` | Retrieval and plotting with earthkit: IFS vs AIFS, ENS spread, Africa maps, vertical sounding | None |
| 04 | `04_opendata_cloud_endpoints` | Open data from cloud mirrors: AWS S3 byte ranges, Azure STAC, Google Cloud | None |
| 05 | `05_cds_era5_reanalysis` | ERA5 monthly reanalysis via the CDS API: retrieve, load, map | Free CDS account |
| 06 | `06_cds_seas5_seasonal` | SEAS5 seasonal forecasts via CDS: Africa precipitation anomalies (with S2S note) | Free CDS account |
| 07 | `07_ads_cams_dust` | CAMS dust forecast via the ADS API: West Africa case | Free ADS account |
| 08 | `08_wmo_nmhs_data_access` | Operational data access for WMO NMHSs: model levels, LAM/WRF initialisation data (pre-executed) | WMO member NMHS |
| 09 | `09_case_study_elnino_outlook` | Case study: monitoring El Niño impact on African seasonal rainfall with SEAS5 anomalies, drought probabilities, terciles, ensemble plumes | Free CDS account |

## Repository layout

```
notebooks/    the guide (01-09) plus shared helpers (_utils.py, add_attribution.py)
figures/      figures saved by the notebooks, with C3S/ECMWF attribution bars
logos/        official logo files used for figure attribution
data/         local download cache (created at runtime, not committed)
```

## Setup

```bash
conda env create -f environment.yml
conda activate ecmwf-open-data-guide
jupyter lab
```

Notebooks 05-07 and 09 need a CDS/ADS API key: register at https://cds.climate.copernicus.eu and place your key in `~/.cdsapirc` as described there.

## Credentials

The notebooks are independent: any one can be run standalone. Notebook 02 reuses
notebook 01's download when present, and fetches its own otherwise.

- **Notebooks 01-04**: no credentials needed (ECMWF Open Data).
- **Notebooks 05, 06, 09**: need a free CDS account. Register at
  https://cds.climate.copernicus.eu and place your key in `~/.cdsapirc`.
- **Notebook 07**: needs the **ADS** (Atmosphere Data Store), a different endpoint
  from the CDS. Register at https://ads.atmosphere.copernicus.eu. The notebook
  shows how to point the client at the ADS URL; a `.cdsapirc` configured only for
  the CDS will not work for CAMS data.
- **Notebook 08**: needs ECPDS access available to WMO Member NMHSs. It is
  committed pre-executed, so it can be read without credentials.

## Support

- Issues & questions: https://support.ecmwf.int
- Open Data docs: https://confluence.ecmwf.int/display/DAC/ECMWF+open+data
- SEWA programme: https://www.ecmwf.int/en/about/media-centre/focus/2022/ecmwf-lead-eu-funded-project-strengthen-early-warning-systems-africa
