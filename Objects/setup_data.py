from typing import Optional, Union
from Objects import Clients
import datetime

client = Clients.myPaperClient
clock = client.get_clock()
tdp = datetime.datetime
time = datetime.time


# alpaca or clock/timestamp are in Eastern time and I cant do clock.timestamp.minute
# tdp.now() is from package datetime
def wait_for_market_open():
    print('...running...wait_for_market_open...')
    while is_open() is False:
        now = tdp.now()
        # timestamp = client.get_clock().timestamp
        # if timestamp is '01:01:00:00000':
        # if clo
        # print(clock)

        # print('now' + str(now))
        # time2 = tdp(Union[tdp.year], Union[tdp.month], Union[tdp.day], Union[tdp.hour],
        #             Union[tdp.minute], Union[tdp.second], Union[tdp.microsecond], tzinfo=None)
        # if now.second is 10:
        #     print(now)
        if now.second is 0 and now.microsecond is 000000:  # and now.second is 10 and now.microsecond is 000000:
            print('with Micro: ' + str(now))
            snapshot = client.polygon.snapshot('NFLX')
            print('snapshot: ' + str(snapshot.c))
        # print(time2)
        # grab_premarket_data('1min')


def grab_premarket_data(interval):
    client.get_barset(symbol='NFLX', limit=None, timeframe=None,
                      start='', end='', until=None)


def is_open():
    return clock.is_open


if __name__ == '__main__':
    wait_for_market_open()
