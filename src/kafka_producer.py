import json
import time

import requests
from kafka import KafkaProducer

from src.config import TWELVE_DATA_API_KEY


API_URL = "https://api.twelvedata.com/quote"

SYMBOL = "AAPL"

KAFKA_TOPIC = "market_data"

KAFKA_SERVER = "localhost:9092"


producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda value: json.dumps(value).encode("utf-8"),
)


def get_market_data():
    params = {
        "symbol": SYMBOL,
        "apikey": TWELVE_DATA_API_KEY,
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def main():
    print(f"Starting Kafka producer for {SYMBOL}...")

    while True:
        try:
            market_data = get_market_data()

            producer.send(
                KAFKA_TOPIC,
                value=market_data,
            )

            producer.flush()

            print(
                f"Sent market event: "
                f"{market_data.get('symbol')} | "
                f"Price: {market_data.get('close')} | "
                f"Time: {market_data.get('datetime')}"
            )

        except requests.RequestException as error:
            print(f"API request failed: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")

        time.sleep(10)


if __name__ == "__main__":
    main()