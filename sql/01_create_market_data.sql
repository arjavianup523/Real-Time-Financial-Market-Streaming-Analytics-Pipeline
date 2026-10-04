CREATE DATABASE IF NOT EXISTS financial_market_analytics;

USE financial_market_analytics;

CREATE TABLE IF NOT EXISTS market_data (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    company_name VARCHAR(255),
    exchange_name VARCHAR(100),
    currency VARCHAR(10),
    market_datetime DATE,
    market_timestamp BIGINT,
    open_price DECIMAL(15, 5),
    high_price DECIMAL(15, 5),
    low_price DECIMAL(15, 5),
    close_price DECIMAL(15, 5),
    volume BIGINT,
    previous_close DECIMAL(15, 5),
    price_change DECIMAL(15, 5),
    percent_change DECIMAL(10, 5),
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);