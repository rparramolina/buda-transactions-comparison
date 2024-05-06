from buda import get_transactions


def format_response(transactions_data):
    yearly_data(transactions_data)
    amount_variation, trades_qty_variation = compare_markets(transactions_data, "2023", "2024")
    print(f"porcentual variation between 2023 and 2024 (orders quantity): {round(trades_qty_variation, 2)}%")
    print(f"porcentual variation between 2023 and 2024 (amount): {round(amount_variation, 2)}%")


def yearly_data(transactions_data):
    for year, value in transactions_data.items():
        print(f"{year} total amount: {round(value['total'], 2)} with {value['trades_qty']} trades")
        print(f"commission: {round(value['total'] * 0.08, 2)}")
    return


def compare_markets(transactions_data, year1, year2):
    amount_variation = ((transactions_data[year2]['total'] - transactions_data[year1]['total']) /
                        transactions_data[year1]['total']) * 100
    trades_qty_variation = ((transactions_data[year2]['trades_qty'] - transactions_data[year1]['trades_qty']) /
                            transactions_data[year1]['trades_qty']) * 100

    return amount_variation, trades_qty_variation


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    market = "BTC-CLP"
    # 2024 transactions_data
    # 01-03-2024 23:59:59
    since_timestamp = '1709337599000'
    # 01-03-2024 00:00:00
    until_timestamp = '1709251200000'
    # until_timestamp = '1709272799000'

    print(f"calculating total trade for black buda 2024 BTC-CLP market")
    total_amount_2024, trades_qty_2024 = get_transactions(market, since_timestamp, until_timestamp)

    # 2023 transactions_data
    # 01-03-2023 23:59:59
    since_timestamp = '1677715199000'
    # 01-03-2023 00:00:00
    until_timestamp = '1677628800000'
    print(f"calculating total trade for black buda 2023 BTC-CLP market")
    total_amount_2023, trades_qty_2023 = get_transactions(market, since_timestamp, until_timestamp)
    data = {
        "2024": {
            "total": total_amount_2024,
            "trades_qty": trades_qty_2024
        },
        "2023": {
            "total": total_amount_2023,
            "trades_qty": trades_qty_2023
        }
    }
    print("Results:")
    format_response(data)

    print("Done!")

