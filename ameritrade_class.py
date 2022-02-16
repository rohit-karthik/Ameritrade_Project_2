import time
import json
import requests
import matplotlib.pyplot as plt


class TDAmeritradeClient:
    def __init__(self, creds_file_name, client_id):
        self.creds_file_name = creds_file_name
        self.creds_file = open(creds_file_name)
        self.creds = json.load(self.creds_file)
        self.client_id = client_id

    def grab_quotes(self, ticker_symbol):
        get_url = f"https://api.tdameritrade.com/v1/marketdata/{ticker_symbol}/quotes?apikey={self.client_id}"
        grab_quotes_response = requests.get(get_url, headers={
            "Authorization": f"Bearer {self.creds['access_token']}"
        })
        return grab_quotes_response

    def refresh_access_token(self):
        post_url = "https://api.tdameritrade.com/v1/oauth2/token"

        refresh_access_response = requests.post(post_url, data={
            "grant_type": "refresh_token",
            "refresh_token": self.creds['refresh_token'],
            "client_id": f"{self.client_id}"
        })
        self.creds['access_token'] = refresh_access_response.json()['access_token']

        with open(self.creds_file_name, "w") as creds_file_write:
            json.dump(self.creds, creds_file_write)

    def get_price_history(self, ticker_symbol, period_range, period, frequency_type):
        history_url = f"https://api.tdameritrade.com/v1/marketdata/{ticker_symbol}/pricehistory"

        price_history_response = requests.get(history_url, headers={
            "Authorization": f"Bearer {self.creds['access_token']}"
        }, params={
            'apiKey': f"{self.client_id}",
            'periodType': period_range,
            'period': period,
            'frequencyType': frequency_type
        })

        history_dict = price_history_response.json()
        # print(history_dict)

        x_vals = []  # date and time array - used for displaying the labels
        y_vals = []  # closing prices
        num_vals = []  # 0 - end array - used for actually graphing (counter)

        for i in range(len(history_dict['candles'])):
            # if frequency_type == "minute":
            # print(history_dict['candles'][i]['datetime'])
            x_vals.append(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(history_dict['candles'][i]['datetime'] / 1000)))
            num_vals.append(i)
            y_vals.append(history_dict['candles'][i]['close'])

        tick_int = int(len(x_vals) / 2)  # halfway point

        # print(num_vals)

        plot_color = "green" if y_vals[0] < y_vals[len(y_vals) - 1] else "red"

        plt.plot(num_vals, y_vals, color=plot_color)
        plt.xticks([0, tick_int, tick_int * 2], [x_vals[0], x_vals[tick_int], x_vals[tick_int * 2 - 1]])
        plt.xlabel(f'{frequency_type.capitalize()} for Last {period_range}')
        plt.ylabel('Closing price')
        plt.title(f'Closing Prices for {ticker_symbol}')
        plt.show()
