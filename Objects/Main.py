from datetime import datetime
import ai_demos as ai
from Objects.Trade import Trade
from Strategies.MA import MA

ma_50_firm = MA(length=50, priority='firm', interval='1min', open_close='close', displacement=0)
ma_200_approach = MA(length=200, priority='Approach', interval='1min', open_close='close', displacement=0)

ma_50_firm.run_Strategy()
# nflx = Trade(ticker='nflx', amount=None, shares=4, interval='1min', timeFrame=datetime.now()) # until??

nflx = Trade(ticker='NFLX', shares=3, interval='1min')
price = nflx.getPrice()
print(price)



