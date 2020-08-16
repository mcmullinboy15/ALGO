import time

from Strategy import Strategy
import pandas as pd

class MovingAverage(Strategy):
    def __init__(self, size, init_price):
        super(MovingAverage, self).__init__()

        self.size = float(size)
        self.last_val = [float(init_price)] * size
        self.average = sum(self.last_val) / len(self.last_val)


    def __str__(self):
        return f"Moving Average:\n"\
               f"\tSize: {self.size}\n"\
               f"\tAverage: {self.average}"

    def __len__(self):
        return self.size

    def __abs__(self):
        return self.average

    def add(self, add_val):
        add_val = float(add_val)

        self.last_val = self.last_val[1:]
        # print(self.last_val)

        self.last_val.append(add_val)
        # print(self.last_val)

        self.average = sum(self.last_val) / len(self.last_val)


df = pd.read_csv('.././data/AAPL-1-day-2018-01-01-2020-06-01.csv', index_col=0)
print(df)
mv10 = MovingAverage(10, 150)
mv180 = MovingAverage(180, 150)
long_short = 0

profit = 0
last_price = 0

for i, row in df.iterrows():
    mv10.add(row.close)
    mv180.add(row.close)
    # print(abs(mv10) < abs(mv180), abs(mv10), abs(mv180))

    if abs(mv10) < abs(mv180) and long_short >= 0:

        if long_short != 0:
            profit += row.close - last_price
        print(f"SELL @ {profit}\t{row.close}\t{last_price}")


        last_price = row.close
        long_short = -1
        # time.sleep(1)

    if abs(mv10) > abs(mv180) and long_short <= 0:

        if long_short != 0:
            profit -= row.close - last_price

        print(f"BUY @ {profit}\t{row.close}\t{last_price}")


        last_price = row.close
        long_short = 1
        # time.sleep(1)

print("\n\n\n\nRESET\n\n\n\n")
profit = 0
last_price = 0
last_histo = 0
long_short = 0

for i, row in df.iterrows():
    mv10.add(row.close)
    mv180.add(row.close)

    histo = abs(mv10) - abs(mv180)


    if last_histo > histo and long_short >= 0:

        if long_short != 0:
            profit += row.close - last_price
        print(f"{profit}\tSELL @ {row.close}\t{last_price}")


        last_price = row.close
        long_short = -1
        # time.sleep(1)

    if last_histo < histo and long_short <= 0:

        if long_short != 0:
            profit -= row.close - last_price

        print(f"{profit}\tBUY @ {row.close}\t{last_price}")


        last_price = row.close
        long_short = 1
        # time.sleep(1)