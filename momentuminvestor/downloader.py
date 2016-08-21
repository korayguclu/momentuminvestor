import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_filaname(path):
    return os.path.join(_ROOT, 'data', path)



if __name__ == '__main__':
  print get_filaname('ishares_equity.csv')