from astropy.io import fits
import numpy as np

def mean_fits(paths):
  ans = np.zeros(fits.open(paths[0])[0].data.shape, dtype=fits.open(paths[0])[0].data.dtype)
  for file in paths:
    ans += fits.open(file)[0].data
  return ans / len(paths)


if __name__ == '__main__':
  
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()