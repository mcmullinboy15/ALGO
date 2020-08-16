from ZZ_Libraries import alpaca_trade_api as tradeapi

from BeginnerPractice import Read_A_CSV

API_KEY = "PKL89E7KIDDGRV43UUA2"
API_SECRET = "pTLJPN4NRZzy5VhCedATlmEziupczCPYtSjJDZcr/fhOXNrHVcmGZY"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"


def run_strategy(var14=None, var16=None):
    # orders = self.alpaca.list_orders(status="open")
    # order = tSubmitOrder = threading.Thread(target=self.submitOrder(
    #     qty, position.symbol, orderSide, respSO))
    # or
    # order = threading.Thread(target=self.submitOrder('NFLX', 3, 'buy'))
    # print('order' + order)

    print('runStrategy...')
    var1 = True

    Read_A_CSV.runCSV('NFLX')
    var3 = Read_A_CSV.allRows
    print("var3: " + str(var3))

    # while var2.hasNext():
    #     var5 = var2.nextFloat()
    #     var3.add(var5)

    # var2.close()

    var28 = var3
    var6 = 9
    var7 = 0.0
    var9 = 7
    var10 = 0.0
    var12 = -1.0
    var14 = 0.0
    # var16 = 0.0
    var18 = var28  # Float[]
    var19 = var28.__sizeof__()
    counter = 0
    for var21 in var3:
        var21 = float(var21)
        # for(var20 = 0 var20 < var19 ++var20):
        # var21 = var18[var22]  # var20] # Float
        if var6 > var9:
            # avg = (float(var28[var6 - 1]) + float(var28[var6 - 2]) + float(var28[var6 - 3]) + float(var28[var6 - 4])
            #        + float(var28[var6 - 5]) + float(var28[var6 - 6]) + float(var28[var6 - 7]))
            avg = (float(var28[counter - 1]) + float(var28[counter - 2]) + float(var28[counter - 3]) + float(
                var28[counter - 4])
                   + float(var28[counter - 5]) + float(var28[counter - 6]) + float(var28[counter - 7]))

            # print('avg: ' + avg)
            var7 = (float(avg) / float(var9))

            if var21 < var7 * 0.95 and var10 == 0.0:
                var10 = var21
                print("Buying on day " + str(var6) + " at price: " + str(var21))
                var12 = 0.0
                if var16 == 0.0:
                    var16 = var21

            elif var21 > var7 * 1.05 and var12 == 0.0:
                var12 = var21
                var14 = var14 + (var12 - var10)
                print("Selling on day " + str(var6) + " at price: " + str(var21))
                print("Trade profit: " + str(float(var12) - float(var10)))
                var10 = 0.0

        if counter > var19:
            counter += var9
        ++var6
        calcProfit()

    def calcProfit():
        print("Total Profit: " + str(var14))
        print("Total Returns: " + str(var14 / var16))


class MR:
    alpaca = None

    # var14 = 0.0
    # var16 = 0.0

    def __init__(self):
        self.alpaca = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, 'v2')
        stockUniverse = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP',
                         'SPLK', 'BA', 'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC',
                         'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', 'OKTA', 'TWTR',
                         'TM', 'RTN', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM', ]

        # Format the allStocks variable for use in the class.
        self.allStocks = []
        for stock in stockUniverse:
            self.allStocks.append([stock, 0])

        self.long = []
        self.short = []
        self.qShort = None
        self.qLong = None
        self.adjustedQLong = None
        self.adjustedQShort = None
        self.blacklist = set()
        self.longAmount = 0
        self.shortAmount = 0
        self.timeToClose = None


ms = MR()
run_strategy()
