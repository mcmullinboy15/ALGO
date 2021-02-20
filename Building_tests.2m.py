from SAVE_data import SAVE_data
import Trader
from Average import Average
import matplotlib.pyplot as plt

mva1_array = []
mva2_array = []

symbol = 'HKD=x'
save_data = SAVE_data(path='C:/amcmullin/IdeaProjects/Python/Yahoo/', name='' + str(symbol) + '_2m_Test.csv')

# mva1s = [10, 20]
# mva2s = [20, 30]
# intervals = ['1m']

mva1s = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240,
         250, 260, 270, 280, 290, 300]
mva2s = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240,
         250, 260, 270, 280, 290, 300]
intervals = ['2m']

percents = []

for interval in intervals:
    for mva_1 in mva1s:
        for mva_2 in mva2s:

            data = Trader(symbol, cash=100000, interval=interval)
            average1 = Average(mva_1, data.hist)
            average2 = Average(mva_2, data.hist)

            temp = 0
            mva1_array = []
            mva2_array = []

            for row in data.hist.iterrows():
                time = row[0]
                p = row[1].Close
                i = row[1].Index

                if average1.skip_max_rows(i):
                    continue

                mva1 = average1.average(i)
                mva2 = average2.average(i)
                mva1_array.append(mva1)
                mva2_array.append(mva2)
                # print('mva1', mva1,'mva2', mva2)

                # Buy
                if mva1 > mva2 and data.long == 0.0:  # if i'm not long
                    data.BUY(p, row[0])

                # Sell
                if mva1 < mva2 and data.long != 0.0:  # if i'm not short
                    temp = data.SELL(p, row[0])

            add = save_data.add_to(interval, mva_1, mva_2, temp)
            print('::', interval, ',', add)
            save_data.save()

save_data.save_and_clean()
