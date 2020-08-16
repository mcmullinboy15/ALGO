








def handleData():
    def run_Strategy(self):
        self.historicalSetUp(self)
    # if
    while self.clock.is_open:
        mva = 0
        for i in mva_period:
            print(str(i))
            mva += i

        p = 245.54

        if p > mva and shares == 0:
            # buy
            stop_price = p * 0.95
            orderEntity = client.submit_order(symbol=ticker, qty=shares,
                                              side='buy', type=None, time_in_force=None,
                                              limit_price=None, stop_price=stop_price,
                                              client_order_id=None, extended_hours=True)
            pd.Timestamp().isoformat()
            order = client.get_order(orderEntity)
            print('You just bought ' + str(shares) + ' of ' + str(ticker) +
                  ', Here is : your order: ' + order)

        if p < mva and shares != 0:
            # sell
            client.submit_order(symbol=ticker, qty=shares, side='sell',
                                type=None, time_in_force=None,
                                limit_price=None, stop_price=None,
                                client_order_id=None, extended_hours=True)

            print('You just sold ' + str(shares) + ' of ' + str(ticker) +
                  ', Here is : your order: ' + order)
