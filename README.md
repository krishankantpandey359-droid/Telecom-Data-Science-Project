# Mobile Phone Specifications Analysis

Python-based exploratory analysis of smartphone product specifications and listed prices. The repository contains two separate datasets and analysis tracks. They are not merged.

## Track 1: Original notebook exercise

- File: `Telecom Dataset.csv`
- Shape: 50 product records × 17 columns
- Used by: `Telecom_Data_Science_Project_COMPLETE (1).ipynb` and `src/phone_data.py`
- Topics: connectivity, touch screen, display dimensions, camera specifications, internal memory, battery power, RAM, weight and listed price.

This is a small product-specification exercise. It contains no telecom subscribers, billing records, usage history or churn labels. It must not be presented as telecom customer analytics or churn prediction.

## Track 2: Supplementary India smartphone dataset

- File: `data/raw/smartphones_india_cleaned.csv`
- Shape: 758 product records × 29 columns
- Upstream repository: [abhinavflac/smartphone-specs-india](https://github.com/abhinavflac/smartphone-specs-india)
- Upstream data file: [smartphones_cleaned.csv](https://github.com/abhinavflac/smartphone-specs-india/blob/main/data/processed/smartphones_cleaned.csv)
- Dataset page: [Kaggle Smartphones Cleaned Dataset](https://www.kaggle.com/datasets/githubmasterin/smartphones-cleaned-dataset)
- Upstream repository states CC0 1.0 Universal. See [dataset provenance](docs/DATASET_PROVENANCE.md).

This separate dataset is the basis for `sql/smartphone_market_analysis.sql`. Import it into SQLite as a table named `smartphones` before running the queries. It contains brand, model, INR listed price, processor, RAM, storage, connectivity, display, battery and camera fields.

The upstream README describes 1,007 scraped listings reduced to 758 cleaned records. It labels the data India / 2025, but does not give an exact collection date. Prices are a historical scrape snapshot, not live prices.

## Reusable Python analysis

`src/phone_data.py` works with Track 1's 50 × 17 dataset. It provides:
- Strict schema and value validation.
- Descriptive statistics: count, mean, median, standard deviation, quartiles and IQR.
- Spearman rank associations between numeric specifications and listed price.
- Quantile-based summaries of sample price bands.

These bands are calculated from the 50-row sample. They are not market-defined budget, mid-range or premium tiers. Correlation and group summaries are descriptive, not causal.

## Run locally

```bash
python -m pip install pandas numpy scipy matplotlib seaborn jupyter nbconvert nbformat pytest
python -m pytest -q
```

GitHub Actions runs the dataset tests and executes non-empty notebook code cells. The supplementary SQL queries are provided as a separate analysis track and require a SQLite import step.

## Data limitations

- Neither dataset represents telecom customers or subscriber behaviour.
- Track 1 has only 50 records and its original source, currency and collection date are undocumented.
- Track 2 has 758 scraped product records. The exact collection date is not documented, and product coverage reflects upstream filtering.
- Do not treat either sample as a complete census of the Indian smartphone market.
- Do not infer that a specification causes a higher price.
- Check source terms and preserve provenance when reusing scraped data.

## Author

Srishti Pandey, MCA Data Science
