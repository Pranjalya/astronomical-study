import numpy as np
from Loading_Catalogues import import_bss
from Finding_Angular_Distance import angular_dist

def find_closest(cat, r, d):
  minim = 10**9+7
  ans = None
  for c in cat:
    dist = angular_dist(c[1], c[2], r, d)
    if dist < minim:
      minim = dist
      ans = (c[0], minim)
  return ans

if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))
