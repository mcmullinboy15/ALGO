import alpaca_trade_api as tradeapi


def alpaca():

    API_KEY = "*****"
    SECRET_KEY = "******"

    api = tradeapi.REST(API_KEY, SECRET_KEY, api_version='v2')

    ticker, multi, timespan, _from, to = 'AAPL', 60, 'minute', '2018-01-01', '2020-06-01'
    df = api.polygon.historic_agg_v2(ticker, multi, timespan, _from=_from, to=to).df
    print(df)
    print(len(df))
    df.to_csv(f'data/{ticker}-{multi}-{timespan}-{_from}-{to}.csv')
