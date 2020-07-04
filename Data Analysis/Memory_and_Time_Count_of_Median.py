from astropy.io import fits
import numpy as np
import time

def median_fits(paths):
  start = time.perf_counter()
  data = []
  for path in paths:
    data.append(fits.open(path)[0].data)
  stack = np.dstack(data)
  del data
  median = np.median(stack, axis=2)
  memory = stack.nbytes/1024
  time_taken = time.perf_counter() - start
  return (median, time_taken, memory)


if __name__ == '__main__':
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])