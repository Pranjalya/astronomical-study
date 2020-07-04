## Reduction
* The astropy module has a cross-matching function that makes it extremely easy to calculate angular distances and cross-match two catalogs.

* Using astropy cross-matching, it took only 25 seconds for two input catalogs of a million sources each.

## K-Dimensional Tree

* A k-d tree, or k-dimensional tree, is a way of representing the points in space in a recursive structure.

*  K is the number of dimensions, which in our case are the two dimensions of our coordinate system, right ascension and declination.

* To construct a k-d tree, you have to recursively partition the space at the median point each time.

* The median point here in the x dimension is A. And so we split the plane at that point, and A becomes the root node of the tree. We then consider points to the left of A and split the plane in the y dimension. And again, at the median point, which is E. We repeat this process, alternating between the x and y dimensions, until the left-hand side of the tree is complete.

* Finally, the process is repeated for the data to the other side of A until every data point in our original dataset is either a node or a leaf in the tree.

* Now once the tree is constructed, you can use this for fast nearest neighbor searching.

* Finds results in O(log n)

* Moving to database also increases speed as it uses CPU cycles.


## What does result of Cross-Matching Mean?

* Nearly all of our radio sources have an optical counterpart, which means we can classify them into two different categories.
    1. Most of our radio galaxies are associated with quasars. Where we're looking towards the central black hole and can see the very energetic accretion disk.
        - The radiation from the accretion disk is so bright that it outshines all of the stars in the galaxy. And therefore, looks just like a bright star, hence the name, quasi-stellar object, or quasar.
    2. The rest of our radio galaxies sit inside normal galaxies, where we can see a cloud of many stars grouped together. This could mean that the supermassive black hole has stopped accreting material. And the radio jets are remnants of past activity.
        - Because we've found optical identifications for most of our radio sources, we can also get redshift for them. This tells us the distance to each galaxy or quasar.

* The redshift for the galaxies range from 0.02 to 0.5, whereas the redshift for the quasars ranges from 0.2 to 3. 

* This tells us most of the galaxies are in the relatively local universe, whereas most of the quasars are typically much further away.