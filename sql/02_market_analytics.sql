USE financial_market_analytics;


-- 1. Latest market event
SELECT
    symbol,
    company_name,
    close_price,
    price_change,
    percent_change,
    volume,
    market_datetime,
    received_at
FROM market_data
ORDER BY id DESC
LIMIT 1;


-- 2. Price statistics
SELECT
    symbol,
    MIN(low_price) AS lowest_price,
    MAX(high_price) AS highest_price,
    AVG(close_price) AS average_close_price
FROM market_data
GROUP BY symbol;


-- 3. Total trading volume
SELECT
    symbol,
    SUM(volume) AS total_volume
FROM market_data
GROUP BY symbol;


-- 4. Average percentage change
SELECT
    symbol,
    AVG(percent_change) AS average_percent_change
FROM market_data
GROUP BY symbol;


-- 5. Highest-volume market event
SELECT
    symbol,
    close_price,
    volume,
    market_datetime,
    received_at
FROM market_data
ORDER BY volume DESC
LIMIT 1;


-- 6. Market events ordered by newest first
SELECT
    id,
    symbol,
    close_price,
    price_change,
    percent_change,
    volume,
    received_at
FROM market_data
ORDER BY id DESC;