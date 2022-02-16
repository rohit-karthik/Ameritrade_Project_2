from ameritrade_class import TDAmeritradeClient

client = TDAmeritradeClient(
    "ameritrade_creds.json",
    "AM7MWDYZKMK6WUWSFVAHA3GXW15ONALN"
)

# client.get_price_history('MSFT', 'day', 1, 'minute')
# client.get_price_history('MSFT', 'month', 1, 'daily')
# client.get_price_history('MSFT', 'year', 1, 'daily')

client.get_price_history('BBY', 'day', 1, 'minute')
client.get_price_history('BBY', 'month', 1, 'daily')
client.get_price_history('BBY', 'year', 1, 'daily')
client.get_price_history('BBY', 'ytd', 1, 'daily')

# client.get_price_history('AMZN', 'day', 1, 'minute')
# client.get_price_history('AAPL', 'day', 1, 'minute')
# client.get_price_history('GOOGL', 'day', 1, 'minute')
# client.get_price_history('BBY', 'day', 1, 'minute')

# get_price_history('month', 1, 'daily')
# get_price_history('year', 1, 'weekly')

# while True:
#     """res = grab_quotes()
#
#     print(res.json())
#     timeElapsed += 5"""
#
#     if timeElapsed > 1740:
#         refresh_access_token()
#
#     time.sleep(5)
