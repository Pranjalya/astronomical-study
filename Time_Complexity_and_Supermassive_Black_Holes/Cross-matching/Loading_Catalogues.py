import numpy as np
from Converting_to_Decimal_degrees import hms2dec, dms2dec

def import_bss():
  dat = np.loadtxt('bss.dat', usecols=range(1, 7))
  ans, i = [], 1
  for data in dat:
    ans.append((i, hms2dec(data[0], data[1], data[2]), dms2dec(data[3], data[4], data[5])))
    i += 1
  return ans

def import_super():
  dat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  i, ans = 1, []
  for data in dat:
    ans.append((i, data[0], data[1]))
    i += 1
  return ans

if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)