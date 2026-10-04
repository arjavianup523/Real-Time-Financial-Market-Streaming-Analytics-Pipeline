import json
import time

import requests

from src.config import TWELVE_DATA_API_KEY


API_URL = "https://api.twelvedata.com/quote"

SYMBOL = "AAPL"


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
    print(f"Starting market data producer for {SYMBOL}...")

    while True:
        try:
            market_data = get_market_data()

            print(json.dumps(market_data, indent=2))

        except requests.RequestException as error:
            print(f"API request failed: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")

        time.sleep(10)


if __name__ == "__main__":
    main()