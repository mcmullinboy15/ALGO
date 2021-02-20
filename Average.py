class Average:
    largest_MVA = 0

    def __init__(self, mva_period, history):
        self.mva_period = mva_period
        self.history = history
        self.closes = self.history.get('Close')
        self.array = []
        for y in range(mva_period):
            self.array.append(y)
        self.array.reverse()

        if mva_period > Average.largest_MVA:
            Average.largest_MVA = mva_period

    def average(self, i):
        mva = 0.0
        for x in self.array:
            # print('x: '+str(x)+', i-x: '+str(i-x)+', p: '+str(self.closes[int(i-x)]))
            mva += self.closes[int(i - x)]
        mva = mva / self.mva_period
        return mva

    def skip_max_rows(self, i):
        if i <= Average.largest_MVA - 1:
            return True
        else:
            return False
