# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

portfolio = {
  "AAPL": {
    "volume": 10,
    "strike": 154.12
  },
  "GOOG": {
    "volume": 2,
    "strike": 812.56
  },
  "TSLA": {
    "volume": 12,
    "strike": 342.12
  },
  "FB": {
    "volume": 18,
    "strike": 209.0
  }
}

print(portfolio['TSLA']['volume'])

print(portfolio['GOOG']['strike'])

market = {
  "AAPL":  198.84,
  "GOOG": 1217.93,
  "TSLA":  267.66,
  "FB":    179.06
}

pnl = 0

for stock in portfolio.keys():
    print(stock)
    current_price = market[stock] * portfolio[stock]['volume']
    strike_price = portfolio[stock]['strike'] * portfolio[stock]['volume']
    pnl += current_price - strike_price

print(pnl)

    



