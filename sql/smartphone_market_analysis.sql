-- SQLite analysis for the supplementary India smartphone dataset.
-- Import data/raw/smartphones_india_cleaned.csv into a table named smartphones first.
-- The imported upstream snapshot is described in docs/DATASET_PROVENANCE.md.
-- Price is listed in INR according to the upstream README. Snapshot collection date is not exact.

-- 1. Data coverage and price range.
SELECT
    COUNT(*) AS phone_models,
    COUNT(DISTINCT brand) AS brands,
    MIN(price_inr) AS min_listed_price_inr,
    ROUND(AVG(price_inr), 2) AS avg_listed_price_inr,
    MAX(price_inr) AS max_listed_price_inr
FROM smartphones;

-- 2. Brand-level coverage and pricing. Use a minimum count to avoid over-reading tiny groups.
SELECT
    brand,
    COUNT(*) AS models,
    ROUND(AVG(price_inr), 2) AS avg_listed_price_inr,
    ROUND(AVG(ram_gb), 2) AS avg_ram_gb,
    ROUND(AVG(battery_mah), 0) AS avg_battery_mah
FROM smartphones
GROUP BY brand
HAVING COUNT(*) >= 3
ORDER BY models DESC, avg_listed_price_inr DESC;

-- 3. Compare average price by RAM capacity.
SELECT
    ram_gb,
    COUNT(*) AS models,
    ROUND(AVG(price_inr), 2) AS avg_listed_price_inr,
    ROUND(AVG(storage_gb), 2) AS avg_storage_gb
FROM smartphones
GROUP BY ram_gb
ORDER BY ram_gb;

-- 4. Connectivity adoption in the supplied sample.
SELECT
    has_5g,
    COUNT(*) AS models,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM smartphones), 2) AS sample_share_pct,
    ROUND(AVG(price_inr), 2) AS avg_listed_price_inr
FROM smartphones
GROUP BY has_5g;

-- 5. Sample-level price vs hardware summaries.
SELECT
    CASE
        WHEN price_inr < 15000 THEN 'Below INR 15k'
        WHEN price_inr < 30000 THEN 'INR 15k-30k'
        WHEN price_inr < 60000 THEN 'INR 30k-60k'
        ELSE 'INR 60k+'
    END AS analyst_defined_price_band,
    COUNT(*) AS models,
    ROUND(AVG(ram_gb), 2) AS avg_ram_gb,
    ROUND(AVG(battery_mah), 0) AS avg_battery_mah,
    ROUND(AVG(display_inches), 2) AS avg_display_inches
FROM smartphones
GROUP BY analyst_defined_price_band
ORDER BY MIN(price_inr);

-- Caution: price bands above are analyst-defined, not upstream market tiers.
-- Listings are a historical scrape snapshot, not a current price comparison feed.
