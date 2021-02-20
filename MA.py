import alpaca_trade_api as tradeapi
# from Objects import Clients
import numpy
from backtrader import talib
import datetime as date
# from Objects import Clients
# import TimeSpan

today = date.date.today() - date.timedelta(hours=24)
tomorrow = today + date.timedelta(hours=24) + date.timedelta(hours=24)
# timeSpan = TimeSpan(today, tomorrow)
# print(timeSpan)
start = '2019-12-15'
# timeSpan = TimeSpan(start, tomorrow)
PAPER_API_KEY = "PKNEXTZWMDNFB0OFO5IF"
PAPER_API_SECRET = "VnU7e2xcqiOeaVvvuSToMkDrNEIFimnFH2Y32sUN"
PAPER_APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
myPaperClient = tradeapi.REST(PAPER_API_KEY, PAPER_API_SECRET, PAPER_APCA_API_BASE_URL, 'v2')
client = myPaperClient
ticker = 'UGAZ'

mva_period = 30
last_qty = 0.0
last_price = 0.0
buy = 0.0
withoutCash = False
first = True

if withoutCash:
    cash = 0
else:
    cash = 100000.0

initInvestment = cash

array = []
for y in range(mva_period):
    array.append(y)
array.reverse()

clock = client.get_clock()

once = True


def isNow(time):
    now = str(date.datetime.now() - date.timedelta(hours=5) - date.timedelta(minutes=1))
    time = str(time)

    # print('time: {}, now: {}'.format(time, now))
    time = time[0:16]
    now = now[0:16]
    # print('time: {}, now: {}'.format(time, now))

    if time == now:
        print(True)
        return True
    # print(False)
    return False

while True:
    
    while clock.is_open: # and once:
        tickers_data = client.polygon.historic_agg_v2(ticker, 1, 'minute', start, tomorrow).df #timeSpan.getFrom(), timeSpan.getTo()).df
        #print('...data start...\n' + str(tickers_data) + '\n...data done...')
    
        i = 0
        for row in tickers_data.iterrows():
            if i < mva_period - 1:
                i += 1
                continue
    
            mva = 0.0
            for x in array:
                # print('x: '+str(x)+', i-x: '+str(i-x)+', p: '+str(closing_prices[i-x]))
                mva += tickers_data.close[i - x]
            mva = mva / mva_period
            p = row[1].close
            # print('p: '+str(p) + ', mva: ' + str(mva))
    
            # Buy
            if p > mva and buy == 0.0:
                # print('BUY')
                if isNow(row[0]):
                    print('Bought: \t' + str(p) + ' at ' + str(row[0]))
                    last_qty = cash // p
                    last_price = p
                    if withoutCash:
                        if first:
                            initInvestment = p
                            first = False
                        buy = p
                    else:
                        buy = p * last_qty
                        
                    print('Shares: ' + str(last_qty))
                    print('cash: {}, p: {}, lastqty: {}, buy: {}'.format(round(cash, 2), p, last_qty, round(buy, 2)))
                    stop_price = (p * 0.98)
                    print('Buying')
                    # orderEntity = client.submit_order(ticker, last_qty, 'buy', 'limit', 'day', limit_price=stop_price)
                    orderEntity = client.submit_order(ticker, last_qty, 'buy', 'market', 'day')
                    print(orderEntity)
                    print()
    
            # Sell
            if p < mva and buy != 0.0:  # when shorting >= 0:
                # print('Sell')
                if isNow(row[0]):
                    print('Sold: \t\t' + str(p) + ' at ' + str(row[0]))
                    print('Selling')
                    orderEntity = client.submit_order(ticker, last_qty, 'sell', 'market', 'day')
                    print(orderEntity)
                    
                    if withoutCash:
                        cash += p - buy
                    else:
                        cash += p * last_qty - buy  # this_qty = -cash // p # for shorting
    
                    print('cash: {}, p: {}, lastqty: {}, buy: {}'.format(round(cash, 2), p, last_qty, round(buy, 2)))
                    last_price = p
                    buy = 0.0
    
                    print("cash: " + str(round(cash, 2)) + "\n")
                    last_qty = 0
                    if withoutCash:
                        profit = round(cash, 2)
                    else:
                        cash = round(cash, 2)
                        profit = round((cash - initInvestment), 2)
                        print("Initial Investment: \t", initInvestment)
                        print("Remaining Funds: \t\t", cash)
    
                    percent = round(((profit / initInvestment) * 100), 2)
                    print("Total profit: \t\t\t$" + str(profit))
                    print("Total Percent Gain: \t", str(percent) + "%")
                    print()
    
            i += 1
        once = False