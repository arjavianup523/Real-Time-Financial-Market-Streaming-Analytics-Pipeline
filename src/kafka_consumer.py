import json

import pymysql
from kafka import KafkaConsumer

from src.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME


KAFKA_TOPIC = "market_data"

KAFKA_SERVER = "localhost:9092"


consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="financial-market-consumer-db",
    value_deserializer=lambda value: json.loads(value.decode("utf-8")),
)


def create_database_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=int(DB_PORT),
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
    )


def save_market_data(market_data):
    connection = create_database_connection()

    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO market_data (
                    symbol,
                    company_name,
                    exchange_name,
                    currency,
                    market_datetime,
                    market_timestamp,
                    open_price,
                    high_price,
                    low_price,
                    close_price,
                    volume,
                    previous_close,
                    price_change,
                    percent_change
                )
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s
                )
            """

            values = (
                market_data.get("symbol"),
                market_data.get("name"),
                market_data.get("exchange"),
                market_data.get("currency"),
                market_data.get("datetime"),
                market_data.get("timestamp"),
                market_data.get("open"),
                market_data.get("high"),
                market_data.get("low"),
                market_data.get("close"),
                market_data.get("volume"),
                market_data.get("previous_close"),
                market_data.get("change"),
                market_data.get("percent_change"),
            )

            cursor.execute(sql, values)

        connection.commit()

    finally:
        connection.close()


def main():
    print(f"Listening for market events from '{KAFKA_TOPIC}'...")

    for message in consumer:
        market_data = message.value

        save_market_data(market_data)

        print(
            f"Saved market event: "
            f"{market_data.get('symbol')} | "
            f"Price: {market_data.get('close')} | "
            f"Volume: {market_data.get('volume')} | "
            f"Time: {market_data.get('datetime')}"
        )


if __name__ == "__main__":
    main()