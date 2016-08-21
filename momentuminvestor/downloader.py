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
  df = web.DataReader(asset_name, 'yahoo', start, end)
  return df

def convet_daily_data_to_monthly(df):
    #----- build custom calendar -----
    month_index =df.index.to_period('M')
    min_day_in_month_index = pd.to_datetime(df.set_index(month_index, append=True).reset_index(level=0).groupby(level=0)['Open'].min())
    custom_month_starts = CustomBusinessMonthBegin(calendar = min_day_in_month_index)
    #----- convert daily data to monthly data -----
    ohlc_dict = {'Open':'first','High':'max','Low':'min','Close': 'last','Volume': 'sum','Adj Close': 'last'}
    mthly_ohlcva = df.resample(custom_month_starts, how=ohlc_dict)
    return mthly_ohlcva

def save_price_data(file_name,df):
    directory =  os.path.join(_ROOT, '.tmp')
    if not os.path.exists(directory):
        os.makedirs(directory)
    df.to_csv(os.path.join(directory,file_name), sep=';')  

if __name__ == '__main__':

  filename =  get_filaname('spdrs_sector.csv')
  assets = get_asset_name(filename)
  for asset in assets:
      asset_name = asset[0]
      asset_desc = asset[1]
      print "-"*len(asset_name)
      print asset_name + " :  " +asset_desc
      print "-"*len(asset_name)
      price_data = get_price_data(asset_name)
      save_price_data(asset_name,price_data)
      print price_data
      print "#####"
  #f = web.DataReader("F", 'yahoo', start, end)
  #print f.head()