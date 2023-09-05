import requests
import pandas as pd

def fetch_binance_data(symbol, interval, limit):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'taker_base_vol', 'taker_quote_vol', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df[['timestamp', 'high', 'low']]

btc_data = fetch_binance_data('BTCUSDT', '1h', 720)  # 720 hours = 30 days
eth_data = fetch_binance_data('ETHUSDT', '1h', 720)

with pd.ExcelWriter('crypto_data.xlsx') as writer:
    btc_data.to_excel(writer, sheet_name='BTC', index=False)
    eth_data.to_excel(writer, sheet_name='ETH', index=False)
