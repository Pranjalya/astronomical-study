# We'll cross-match two catalogues: one from a radio survey, the AT20G Bright Source Sample (BSS) catalogue and one from an optical survey, the SuperCOSMOS all-sky galaxy catalogue.
# The BSS catalogue lists the brightest sources from the AT20G radio survey while the SuperCOSMOS catalogue lists galaxies observed by visible light surveys. If we can find an optical match for our radio source, we are one step closer to working out what kind of object it is, e.g. a galaxy in the local Universe or a distant quasar.

#### Steps
# You now have all the tools necessary to crossmatch the BSS and SuperCOSMOS catalogues. In the next problem you'll put it all together to see how many of the bright radio sources in the BSS catalogue have a counterpart in the SuperCOSMOS catalogue. The process you should follow is:
# 
# 1. Select an object from the BSS catalogue;
# 2. Go through all the objects in SuperCOSMOS and find the closest one to the BSS object;
# 3. If the objects are close enough, record the match;
# 4. Repeat 1-3 for all the other objects in the BSS catalogue.
# 5. In step 3, if the closest object isn't within a given distance then it's unlikely that the two objects are actually counterparts, and it's more likely that they just happen to be nearby.
# 
# The given distance you choose depends on the uncertainty of the measured object positions in each catalogue.


####################### STEPS ###########################
# Write a crossmatch function that crossmatches two catalogues within a maximum distance. It should return a list of matches and non-matches for the first catalogue against the second.
# 
# The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object IDs from the first catalogue only. Both lists should be ordered by the first catalogue's IDs.
# 
# The BSS and SuperCOSMOS catalogues will be given as input arguments, each in the format you’ve seen previously. The maximum distance is given in decimal degrees.

import numpy as np
from Finding_Angular_Distance import angular_dist
from Loading_Catalogues import import_bss, import_super

def crossmatch(cat1, cat2, max_radius):
    matches = []
    no_matches = []
    for id1, ra1, dec1 in cat1:
        closest_dist = np.inf
        closest_id2 = None
        for id2, ra2, dec2 in cat2:
            dist = angular_dist(ra1, dec1, ra2, dec2)
            if dist < closest_dist:
                closest_id2 = id2
                closest_dist = dist
        
        # Ignore match if it's outside the maximum radius
        if closest_dist > max_radius:
            no_matches.append(id1)
        else:
            matches.append((id1, closest_id2, closest_dist))

    return matches, no_matches

if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
