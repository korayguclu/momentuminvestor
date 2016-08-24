import os
import pandas as pd
import csv

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_filaname(path):
  return os.path.join(_ROOT, 'data', path)

def get_asset_name(filename):
  with open(filename, 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    return list(reader)    

def load_asset_data(filename):
  return pd.read_csv('./.tmp/'+filename,sep=';',index_col="Date",parse_dates=True);

def calculate_rsl(data):
  data["Adj Close"]

ohlc_dict = {
    'Open':'first',
    'High':'max',
    'Low':'min',
    'Close':'last',
    'Volume':'sum'
}
c_dict = {
    'Close':'last'
}

if __name__ == '__main__':
  filename =  get_filaname('spdrs_sector.csv')
  assets = get_asset_name(filename)
  for asset in assets:
      asset_name = asset[0]
      asset_desc = asset[1]
      print asset_name
      data = load_asset_data(asset_name)
      close = data['Adj Close'].to_frame()
      close.columns=['Close']
      ac = data.resample('W-Fri', how=c_dict)
      ac['5w_sma'] = ac.rolling(window=27).mean()
      ac['rsl'] =ac['Close'] / ac['5w_sma']
      print type(ac) 
      # close['26w_sma'] = close['Adj Close'].resample('W-FRI').rolling(window=26).mean()
      # close['26w_sma'] = pd.rolling_mean(close['Adj Close'], 26, min_periods=1)
      print ac
