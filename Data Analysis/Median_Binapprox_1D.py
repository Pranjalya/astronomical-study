import numpy as np

def median_bins(values, B):
  mean = np.mean(values)
  std = np.std(values)
  minval = mean - std
  count = sum(map(lambda x: 1 if x<minval else 0, values))
  bin_width = 2*std/B
  bins = np.zeros(B)
  for value in values:
    if value >= minval and value<mean+std :
      bins[int((value - (mean - std))/bin_width)] += 1
  return mean, std, count, bins

def median_approx(values, B):
  mean, std, count, bins = median_bins(values, B)
  ok = -1
  for b, bincount in enumerate(bins):
    count += bincount
    ok = b
    if count >= (len(values)+1)/2:
      break

  width = 2*std/B
  median = mean - std + width*(ok + 0.5)
  return median
  
if __name__ == '__main__':
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
