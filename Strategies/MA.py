import pandas as pd
import alpaca_trade_api as tradeapi
import alpaca_backtrader_api as backtrader
from Objects import Clients
from Objects import setup_data
from Objects.TimeSpan import TimeSpan
from Objects.Trade import Trade
import datetime as date


# import ta-lib


class MA:

    def __init__(self, client, myTrade, length=50, priority='firm', interval='1min', open_close='close',
                 displacement=0):
        self.client = client
        self.length = length
        self.priority = priority
        self.interval = interval
        self.open_close = open_close
        self.displacement = displacement
        self.clock = client.get_clock()
        self.trade = myTrade
        # self.mva = self.setMVA()


        """I need it to create a Trade, should I make the 
        MA params bigger or have a macd.setTrade(ticker, etc..)"""

    def run_Strategy(self):
        # self.historicalSetUp(self)
        # if
        shares = self.trade.shares
        while not self.clock.is_open:
            mva = self.setMVA()
            # for i in mva_period:
            #     print(str(i))
            #     mva += i
            #
            # p = 245.54

            if p > mva and shares == 0:
                # buy
                purchasedAmount = (p * shares)
                stop_price = p * 0.95
                # orderEntity = client.submit_order(symbol=ticker, qty=shares,
                #                                   side='buy', type=None, time_in_force=None,
                #                                   limit_price=None, stop_price=stop_price,
                #                                   client_order_id=None, extended_hours=True)
                pd.Timestamp().isoformat()
                order = 'None'
                # order = client.get_order(orderEntity)
                print('You just bought ' + str(shares) + ' of ' + str(ticker) +
                      ', Here is : your order: ' + order)

            if p < mva and shares != 0:
                # sell
                soldAmount = (p * shares)
                # client.submit_order(symbol=ticker, qty=shares, side='sell',
                #                     type=None, time_in_force=None,
                #                     limit_price=None, stop_price=None,
                #                     client_order_id=None, extended_hours=True)

                print('You just sold ' + str(shares) + ' of ' + str(ticker) +
                      ', Here is : your order: ' + order)

    # def historicalSetUp(self):
    #     mva_period = 7
    #     shares = 0
    #     last_qty = 0
    #     last_price = 0
    #     cash = 1000
    #     history = [cash]
    #
    #     for i in closing_prices:
    #         p = closing_prices[i]
    #         mva = 0.0
    #
    #         for x in range(1, mva_period + 1):
    #             mva += closing_prices[i - x] / mva_period
    #
    #         if p > mva and shares == 0:  # BUY
    #             purchasedAmount = (p * shares)
    #         if p < mva and shares != 0:  # SELL
    #             soldAmount = (p * shares)
    #
    # def extend(self, Trade):
    #     pass

    "I'm not sure if the Index is the number of candle-sticks but maybe" \
    "it's index/2 is the number of candles to look at"

    def setMVA(self):
        var = client.polygon.historic_agg_v2(
            'AAPL', 1, 'minute', _from=self.trade.timeSpan._from, to=self.trade.timeSpan.to, unadjusted=False
        ).df

        mva_period = 7
        mva = 0
        closing_prices = var.close
        start = len(closing_prices)-mva_period
        end = len(closing_prices)
        print('closing: ['+str(closing_prices)+'], start: '+str(start)+', end: '+str(end))
        for x in range(start, end):
            print('p: '+str(closing_prices[x]))
            mva += closing_prices[x]
        mva = mva / mva_period
        print('mva: '+str(mva)+' from {'+str(closing_prices[start])+'}&{'+str(closing_prices[end-1])+'}')
        return mva


if __name__ == '__main__':
    client = Clients.myRealClient
    ticker = 'PCG'

    cash = 1000
    last_qty = 0
    last_price = 0

    # closing_prices = history.close

    # setup_data.wait_for_market_open()

    today = date.date.today() #- date.timedelta(hours=24)
    tomorrow = today + date.timedelta(hours=24)

    # timeSpan = TimeSpan(today, tomorrow)
    timeSpan = TimeSpan('2019-12-13', '2019-12-14')
    aaplTrade = Trade(ticker, shares=30, interval='1min', timeSpan=timeSpan)
    print("aaplTrade: "+str(aaplTrade))
    AAPL_MA = MA(client=client, myTrade=aaplTrade)
    AAPL_MA.run_Strategy()

"""Concrete date type.

Constructors:

__new__()
fromtimestamp()
today()
fromordinal()

Operators:

__repr__, __str__
__eq__, __le__, __lt__, __ge__, __gt__, __hash__
__add__, __radd__, __sub__ (add/radd only with timedelta arg)

Methods:

timetuple()
toordinal()
weekday()
isoweekday(), isocalendar(), isoformat()
ctime()
strftime()

Properties (readonly):
year, month, day
"""
