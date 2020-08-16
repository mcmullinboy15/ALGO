from pylivetrader import 
import numpy as np

def initialize(context):
    context.fnv=sid(41886)#franco nevada corp
    context.rgld=sid(6455)#royal gold corp

    schedule_function(trade, date_rules.every_day(), time_rules.market_open(minutes = 65))

def trade(context, data):
    rgld_avg = np.mean(data.history(context.rgld,'price',5,'1d')) # The Number is day(moving average)
    fnv_avg = np.mean(data.history(context.fnv,'price',5,'1d'))
    spread_avg = (rgld_avg - fnv_avg)

    rgld_curr = data.current(context.rgld,'price')
    fnv_curr = data.current(context.fnv,'price')
    spread_curr = (rgld_curr - fnv_curr)
    print("rgld_curr, fnv_curr, spread_avg, spread_curr,spread_curr/spread_avg: ",rgld_curr,fnv_curr,spread_avg,spread_curr,spread_curr/spread_avg)

    # 1.10 is the standard deviation or the bands
    if spread_curr > spread_avg*1.10:#detect a wide spread
        print("wide: spread_avg, spread_curr: ",spread_avg,spread_curr)

        order_target_percent(context.rgld,0.50)
        order_target_percent(context.fnv,-0.50)

    # .90 is the standard deviation or the bands
    elif spread_curr < spread_avg*.90:#detect a tight spread
        print("tight: spread_avg, spread_curr: ",spread_avg,spread_curr)
        order_target_percent(context.rgld,0.50)
        order_target_percent(context.fnv,-0.50)
    else:
        pass