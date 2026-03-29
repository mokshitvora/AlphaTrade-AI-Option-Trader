import yfinance as yf
def get_market_data():
  current_nifty =  yf.Ticker("^NSEI")

  current_vix = yf.Ticker("^VIX")
  info = current_nifty.info
  current_price = info["regularMarketPrice"]
  percentage_change = info["regularMarketChangePercent"]
  fifty_day_moving_average = info["fiftyDayAverage"]
  two_hundred_day_moving_average = info["twoHundredDayAverage"]
  fiftytwo_week_high = info["fiftyTwoWeekHigh"]
  fiftytwo_week_low = info["fiftyTwoWeekLow"]
  vix_level = current_vix.info["regularMarketPrice"]
  return {"current_price" : current_price, "percentage_change" : percentage_change, "fifty_day_moving_average" : fifty_day_moving_average, "two_hundred_day_moving_average" : two_hundred_day_moving_average, "fiftytwo_week_high" : fiftytwo_week_high, "fiftytwo_week_low" : fiftytwo_week_low, "vix_level" : vix_level}

