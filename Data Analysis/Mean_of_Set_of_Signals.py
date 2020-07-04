import numpy as np
def mean_datasets(files):
  ans = np.zeros(np.loadtxt(files[0], delimiter=',').shape)
  for file in files:
    ans += np.loadtxt(file, delimiter=',')
  return np.round(ans / len(files), decimals=1)

if __name__ == '__main__':
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
