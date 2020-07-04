# Import the running_stats function
from helper import running_stats
from astropy.io import fits
import numpy as np

def median_bins_fits(paths, B):
  mean, std = running_stats(paths)
  minval = mean - std
  bin_width = 2*std/B
  bins = np.zeros((mean.shape[0], mean.shape[1], B))
  count = np.zeros(mean.shape)
  
  for path in paths:
    data = fits.open(path)[0].data
    for i in range(data.shape[0]):
      for j in range(data.shape[1]):
        if data[i, j] < minval[i, j]:
          count[i, j] += 1
        elif data[i, j] < mean[i, j] + std[i, j]:
          bins[i, j, int((data[i, j] - (mean[i, j] - std[i, j]))/bin_width[i, j])] += 1
  return mean, std, count, bins

def median_approx_fits(paths, B):
  mean, std, count, bins = median_bins_fits(paths, B)
  median = np.zeros(mean.shape)
  width = 2*std/B
  for i in range(mean.shape[0]):
    for j in range(mean.shape[1]):
      for b, bincount in enumerate(bins[i, j]):
        count[i, j] += bincount
        if count[i, j] >= (len(paths)+1)/2:
          break
      median[i, j] = mean[i, j] - std[i, j] + width[i, j]*(b + 0.5)
  return median


if __name__ == '__main__':
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
