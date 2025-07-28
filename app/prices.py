from twelvedata import TDClient
from twelvedata.client import DefaultHttpClient
from settings import twelvedata_api_key, https_proxy
from typing import Dict
from datetime import datetime, timezone
from pydantic import BaseModel

http_client = DefaultHttpClient("https://api.twelvedata.com/")
print(f"{datetime.now()}: Using HTTPS proxy: '{https_proxy}'")
if https_proxy:
    http_client.session.proxies = {
        "http": https_proxy,
        "https": https_proxy,
    }

td = TDClient(apikey=twelvedata_api_key, http_client=http_client)

prices: Dict[str, float] = {}
prices_timestamp = datetime.fromtimestamp(0, tz=timezone.utc)


class PriceInfo(BaseModel):
    price: float
    timestamp: datetime


def fetch_last_price(symbol: str) -> float:
    """Fetch the last price of a stock symbol."""
    price_data = td.price(symbol=symbol).as_json()
    if isinstance(price_data, dict) and "price" in price_data:
        print(f"{datetime.now()}: Fetched data for {symbol}: {price_data}")
        return float(price_data["price"])
    raise ValueError(f"Invalid price data for symbol {symbol}: {price_data}")


def update_prices():
    """Function to update prices of stocks."""
    for symbol in ["GOOGL", "NVDA", "USD/CHF"]:
        prices[symbol] = fetch_last_price(symbol)
        print(f"{datetime.now()}: Updated price for {symbol}: {prices[symbol]}")


def last_price(symbol: str) -> PriceInfo:
    """Function to get the price of a stock."""
    global prices_timestamp
    since_update = datetime.now(tz=timezone.utc) - prices_timestamp
    if since_update.total_seconds() > 600:  # 10 minutes
        update_prices()
        prices_timestamp = datetime.now(tz=timezone.utc)
    else:
        update_sec = 600 - since_update.total_seconds()
        print(
            f"{datetime.now()}: Using cached price for {symbol}. Will update in {update_sec} seconds."
        )

    internal_symbol = symbol.replace("_", "/")
    return PriceInfo(price=prices[internal_symbol], timestamp=prices_timestamp)
