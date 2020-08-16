from Objects import Clients
import datetime


# client = Clients.myPaperClient
# clock = client.get_clock()
# tdp = datetime.datetime
# isLong = False
# isShort = False


class Trade:
    """I want to make it so if I just pass in amount='$500' it will calculate the shares,
    but if I wanted I could also pass in the shares=50 and self.amount will be calculated"""

    def __init__(self, ticker=None, amount=None, shares=None, interval=None, timeSpan=None):
        self.ticker = ticker
        self.amount = amount  # TODO like (shares * self.getPrice())
        self.shares = shares
        # untested
        if self.shares is None:
            self.shares = (self.amount / self.getPrice())
        self.interval = interval
        self.timeSpan = timeSpan
        self.client = Clients.myPaperClient
        self.polygon = Clients.myPaperClient.polygon

    """tbc: convert to shares"""

    def setAmount(self, amount):
        self.amount = amount

    # Not functional
    # def getPrice(self):
    #     time = tdp.now()
    #     return self.polygon.historic_agg(self.shares, self.ticker, time, to=None, limit=None)

    def isLong(self):
        isLong = True
        isShort = False
        return isLong

    def isShort(self):
        isShort = True
        isLong = False
        return isShort

    # BackLog
    def until(self):
        return self.timeSpan

    def __str__(self):
        return "ticker: " + str(self.ticker) + ", amount: " + str(self.amount) + \
               ", shares: " + str(self.shares) + ", interval: " + str(self.interval) + ", timeSpan: " + str(self.timeSpan)

    def getPrice(self):
        pass
