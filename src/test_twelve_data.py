import requests

from src.config import TWELVE_DATA_API_KEY


url = "https://api.twelvedata.com/quote"

params = {
    "symbol": "AAPL",
    "apikey": TWELVE_DATA_API_KEY,
}


response = requests.get(url, params=params, timeout=10)

print("Status code:", response.status_code)

data = response.json()

print(data)