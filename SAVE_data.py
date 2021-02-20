import numpy
import pandas as pd
from pandas import DataFrame


class SAVE_data:

# add another column for how  fast  it was to finish  the comparison

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.num = 0
        self.df = pd.DataFrame(columns=list('I12P'))

    def add_to(self, interval, mva1, mva2, percent):
        self.df.loc[self.num] = [interval] + [mva1] + list((mva2, percent))
        text = '' + str(mva1) + ',' + str(mva2) + ',' + str(percent) + '%\n'
        self.num += 1
        return text

    def save_and_clean(self):
        self.save()
        self.clean()

    def save(self):
        self.df.to_csv(self.name)

    def clean(self, rm_equals=False, rm_neg=False, rm_below=-100000):
        for row in self.df.iterrows():
            print(row)

            if rm_equals:
                if row[0] == row[1]:
                    print(row[0])
                    row = None
                else:
                    print(row[0])

            if rm_neg:
                if int(row[3]) < 0:
                    row = None

            if int(row[3]) < rm_below:
                row=None

        self.save()
