def hms2dec(hours, minutes, seconds):
  '''Converts HMS (hours:minutes:seconds) format to decimals'''
  return 15*(hours + minutes/60 + seconds/(60*60))

def dms2dec(degree, arcminutes, arcseconds):
  '''Converts DMS (degrees:arcminutes:arcseconds) format to decimals'''
  ans = degree + arcminutes/60 + arcseconds/(60*60)
  return ans if degree>=0 else -1*(-1*degree + arcminutes/60 + arcseconds/(60*60))

if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(23, 12, 6))

  # The second example from the question
  print(dms2dec(22, 57, 18))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))