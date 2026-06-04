import json
import ssl
import time
import urllib.error
import urllib.request

# Set the target price threshold for alerting (in USD)
BITCOIN_THRESHOLD = 60000


def get_crypto_prices():
    # Binance API URLs for Bitcoin and Ethereum prices against USDT (Dollar)
    btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    eth_url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

    try:
        # Bypass SSL certificate verification
        context = ssl._create_unverified_context()

        # Fetch Bitcoin price
        with urllib.request.urlopen(
            btc_url, timeout=10, context=context
        ) as response:
            btc_data = json.load(response)

        # Fetch Ethereum price
        with urllib.request.urlopen(
            eth_url, timeout=10, context=context
        ) as response:
            eth_data = json.load(response)

        # Convert price from string to float (decimal number)
        btc_price = float(btc_data["price"])
        eth_price = float(eth_data["price"])

        return btc_price, eth_price

    except (urllib.error.URLError, ValueError, KeyError) as e:
        print(f"An error occurred while fetching data: {e}")
        return None, None


def track_prices():
    print("--- Starting Bitcoin and Ethereum price tracking (Binance API) ---")
    print(f"Bitcoin alert threshold: ${BITCOIN_THRESHOLD}\n")

    while True:
        btc_price, eth_price = get_crypto_prices()

        if btc_price is not None and eth_price is not None:
            # Round the price to 2 decimal places for clean display
            print(
                f"Current prices - Bitcoin: ${btc_price:,.2f}, Ethereum: ${eth_price:,.2f}"
            )

            if btc_price < BITCOIN_THRESHOLD:
                print(
                    f"⚠️ Alert: Bitcoin price has dropped below ${BITCOIN_THRESHOLD}!"
                )
        else:
            print("Unable to retrieve current prices. Retrying...")

        # Pausing for 30 points to comply with API rate limits
        print("Waiting 30 seconds before the next price update...\n")
        time.sleep(30)


if __name__ == "__main__":
    track_prices()
