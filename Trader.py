import yfinance as yf
import datetime as date
# from Objects import Clients

'''
data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "SPY AAPL MSFT",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "ytd",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )
'''


class Trader:

    def __init__(self, ticker, cash, realorpaper='paper', period='7d', interval='1m'):
        # self.client = Clients.myRealClient() if realorpaper == 'real' or 'REAL' else Clients.myPaperClient()
        self.ticker = ticker
        self.Ticker = yf.Ticker(ticker)
        # self.info = self.Ticker.info
        # print(self.info)
        # if self.info.get('exDividendDate') is not None:
        #     self.exDate = date.datetime.fromtimestamp(int(self.info.get('exDividendDate'))).strftime(
        #         '%Y-%m-%d %H:%M:%S')
        self.hist = self.Ticker.history(period, interval)
        self.hist['Index'] = range(0, len(self.hist))
        # print(self.hist)
        self.long = 0
        # self.short = 0
        self.cash = cash
        self.initInvestment = cash

        self.last_qty = 0
        self.last_price = 0

    def BUY(self, p, time):
        if not self.isNow(time):

            # print('Bought: \t' + str(p) + ' at ' + str(time))
            self.last_qty = self.cash // p
            self.last_price = p
            # if withoutCash:
            #     if first:
            #         initInvestment = p
            #         first = False
            #     buy = p
            # else:
            self.long = p * self.last_qty

            # print('Shares: ' + str(self.last_qty))
            # print('cash: {}, p: {}, lastqty: {}, buy: {}'.format(round(self.cash, 2), p, self.last_qty, round(self.long, 2)))
            # stop_price = (p * 0.95)
            # print('Buying')

            # orderEntity = self.client.submit_order(self.ticker, self.last_qty, 'buy', 'limit', 'day', limit_price=stop_price)

            # print()

    def SELL(self, p, time):
        if not self.isNow(time):

            # print('Sold: \t\t' + str(p) + ' at ' + str(time))
            # print('Selling')
            # orderEntity = client.submit_order(ticker, last_qty, 'sell', 'market', 'day')
            # print(orderEntity)

            "wait for execution, then get orderEntity's actual price"

            # if withoutCash:
            #     self.cash += p - buy
            # else:
            self.cash += p * self.last_qty - self.long  # this_qty = -cash // p # for shorting

            # print('cash: {}, p: {}, lastqty: {}, buy: {}'.format(round(self.cash, 2), p, self.last_qty, round(self.long, 2)))
            self.last_price = p
            self.long = 0.0

            # print("cash: " + str(round(self.cash, 2)) + "\n")
            self.last_qty = 0
            # if withoutCash:
            #     profit = round(self.cash, 2)
            # else:
            self.cash = round(self.cash, 2)
            profit = round((self.cash - self.initInvestment), 2)
            # print("Initial Investment: \t", self.initInvestment)
            # print("Remaining Funds: \t\t", self.cash)
#
            percent = round(((profit / self.initInvestment) * 100), 2)
            # print("Total profit: \t\t\t$" + str(profit))
            # print("Total Percent Gain: \t", str(percent) + "%")
            # print()
            return percent

    def isNow(self, time):
        now = str(date.datetime.now() + date.timedelta(hours=2) - date.timedelta(minutes=1))
        time = str(time)

        # print('time: {}, now: {}'.format(time, now))
        time = time[0:16]
        now = now[0:16]
        # print('time: {}, now: {}'.format(time, now))

        if time == now:
            # print(True)
            return True
        # print(False)
        return False
