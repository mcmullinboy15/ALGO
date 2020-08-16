# /**
# * what if I put all this in the Strategies Class and made it so their not abstract but all static
# */
# class Data:


# def __init__(self):
    # /**
    # * for "-" add '...&& !inputLine.contains("Last Refreshed")...' to the if statment
    # */
variables = "-", "open\":", "high\":", "low\":", "close\":", "volume\":"  # []
TIME_SERIES = "TIME_SERIES_INTRADAY"
ticker = ""
interval = "1min"
outputsize = "full"
stats = None  # Stats[]


def setStatsArray(statsArray):
    print("Setting Stats[] ... ")
    stats = statsArray


def getStatsArray():
    return stats


def getVariables():  # []
    return variables


def getTIME_SERIES():
    return TIME_SERIES


# /**
# * TIME_SERIES_INTRADAY, TIME_SERIES_DAILY, TIME_SERIES_DAILY_ADJUSTED, TIME_SERIES_WEEKLY,
# * TIME_SERIES_WEEKLY_ADJUSTED, TIME_SERIES_MONTHLY, TIME_SERIES_MONTHLY_ADJUSTED
# * @param newTIME_SERIES
#          */
def setTIME_SERIES(newTIME_SERIES):
    print("Setting TIME_SERIES to ... " + newTIME_SERIES)
    TIME_SERIES = newTIME_SERIES


def getTicker():
    return dotCSV_Logic("withOut")


def getTicker_CSV():
    return dotCSV_Logic("with")


# /**
# * pass "with" or "withOut" depending if you want or don't want the '.csv'
# **/

@staticmethod
def dotCSV_Logic(withCSV):
    ticker = None  # set to Feild
    # ticker2 = None
    if withCSV == "with":
        if ticker.contains(".csv"):
            ticker += ".csv"
        else:
            ticker = ticker
    elif withCSV == "withOut":
        if ticker.contains(".csv"):
            ticker = ticker[ticker.find(".")]
        else:
            ticker = ticker

    # Throw this exception when ticker is None
    # print("MAKE SURE THAT YOU INITIALIZED THE TICKER YOU WISH TO USE")

    return ticker


def setTicker(newTicker):
    print("Setting Ticker to ... " + newTicker)
    ticker = newTicker


def getInterval():
    return interval


# /**
# * 1min, 5min, 15min, 30min, 60min
# * @param newInterval
# */
def setInterval(newInterval):
    print("Setting Interval to ... " + newInterval)
    interval = newInterval


def getOutputsize():
    return outputsize


# /**
# * compact, full
# * @param newOutputsize
# */
def setOutputsize(newOutputsize):
    print("Setting Outputsize to ... " + newOutputsize)
    outputsize = newOutputsize


# class Stats:
# List<> timeStamp = new ArrayList<>()
# List<Float> open = new ArrayList<>()
# List<Float> high = new ArrayList<>()
# List<Float> low = new ArrayList<>()
# List<Float> close = new ArrayList<>()
# List<Float> volume = new ArrayList<>()

# // Getters and Setters for Stock Variables
# // Getters could return a List<Float> too
# def __init__(self):
timeStamp = None
open = None
high = None
low = None
close = None
volume = None


def getTimeStamp():  # String[]
    return timeStamp.toArray()


def addTimeStamp(timeStamp_temp):  # String
    timeStamp.add(timeStamp_temp)


def getOpen():  # Float[]
    return open.toArray()


def addOpen(Open_temp):  # Float
    open.add(Open_temp)


def getHigh():  # Float[]
    return high.toArray()


def addHigh(High_temp):  # Float
    high.add(High_temp)


def getLow():  # Float[]
    return low.toArray()


def addLow(Low_temp):  # Float
    low.add(Low_temp)


def getClose():  # Float[]
    return close.toArray()


def addClose(Close_temp):  # Float
    close.add(Close_temp)


def getVolume():  # Float[]
    return volume.toArray()


def addVolume(Volume_temp):  # Float
    volume.add(Volume_temp)
