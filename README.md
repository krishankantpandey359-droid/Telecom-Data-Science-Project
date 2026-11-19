# Mobile Phone Specifications Data Analysis

## Project overview

This project explores a 50-record mobile phone specifications dataset using Python and exploratory data analysis. It analyzes connectivity, touch screen, display dimensions, camera specifications, internal memory, battery power, RAM, weight and listed price.

This is a product-specification analysis. It does not contain telecom customer, subscription, billing or churn records.

## Dataset and limitations

The supplied CSV contains 50 product records and 17 columns. The original publisher, sampling frame, currency/unit for Price, measurement units and collection date are not documented. The data therefore supports a reproducible analysis exercise, not claims about the current phone market. Treat all results as descriptive patterns in this sample, not as market-wide findings or causal effects.

## Reusable analysis

`src/phone_data.py` provides:
- CSV loading and strict schema/value validation, including unique product IDs, duplicate-column detection, finite numeric values, positive measurements/prices and yes/no feature flags.
- Descriptive statistics including count, mean, median, standard deviation, quartiles and IQR.
- Spearman rank associations between numeric specifications and listed price.
- Quantile-based price-band summaries for RAM, internal memory, battery power and weight.

The price bands are calculated from this sample's own price distribution. They are not externally defined budget, mid-range or premium market categories. Correlations and group summaries are descriptive, not causal.

## Run locally

```bash
python -m pip install pandas numpy scipy matplotlib seaborn jupyter nbconvert nbformat pytest
python -m pytest -q
```

GitHub Actions runs the data tests and executes non-empty notebook code cells.

## Analysis scope

The project analyzes phone product specifications and listed prices. It must not be described as customer churn prediction or telecom customer behavior analysis. A future prediction extension requires a documented larger dataset, a defined target, a leakage-safe train/test design and a baseline comparison.

## Author

Srishti Pandey, MCA Data Science
