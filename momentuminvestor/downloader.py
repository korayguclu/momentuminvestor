import os
import pandas as pd

import pandas.io.data as web
import datetime
import csv
from pandas.tseries.offsets import CustomBusinessMonthBegin

end =  datetime.date.today()
start = end - datetime.timedelta(days=365*2)

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_filaname(path):
  return os.path.join(_ROOT, 'data', path)

def get_asset_name(filename):
  with open(filename, 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    return list(reader)    

def get_price_data(asset_name):
  f = web.DataReader(asset_name, 'yahoo', start, end)
  print f.head()    

def convet_daily_data_to_monthly(df):
    #----- build custom calendar -----
    month_index =df.index.to_period('M')
    min_day_in_month_index = pd.to_datetime(df.set_index(month_index, append=True).reset_index(level=0).groupby(level=0)['Open'].min())
    custom_month_starts = CustomBusinessMonthBegin(calendar = min_day_in_month_index)
    #----- convert daily data to monthly data -----
    ohlc_dict = {'Open':'first','High':'max','Low':'min','Close': 'last','Volume': 'sum','Adj Close': 'last'}
    mthly_ohlcva = df.resample(custom_month_starts, how=ohlc_dict)
    return mthly_ohlcva


if __name__ == '__main__':

  filename =  get_filaname('spdrs_sector.csv')
  assets = get_asset_name(filename)
  for asset in assets:
      print "-"*len(asset[0])
      print asset[0] + " :  " +asset[1]
      print "-"*len(asset[0])
      price_data = get_price_data(asset[0])
      print price_data
      print "#####"
  #f = web.DataReader("F", 'yahoo', start, end)
  #print f.head()