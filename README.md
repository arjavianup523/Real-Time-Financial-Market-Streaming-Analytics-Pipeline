# Real-Time Financial Market Streaming & Analytics Pipeline

An end-to-end real-time financial market data pipeline built with Python, Kafka, MySQL, Streamlit, Docker, and Twelve Data.

## Architecture

Twelve Data API
        ↓
Python Producer
        ↓
Apache Kafka
        ↓
Python Consumer
        ↓
MySQL
        ↓
SQL Analytics
        ↓
Streamlit Dashboard

## Project Overview

This project demonstrates how real-time financial market data can be collected, streamed through an event-streaming platform, stored in a relational database, analyzed using SQL, and presented through an interactive dashboard.

The pipeline continuously retrieves market data for AAPL from Twelve Data and publishes each market event to a Kafka topic.

A Python Kafka Consumer receives these events and stores them in MySQL.

Streamlit then reads the stored data and displays:

- Latest market price
- Price change
- Percentage change
- Trading volume
- Price history
- Recent market events
- Market summary

## Tech Stack

- Python
- Twelve Data API
- Apache Kafka
- kafka-python
- MySQL
- PyMySQL
- SQL
- Pandas
- Streamlit
- Docker
- Docker Compose
- Git & GitHub

## Project Structure

```text
Real_Time_Financial_Market_Streaming_Analytics_Pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── producer.py
│   ├── kafka_producer.py
│   ├── kafka_consumer.py
│   └── test_twelve_data.py
│
├── sql/
│   ├── 01_create_market_data.sql
│   ├── 02_market_analytics.sql
│   └── 03_create_analytics_views.sql
│
├── dashboard/
│   └── app.py
│
├── tests/
├── notebooks/
│
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
