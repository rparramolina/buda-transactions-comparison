import requests
import pandas as pd


# todas las comisiones se cobran en CLP
# considerar GMT-3
# truncar 2 decimales
# moneda_1-moneda_2 cantidad transada en moneda_1 y precio en moneda_2


def get_transactions(market, since_timestamp, until_timestamp):
    trades = _get_trades(market, since_timestamp, until_timestamp)
    trades_qty = len(trades)
    df = pd.DataFrame(trades, columns=['timestamp', 'amount', 'price', 'direction', 'id'])
    df.drop(columns=['id'], inplace=True)
    df['amount_number'] = df['amount'].astype(float)
    df['price_number'] = df['price'].astype(float)
    df['total_trade_clp'] = df['amount_number'] * df['price_number']
    total_amount = df['total_trade_clp'].sum()
    return total_amount, trades_qty


def get_markets():
    url = "https://www.buda.com/api/v2/markets.json"
    response = requests.get(url)
    markets = response.json()
    return markets


def _get_trades(market, since_timestamp, until_timestamp, limit=100):

    trades_response = []
    flag = True
    while flag:
        url = f"https://www.buda.com/api/v2/markets/{market}/trades?timestamp={since_timestamp}&limit={limit}"
        response = requests.get(url)
        trades = response.json()
        since_timestamp = trades['trades']['last_timestamp']
        if since_timestamp <= until_timestamp:
            break

        if len(trades['trades']['entries']) == 0:
            break
        for trade in trades['trades']['entries']:

            if int(trade[0]) < int(until_timestamp):
                flag = False
                break
            trades_response.append(trade)

    return trades_response
