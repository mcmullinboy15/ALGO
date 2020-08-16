import alpaca_trade_api as tradeapi
import numpy
from backtrader import talib
from Objects import Clients
import datetime as date


class SetupAlgo:

    def __init__(self,
                 client=Clients.myPaperClient(),
                 symbol='TSLA',
                 multiplier=1,
                 timeSpan='minute',
                 _from='2019-12-10',
                 to='2019-12-28',

                 mva_period_1=3,
                 mva_period_2=30,

                 last_qty=0.0,
                 last_price=0.0,
                 buy=0.0,
                 cash=100000,

                 withoutCash=False,
                 first=True,
                 once=True
                 ):

        self.client = client
        self.symbol = symbol
        self.multiplier = multiplier
        self.timeSpan = timeSpan
        self._from = _from
        self.to = to
        self.mva_period_1 = mva_period_1
        self.mva_period_2 = mva_period_2
        self.last_qty = last_qty
        self.last_price = last_price
        self.buy = buy
        self.withoutCash = withoutCash
        self.first = first
        self.once = once
        self.cash = cash
        if withoutCash:
            self.cash = 0
        self.initInvestment = self.cash

    def asdfasdf(self):
        today = date.date.today() - date.timedelta(hours=24)
        tomorrow = today + date.timedelta(hours=24) + date.timedelta(hours=24)

    def isNow(self, time, twoHourOffset=False, OhioServerOffset5H1M=True):
        now = None
        if OhioServerOffset5H1M:
            now = str(date.datetime.now() - date.timedelta(hours=5) - date.timedelta(minutes=1))
        elif twoHourOffset:
            now = str(date.datetime.now() - date.timedelta(hours=2))
        time = str(time)

        # print('time: {}, now: {}'.format(time, now))
        time = time[0:16]
        now = now[0:16]
        # print('time: {}, now: {}'.format(time, now))

        if time == now:
            print(True)
            return True
        # print(False)
        return True  # False



# client = Clients.myPaperClient()
#
# symbol = 'TSLA'
# multiplier = 1
# timespan = 'minute'
# _from = '2019-12-10'
# to = '2019-12-28'
#
# mva_period_1 = 3
# mva_period_2 = 30
#
# last_qty = 0.0
# last_price = 0.0
# buy = 0.0
# withoutCash = False
# first = True
#
# if withoutCash:
#     cash = 0
# else:
#     cash = 100000.0
#
# initInvestment = cash

array_1 = []
for y in range(mva_period_1):
    array_1.append(y)
array_1.reverse()
array_2 = []
for y in range(mva_period_2):
    array_2.append(y)
array_2.reverse()

clock = client.get_clock()
