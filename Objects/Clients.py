import alpaca_trade_api as tradeapi

PAPER_API_KEY = "PK2GKXD44ZJJCWB5WJ9C"
PAPER_API_SECRET = "8cuJv1Rleaj0enpiGUjQGJhbpXT92AmdKIixuu20"
PAPER_APCA_API_BASE_URL = "https://paper-api.alpaca.markets"


def myPaperClient():
    return tradeapi.REST(PAPER_API_KEY, PAPER_API_SECRET, PAPER_APCA_API_BASE_URL, 'v2')


REAL_API_KEY = "AKGARBDBVCOROU6PHPC7"
REAL_API_SECRET = "Z0dTzvUrZtKq5Ya4HhNuq6lFgV6ZCtpTMi5Ehu5p"
REAL_APCA_API_BASE_URL = "https://api.alpaca.markets"


def myRealClient():
    return tradeapi.REST(REAL_API_KEY, REAL_API_SECRET, REAL_APCA_API_BASE_URL, 'v2')


APCA_API_DATA_URL = "https://data.alpaca.markets"


def myDataClient():
    return tradeapi.REST(REAL_API_KEY, REAL_API_SECRET, APCA_API_DATA_URL, 'v2')


# APCA_Endpoint = "https://paper-api.alpaca.markets" \
#                 + getTIME_SERIES() \
#                 + "&symbol=" + getTicker() \
#                 + "&interval=" + getInterval() \
#                 + "&outputsize=" + getOutputsize() \
#                 + "&apikey=" + getAlphavantage_API_Key()

Alphavantage_API_KEY_ID = "H5XE5TXZN7S7KU47"

# Alphavantage_Endpoint = "https://www.alphavantage.co/query?" \
#                         + "function=" + getTIME_SERIES() \
#                         + "&symbol=" + getTicker() \
#                         + "&interval=" + getInterval() \
#                         + "&outputsize=" + getOutputsize() \
#                         + "&apikey=" + getAlphavantage_API_KEY_ID()

IEX_Cloud_StableURL = "https://cloud.iexapis.com/stable/"
IEX_Cloud_Publishable_API = "pk_3edca43437bc4009af508a44a7d0924b"
IEX_Cloud_Secret_API = "sk_148db4004fcf428fa70fb0a764cbfc3a"
