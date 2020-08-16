import yahoofinancials

yf = yahoofinancials.YahooFinancials('AAPL')
yfETL = yahoofinancials.YahooFinanceETL("AAPL")
ex = yf.get_exdividend_date()
yield_ = yf.get_dividend_yield()
payout = yf.get_payout_ratio()
close = yf.get_prev_close_price()

print(yf, '\n\n', ex, '\n\n', yield_, '\n\n', payout, '\n\n', close, '\n\n')

start_date = '2019-09-15'
end_date = '2088-09-15'
yahoo_financials = yahoofinancials.YahooFinancials('AAPL')

print(yahoo_financials.get_exdividend_date())
