from Objects import Clients


class polygon_wrapper:

    def __init__(self, type, symbol):
        if type == 'paper':
            self.client = Clients.myPaperClient()
        if type == 'real':
            self.client = Clients.myRealClient()

        self.ply = self.client.polygon
        self.financials = self.ply.financials(symbol=symbol)


if __name__ == '__main__':
    pw = polygon_wrapper('paper', 'AAPL')
    for i in pw.financials.__iter__():
        print(i)
