# Interactive Snowmelt Energy Balance & Albedo Model

## Overview
This repository contains a full-stack spatial data pipeline and interactive web application designed to calculate real-time snowmelt energy balance across the Colorado Rockies. The model specifically highlights the impact of dust-on-snow (DOS) events by comparing baseline clean snow albedo against an empirical dust-decay albedo model.

👉 **[View the Live Interactive Application Here](https://sofsieh.github.io/albedo-melt-calculator/)**

## The Empirical Model
The core of this project calculates the snowmelt energy (Qm) using a modified energy balance equation. It computes the theoretical melt rate of pristine snow and compares it to the accelerated melt rate caused by observed dust layers.

Qm = (1 - α) * SW_in + LW_net + β(T_air - T_surf) + Qp

**Variables & Constants:**
* `α`: Effective snow albedo. Derived via physical backtracking `α = α_0 - k*C_d`, where `α_0` is clean snow albedo (0.85), `C_d` is dust concentration, and `k` is the site-specific optical sensitivity.
* `SW_in`: Incoming shortwave radiation (W/m²)
* `LW_net`: Net longwave radiation (W/m²)
* `T_surf`: Snow surface temperature (°C), derived via the Stefan-Boltzmann law from upward longwave radiation.
* `β`: Empirical sensible/latent heat exchange coefficient (W/m²°C)
* `Qp`: Precipitation enthalpy (W/m²) calculated from hourly precipitation and air temperature.

## Project Architecture
This project bridges the gap between raw environmental telemetry and interactive public visualization.

1. **Data Ingestion (Python):** Python scripts dynamically fetch 7-day hourly telemetry from the USGS NWIS and NRCS AWDB (SNOTEL) REST APIs.
2. **Processing & Modeling (Pandas/NumPy):** The raw data is standardized. Missing sensor data is safely handled, Imperial units are converted to Metric, and the physical backtracking algorithm establishes current dust loads.
3. **Spatial Conversion (GeoPandas):** The processed DataFrames are merged with site-specific constants (like the `k` value) and exported as standardized GeoJSONs for ArcGIS hosting.
4. **Interactive Web Mapping (JavaScript):** The front-end UI leverages the ArcGIS Maps SDK. When a user clicks the map, the app performs a spatial query (`geometryEngine`) across multiple feature layers concurrently, calculates the real-time energy balance for the nearest station, and renders a comparative analysis using Chart.js.

## Tech Stack
* **Data Processing:** Python, Pandas, NumPy, GeoPandas, Requests
* **Spatial Hosting:** ArcGIS Online (Hosted Feature Layers)
* **Front-End:** HTML5, CSS3, ArcGIS Maps SDK for JavaScript, Chart.js

## Running the Data Pipeline Locally
To update the GeoJSON files with the latest 7-day telemetry:
1. Clone this repository.
2. Ensure you have the necessary spatial libraries installed (e.g., via `conda install -c conda-forge geopandas`).
3. Run `Code1.py` (USGS data) and `Code2.py` (SNOTEL data).
4. Upload the resulting `.geojson` files to your spatial hosting platform.

---
*Developed as part of ongoing research in snow hydrology and environmental engineering.*
