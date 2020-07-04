import numpy as np

def calc_stats(filepath):
  values = np.loadtxt(filepath, delimiter=',')
  return (np.round(np.mean(values), decimals=1), np.round(np.median(values), decimals=1))

if __name__ == '__main__':
  mean = calc_stats('data.csv')
  print(mean)