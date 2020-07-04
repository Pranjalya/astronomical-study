# We can improve on the previous optimisation further by not only stopping the search once it gets past declination of the object to be matched, but starting the search as close as possible to the object. To summarise, the modification is:

# Sort the second catalogue objects by order of declination;
# Start the search loop at the first second catalogue object with declination greater than  δ−r ;
# Finish the search loop at the last second catalogue object with declination less than  δ+r .
# Boxing in the search in this way saves on calculating the distances for almost the entire second catalogue.

# We just need to find a fast way to find the second catalogue objects nearest to the boundaries of  [δ−r,δ+r] so we know where to start and finish our search.

# The easiest way to do this conceptually is to loop through the sorted catalogue, checking every declination until we find the objects we're looking for. But there is a more efficient way.

import numpy as np
import time

def angular_dist(r1, d1, r2, d2):
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return 2*np.arcsin(np.sqrt(a + b))

def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  max_radius = np.radians(max_radius)
  
  matches = []
  no_matches = []

  # Convert coordinates to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  order = np.argsort(cat2[:,1])
  cat2_ordered = cat2[order]
  
  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_id2 = None
    max_dec = dec1 + max_radius
    min_dec = dec1 - max_radius
    
    min_index = cat2_ordered[:, 1].searchsorted(min_dec, side='left')
    max_index = cat2_ordered[:, 1].searchsorted(max_dec, side='right')
    
    for id2, (ra2, dec2) in enumerate(cat2_ordered[min_index:max_index+1], min_index):
      dist = angular_dist(ra1, dec1, ra2, dec2)
      if dist < min_dist:
        min_id2 = order[id2]
        min_dist = dist
        
    # Ignore match if it's outside the maximum radius
    if min_dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id2, np.degrees(min_dist)))
    
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken


if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
