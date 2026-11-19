# Supplementary dataset provenance

## Dataset

- Name: Smartphones Cleaned Dataset, India
- Upstream repository: https://github.com/abhinavflac/smartphone-specs-india
- Upstream data file: https://github.com/abhinavflac/smartphone-specs-india/blob/main/data/processed/smartphones_cleaned.csv
- Dataset page: https://www.kaggle.com/datasets/githubmasterin/smartphones-cleaned-dataset
- Upstream license file: https://github.com/abhinavflac/smartphone-specs-india/blob/main/LICENSE
- License stated by upstream repository: CC0 1.0 Universal
- Upstream README describes a scrape of Smartprix.com, with 1,007 extracted listings reduced to 758 cleaned smartphone records and 29 engineered features.
- Imported file: `data/raw/smartphones_india_cleaned.csv`
- Imported rows: 758
- Imported columns: 29
- Upstream README labels the dataset as India / 2025. The exact collection date is not specified in the README.

## Field names

- `brand`
- `model`
- `price_inr`
- `rating_score`
- `processor_brand`
- `processor_name`
- `core_count`
- `clock_speed_ghz`
- `ram_gb`
- `storage_gb`
- `has_5g`
- `has_vo5g`
- `has_volte`
- `has_nfc`
- `has_ir_blaster`
- `display_inches`
- `res_width_px`
- `res_height_px`
- `refresh_rate_hz`
- `battery_mah`
- `charging_watt`
- `fast_charging`
- `rear_camera_count`
- `front_camera_count`
- `rear_camera_main_mp`
- `front_camera_main_mp`
- `os_name`
- `memory_card_supported`
- `memory_card_type`

The upstream README describes the following fields: brand, model, price_inr, rating_score, processor_brand, processor_name, core_count, clock_speed_ghz, ram_gb, storage_gb, display_inches, res_width_px, res_height_px, refresh_rate_hz, battery_mah, charging_watt, fast_charging, rear_camera_count, front_camera_count, rear_camera_main_mp, front_camera_main_mp, has_5g, has_vo5g, has_volte, has_nfc, has_ir_blaster, os_name, memory_card_supported, and memory_card_type.

## Interpretation and quality caveats

- The upstream README states prices are in INR and gives an approximate observed range of ₹5,000 to ₹150,000+.
- The exact collection date is not documented. Prices and product availability change over time.
- The upstream data was scraped from Smartprix. Treat the dataset as a historical snapshot, not a live market feed.
- Check duplicate models, missing values, implausible specifications, and price outliers before analysis.
- Upstream filtering rules include minimum battery, display, RAM, processor, and OS requirements. This means the dataset is not a complete census of every phone category.
- CC0 is the license declared by the upstream dataset repository. Preserve attribution and the source link as good practice. Verify third-party rights and platform terms before redistributing scraped content.

## Attribution

Dataset and cleaning workflow by the upstream repository owner. Source: abhinavflac/smartphone-specs-india and its linked Kaggle dataset. No endorsement by Smartprix or Kaggle is implied.
