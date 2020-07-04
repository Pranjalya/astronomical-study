# One of the most widely used formats for astronomical images is the Flexible Image Transport System. In a FITS file, the image is stored in a numerical array, which we can load into a NumPy array.
# FITS files also have headers which store metadata about the image.
# FITS files are a standard format and astronomers have developed many libraries (in many programming languages) that can read and write FITS files.

# Read FITS file and print header info and its coyntent into numpy arra
from astropy.io import fits
hdulist = fits.open('image0.fits')
print(hdulist.info())
data = hdulist[0].data
print(data.shape)


# Opening a FITS file in Astropy returns a HDU (Header/Data Unit) list. Each HDU stores headers and (optionally) image data.
# The header contains metadata about the HDU object, e.g. its dimensions and data type. Every HDU can contain image data. The first HDU is called tprimary HDU.
# If we want to access individual HDUs, we can index the HDU list object returned by fits.open. The image data can be accessed using the data attrinute.

###################################################

from astropy.io import fits
import numpy as np

def load_fits(path):
  hdulist = fits.open(path)
  data = hdulist[0].data
  return np.unravel_index(np.argmax(data), data.shape)
  
if __name__ == '__main__':
  bright = load_fits('image1.fits')
  print(bright)

  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 
