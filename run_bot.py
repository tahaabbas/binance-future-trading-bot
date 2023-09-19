import requests
from binance.client import Client
from binance.exceptions import BinanceAPIException
import time
import talib
import numpy as np

# Constants
FEE = 0.001  # 0.1%

# Binance API keys
API_KEY = 'YOUR_BINANCE_API_KEY'
API_SECRET = 'YOUR_BINANCE_API_SECRET'

# Telegram settings
ENABLE_TELEGRAM = False
TELEGRAM_API = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'

client = Client(API_KEY, API_SECRET)

def send_telegram_message(message):
    if ENABLE_TELEGRAM:
        url = f"https://api.telegram.org/bot{TELEGRAM_API}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
        requests.get(url)

def get_historical_data(symbol, interval):
    klines = client.futures_klines(symbol=symbol, interval=interval)
    close_prices = [float(entry[4]) for entry in klines]
    return close_prices

def get_latest_price(symbol):
    ticker = client.futures_ticker(symbol=symbol)
    return float(ticker['lastPrice'])

def place_order(symbol, side, leverage):
    try:
        # Set leverage
        client.futures_change_leverage(symbol=symbol, leverage=leverage)
        # Place order
        order = client.futures_create_order(symbol=symbol, side=side, type='MARKET', quantity=1)  # Adjust quantity as needed
        return order
    except BinanceAPIException as e:
        send_telegram_message(f"Error placing {side} order: {e.message}")
        return None

def close_order(symbol, side):
    """Close existing order based on the side (BUY/SELL)"""
    try:
        open_orders = client.futures_get_open_orders(symbol=symbol)
        for order in open_orders:
            if order['side'] == side:
                client.futures_cancel_order(symbol=symbol, orderId=order['orderId'])
                send_telegram_message(f"Closed {side} order.")
    except BinanceAPIException as e:
        send_telegram_message(f"Error closing {side} order: {e.message}")

def main(symbol, short_ema_period, long_ema_period, interval, leverage):
    last_action = None
    while True:
        try:
            close_prices = get_historical_data(symbol, interval)
            short_ema = talib.EMA(np.array(close_prices), timeperiod=short_ema_period)[-1]
            long_ema = talib.EMA(np.array(close_prices), timeperiod=long_ema_period)[-1]
            latest_price = get_latest_price(symbol)

            if short_ema > long_ema and last_action != 'BUY':
                close_order(symbol, 'SELL')
                order = place_order(symbol, 'BUY', leverage)
                if order and order['status'] == 'FILLED':
                    last_action = 'BUY'
                    send_telegram_message(f"Placed BUY order at {latest_price}. Short EMA: {short_ema}, Long EMA: {long_ema}")

            elif short_ema < long_ema and last_action != 'SELL':
                close_order(symbol, 'BUY')
                order = place_order(symbol, 'SELL', leverage)
                if order and order['status'] == 'FILLED':
                    last_action = 'SELL'
                    send_telegram_message(f"Placed SELL order at {latest_price}. Short EMA: {short_ema}, Long EMA: {long_ema}")

            time.sleep(60)  # Wait for 1 minute before the next iteration

        except requests.exceptions.Timeout:
            send_telegram_message("Timeout error when communicating with Binance's API. Retrying...")
            continue

if __name__ == "__main__":
    # Example usage: python script_name.py BTCUSDT 8 20 1h 10
    import sys
    symbol = sys.argv[1]
    short_ema_period = int(sys.argv[2])
    long_ema_period = int(sys.argv[3])
    interval = sys.argv[4]
    leverage = int(sys.argv[5])

    main(symbol, short_ema_period, long_ema_period, interval, leverage)
