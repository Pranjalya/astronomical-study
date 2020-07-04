def list_stats(values):
  values.sort()
  mid = len(values)//2
  if(len(values)%2==0):
    return ((values[mid-1]+values[mid])/2, sum(values)/len(values))
  return (values[mid], sum(values)/len(values))


if __name__ == '__main__':
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  m = list_stats([1.5])
  print(m)