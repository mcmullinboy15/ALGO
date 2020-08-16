# Matthew Rock the Bomb.com

import alpaca_trade_api as tradeapi
# from Objects import Clients
import numpy
# import talib as ta
from backtrader import talib
import datetime as date
from Objects import Clients
from Objects.TimeSpan import TimeSpan

close = numpy.random.random(100)
# output = talib.SMA(close)
# print(output)


# from livewires import colour as color

# client = tradeapi.REST("AKVNXPP4VONAE7MBAX7S", "TeNc1VpUfGhaLPzJsWLLF66vfo2HFU7174z/3RX5", "https://paper-api.alpaca.markets", 'v2')
# Calls GET /bars/{timeframe} for the given symbols, and returns a Barset with limit Bar objects for each of the the requested symbols. timeframe can be one of minute, 1Min, 5Min, 15Min, day or 1D. minute is an alias of 1Min. Similarly, day is an alias of 1D. start, end, after, and until need to be string format, which you can obtain with pd.Timestamp().isoformat() after cannot be used with start and until cannot be used with end.

today = date.date.today() - date.timedelta(hours=24)
tomorrow = today + date.timedelta(hours=24)
# timeSpan = TimeSpan(today, tomorrow)
timeSpan = TimeSpan('2019-12-05', '2019-12-14')
client = Clients.myDataClient
ticker = 'HOME'

# barset = client.get_barset('AAPL', '1Min').df  # , '2019-10-8', '2019-10-10').df
# tickers_data = client.polygon.historic_agg('day', 'AAPL', '2019-1-1', '2019-12-30').df  # dataBase format
tickers_data = client.polygon.historic_agg_v2(ticker, 1, 'minute', timeSpan.getFrom(), timeSpan.getTo(),
                                              unadjusted=False, limit=None).df
print('...data start...\n' + str(tickers_data) + '\n...data done...')
print()

mva_period = 7
# dates = tickers_data.get('time')
closing_prices = tickers_data.close
# closing_prices = barset
last_qty = 0
last_price = 0
cash = 700
history = [cash]

print('len(closing_prices): ' + str(len(closing_prices)))
print()

i = 0
# for i in range(mva_period, len(closing_prices)):
for row in tickers_data.iterrows():
    # print(str(row[0]) + " ::: " + str(row[1].close))
    p = row[1].close
    mva = 0.0
    # print('p: ' + str(p))
    # print('last_qty: ' + str(last_qty))
    # print('last_price: ' + str(last_price))

    # calculate moving average
    # for x in range(1, mva_period + 1):
    for x in [6, 5, 4, 3, 2, 1, 0]:
        # print('x: '+str(x)+', i-x: '+str(i-x)+', p: '+str(closing_prices[i-x]))
        mva += closing_prices[i - x]
    mva = mva / mva_period

    # print('p: '+str(p))
    # print('mva: ' + str(mva))

    # Sell
    if p > (mva * 1.02) and last_qty > 0:  # when shorting >= 0:
        print('last_qty: ' + str(last_qty))
        print('Sell: ' + str(p))
        print("Sell_last_price: " + str(last_price))

        print('if ' + str(row[0]) + ' is ' + str(date.datetime.now()))
        if row[0] is date.datetime.now():
            print('Sell')
            orderEntity = client.submit_order(symbol=ticker, qty=last_qty, side='sell',
                                              type=None, time_in_force=None, limit_price=None,
                                              stop_price=None, client_order_id=None, extended_hours=True)

        # this_qty = -cash // p # for shorting
        cash = last_qty * p  # - last_price * last_qty
        last_price = p
        last_qty = 0

        print("Sell_last_qty: " + str(last_qty))
        print("cash: " + str(int(cash)) + "\n")

    # Buy
    if p < (mva * 0.98) and last_qty <= 0:
        print('last_qty: ' + str(last_qty))
        print('Buy: ' + str(p))
        print("Buy_last_price: " + str(last_price))

        print('if ' + str(row[0]) + ' is ' + str(date.datetime.now()))
        if row[0] is date.datetime.now():
            # stop_price = (p * 0.95)
            print('Buy')
            orderEntity = client.submit_order(symbol=ticker, qty=last_qty, side='buy',
                                              type=None, time_in_force=None, limit_price=None,
                                              stop_price=None, client_order_id=None, extended_hours=True)
        this_qty = cash // p
        cash = this_qty * p  # + last_qty * last_price
        last_price = p
        last_qty = this_qty

        print("Buy_last_qty: " + str(last_qty))
        print("cash: " + str(int(cash)) + "\n")

    history.append(cash)
    i += 1

# print(cash)
# hist_frame(closing_prices)
# closing_prices.plot()                                 # Can help you understand how it is working
# rolling_ave = closing_prices.rolling(mva_period)  # the current moving average

# if __name__ == '__main__': main()
