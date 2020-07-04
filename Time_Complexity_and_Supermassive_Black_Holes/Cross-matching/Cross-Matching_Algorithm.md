## Creating Catalogue of Survey Images
* When we create a catalog from survey images, we start by extracting a list of sources, galaxies and stars, using source-finding software like _sExtractor_. 
* Basically they run through the pixels in an image and find peaks that are statistically significant.
* Then, they group the surrounding pixels and fit a function, usually based on the telescope response, which is called the 'beam' or the 'point spread function'.
* This results in a list of objects, each of which has a position, an angular size and an intensity measurement.
* The uncertainties on these measured values depend on things like noise in the image, the calibration of the telescope, and how well we can characterize the telescope's response function.

## Action
* Once we have our catalogues, cross-matching involves searching the second catalogue to find a counterpart for each object in the first catalogue. 
* To do this, we usually search within a given radius, based on the uncertainties in the position.
* For distance we use angular distance or the Great Circle Distance.

## Cross Matching Algorithm

for source_A in catalogue_1:
    for source_B in catalogue_2:
        offset = angular_distance(A, B)
        if offset < radius:
            if offset smallest seen so far:
                best_match = (A, B, offset)

* __Result__ : When we run it on two catalogues, we end up with a list of matches between galaxies in the first catalogue, galaxies in the second catalogue and the great circles offset between them.

* __Problem With this__ : When we increase the number of galaxies in each catalogue by a factor of ten, the time the program takes to run increases by a factor of 100.