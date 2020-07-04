import numpy as np

def angular_dist(RA1, dec1, RA2, dec2):
  # Convert to radians
  r1 = np.radians(RA1)
  d1 = np.radians(dec1)
  r2 = np.radians(RA2)
  d2 = np.radians(dec2)

  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2

  angle = 2*np.arcsin(np.sqrt(a + b))
    
  # Convert back to degrees
  return np.degrees(angle)

if __name__ == '__main__':
  pass