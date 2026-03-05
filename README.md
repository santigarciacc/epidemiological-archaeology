# epidemiological-archaeology
This repository contains the official codebase for the paper: **"Epidemiological Archaeology of SARS-CoV-2: Retrospective Inference of True Incidence via $H^3$ Topological Regularization of Excess Mortality"**.  It provides a scalable mathematical framework to retrospectively reconstruct the true infection and mortality curves of the COVID-19
# 🏛️ Epidemiological Archaeology of SARS-CoV-2

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Research-orange)

This repository contains the official codebase for the paper: **"Epidemiological Archaeology of SARS-CoV-2: Retrospective Inference of True Incidence via $H^3$ Topological Regularization of Excess Mortality"**.

It provides a scalable mathematical framework to retrospectively reconstruct the true infection and mortality curves of the COVID-19 pandemic, bypassing the severe unobservability biases (testing shortages, political opacity) present in official institutional registries.

## 🚀 Features

* **$H^3$ Topological Regularization:** Smooths and filters all-cause excess mortality data using Sobolev spaces to extract pure epidemiological signals.
* **Dynamic IFR (Infection Fatality Ratio):** Adjusts lethality dynamically over time to account for the Wild Type, Alpha/Delta variants, vaccination campaigns, and the Omicron wave.
* **Kinematic Time-Shift Operator:** Applies a robust clinical delay ($\tau = 20$ days) from infection to death.
* **Global Scalability:** Automatically processes data for dozens of countries, calculating unobservability ratios for both infections and mortality.
* **Automated Visualizations:** Generates high-resolution 3-panel epidemiological plots for each analyzed nation.

## 📊 Data Sources
This model seamlessly integrates open datasets:
1. [World Mortality Dataset (WMD)](https://github.com/akarlinsky/world_mortality) for all-cause mortality.
2. [JHU CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19) for official cases, deaths, and demographic baselines.

## ⚙️ Installation and Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/TU_USUARIO/epidemiological-archaeology.git](https://github.com/TU_USUARIO/epidemiological-archaeology.git)
   cd epidemiological-archaeology


   pip install -r requirements.txt
