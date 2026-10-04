USE financial_market_analytics;


-- =========================================================
-- 1. Market Summary View
-- =========================================================

CREATE OR REPLACE VIEW market_summary AS
SELECT
    symbol,
    COUNT(*) AS total_events,
    MIN(low_price) AS lowest_price,
    MAX(high_price) AS highest_price,
    AVG(close_price) AS average_close_price,
    SUM(volume) AS total_volume,
    AVG(percent_change) AS average_percent_change
FROM market_data
GROUP BY symbol;


-- =========================================================
-- 2. Latest Market Data View
-- =========================================================

CREATE OR REPLACE VIEW latest_market_data AS
SELECT
    id,
    symbol,
    company_name,
    exchange_name,
    currency,
    market_datetime,
    open_price,
    high_price,
    low_price,
    close_price,
    volume,
    previous_close,
    price_change,
    percent_change,
    received_at
FROM market_data
WHERE id = (
    SELECT MAX(id)
    FROM market_data
);


-- =========================================================
-- 3. Price Performance View
-- =========================================================

CREATE OR REPLACE VIEW price_performance AS
SELECT
    symbol,
    market_datetime,
    open_price,
    close_price,
    price_change,
    percent_change,
    volume,
    received_at
FROM market_data
ORDER BY received_at;


-- =========================================================
-- 4. High Volume Events View
-- =========================================================

CREATE OR REPLACE VIEW high_volume_events AS
SELECT
    id,
    symbol,
    close_price,
    volume,
    price_change,
    percent_change,
    received_at
FROM market_data
ORDER BY volume DESC;