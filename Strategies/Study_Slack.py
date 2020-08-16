from backtrader import talib
import datetime as date

from Objects import Clients


class Study(object):
    def __init__(self, history):
        self.history = history
        self.bullishPattern = self.bullishCandleStickPatterns(history.iloc[-1], history.iloc[-2], history.iloc[-3])

    def addEMA(self, length):
        try:
            self.history['EMA' + str(length)] = talib.EMA(self.history['close'], timeperiod=length)
        except Exception as e:
            return None

    def addSMA(self, length):
        try:
            self.history['EMA' + str(length)] = talib.SMA(self.history['close'], timeperiod=length)
        except Exception as e:
            return None

    def addVWAP(self):
        try:
            df = self.history
            df = df.assign(
                vwap=df.eval(
                    'wgtd = close * volume', inplace=False
                ).groupby(df.index.date).cumsum().eval('wgtd / volume')
            )
            self.history['VWAP'] = df['vwap']
        except Exception as e:
            return None

    def addMACD(self, fast, slow, signal):
        try:
            macd, signalline, macdhist = talib.MACD(
                self.history['close'],
                fastperiod=fast,
                slowperiod=slow,
                signalperiod=signal
            )
            self.history['MACD_F' + str(fast) + '_S' + str(slow) + '_L' + str(signal) + '_SIGNAL'] = macd - signalline
            self.history['MACD_F' + str(fast) + '_S' + str(slow) + '_L' + str(signal) + '_MACD'] = macd
            self.history['MACD_F' + str(fast) + '_S' + str(slow) + '_L' + str(signal) + '_SL'] = signalline
            self.history['MACD_F' + str(fast) + '_S' + str(slow) + '_L' + str(signal) + '_HIST'] = macdhist
        except Exception as e:
            return None

    def addRSI(self, length):
        try:
            self.history['RSI' + str(length)] = talib.RSI(self.history['close'], timeperiod=length)
        except Exception as e:
            return None

    def addBBANDS(self, length, devup, devdn, type):
        try:
            up, mid, low = talib.BBANDS(self.history['close'], timeperiod=length, nbdevup=devup, nbdevdn=devdn,
                                        matype=type)
            bbp = (self.history['close'] - low) / (up - low)
            self.history['BBANDS' + str(length) + '_bbp'] = bbp
            self.history['BBANDS' + str(length) + '_up'] = up
            self.history['BBANDS' + str(length) + '_low'] = low
            self.history['BBANDS' + str(length) + '_mid'] = mid
        except Exception as e:
            return None

    def bullishCandleStickPatterns(self, c1, c2, c3):
        pattern = None
        # LOCH bullish
        if c1.low < c1.open < c1.close <= c1.high and \
                c1.high - c1.close < c1.open - c1.low and \
                c1.close - c1.open < c1.open - c1.low:
            pattern = 'hammer'
        if c1.low <= c1.open < c1.close < c1.high and \
                c1.high - c1.close > c1.open - c1.low and \
                c1.close - c1.open < c1.high - c1.close:
            pattern = 'inverseHammer'
        # LCOH bearish
        if c2.low < c2.close < c2.open < c2.high and \
                c1.low <= c1.open < c1.close < c1.high and \
                c1.open < c2.close and \
                c1.close - c1.open > c2.open - c2.close:
            pattern = 'bullishEngulfing'
        if c2.low < c2.close < c2.open < c2.high and \
                c1.low <= c1.open < c1.close < c1.high and \
                c1.open < c2.close and \
                c1.close > c2.close + (c2.open - c2.close) / 2:
            pattern = 'piercingLine'
        if c3.low < c3.close < c3.open < c3.high and \
                c1.low <= c1.open < c1.close < c1.high and \
                abs(c2.open - c2.close) < abs(c3.open - c3.close) and \
                abs(c2.open - c2.close) < abs(c1.open - c1.close):
            pattern = 'morningStar'
        if c3.low <= c3.open < c3.close < c3.high and \
                c2.low <= c2.open < c2.close < c2.high and \
                c1.low <= c1.open < c1.close < c1.high and \
                c3.close <= c2.open and \
                c2.close <= c1.open:
            pattern = 'threeWhiteSoldiers'
        return pattern

    def getHistory(self):
        return self.history


def main():
    today = date.date.today() - date.timedelta(hours=24)
    tomorrow = today + date.timedelta(hours=24)  # - date.timedelta(hours=24)

    # not working
    history = Clients.myRealClient.polygon.historic_agg_v2(
        'AAPL', 1, 'minute', _from=today, to=tomorrow, unadjusted=False
    ).df
    print(history)

    # usage:
    study = Study(history)  # history is daily bars
    study.addRSI(14)
    studyHistory = study.getHistory()
    # if study.bullishPattern is not None and \
    #     studyHistory['RSI14'][-1] < 40:
    print(studyHistory)


if __name__ == '__main__': main()
