# Mobile Phone Specifications Data Analysis

## 📌 Project Overview

This project explores a 50-record mobile phone specifications dataset using Python and exploratory data analysis.

The analysis covers connectivity, touch screen, display dimensions, camera specifications, internal memory, battery power, RAM, weight and price.

## 🎯 Objectives

- Understand the mobile phone specifications dataset
- Inspect rows, columns and data types
- Check missing values and duplicate records
- Perform data cleaning
- Perform Exploratory Data Analysis (EDA)
- Analyse numerical and categorical variables
- Create meaningful data visualisations
- Study relationships between numerical variables
- Explore relationships between phone specifications and price
- Generate useful data-driven insights

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Google Colab

## 🔍 Project Workflow

1. Data Loading
2. Data Inspection
3. Data Cleaning
4. Descriptive Statistics
5. Exploratory Data Analysis
6. Data Visualisation
7. Correlation Analysis
8. Phone Specification Analysis
9. Key Findings
10. Conclusion

## 📊 Analysis Performed

The project includes analysis of:

- Mobile phone hardware and device specifications
- Numerical variables
- Categorical variables
- Connectivity and device features
- Phone price and hardware specifications
- Phone price patterns
- Relationships between numerical variables

## 📈 Visualisations

The notebook contains different visualisations such as:

- Histograms
- Bar charts
- Box plots
- Count plots
- Correlation heatmap
- Phone specification comparisons

## 💡 Key Learning Outcomes

Through this project, I learned how to:

- Work with a mobile phone dataset
- Use Pandas for data analysis
- Clean and prepare data
- Perform Exploratory Data Analysis
- Create data visualisations
- Interpret statistical results
- Explore relationships between phone features and price
- Follow a structured Data Science workflow

## 📝 Conclusion

This project demonstrates a practical Data Science workflow using mobile phone specifications data. The analysis explores device features and their relationships with phone prices. It does not analyse telecom customers, subscriptions, billing, or churn.

The project can be extended with a larger, documented mobile phone dataset and a clearly defined prediction objective, such as estimating price from device specifications.

## 👩‍💻 Project Author

**Srishti Pandey**

MCA Data Science Student

**Project:** Mobile Phone Specifications Data Analysis


## Dataset integrity and automated checks

The notebook embeds a 50-row, 17-column mobile-phone specifications dataset. The project is a product-specification EDA exercise, not a telecom customer churn analysis. The embedded CSV is tested directly from the notebook source for row count, required columns, unique product IDs, finite non-negative numeric values, and yes/no feature flags.

Run the dataset checks locally:

```bash
python -m pip install pandas pytest
python -m pytest -q
```

GitHub Actions runs these checks and executes every non-empty notebook code cell. The CI artifact contains the executed notebook.


## Reusable analysis module

`src/phone_data.py` adds a reproducible CSV-based analysis path alongside the notebook:

- `load_phone_data(path)` loads the repository CSV and validates it.
- `validate_phone_data(frame)` checks the exact schema, unique product IDs, yes/no feature flags, missing values and finite non-negative numeric specifications.
- `summarize_phone_data(frame)` reports count, mean, median, standard deviation, quartiles and IQR.
- `price_rank_correlations(frame)` ranks numeric specifications by Spearman association with the supplied listed-price field.

Run the reusable checks from the repository root:

```bash
python -m pip install pandas numpy pytest
python -m pytest -q
```

The CSV and notebook are educational samples of 50 products. The dataset source, sampling frame, price currency and collection date are not documented. Treat associations as descriptive only. The project does not contain customer, subscription, billing or churn records.
