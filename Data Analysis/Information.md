## Pulsars
* Pulsars are rotating neutron stars observed to have pulses of radiation at very regular intervals that typically range from milliseconds to seconds. 
* Pulsars have very strong magnetic fields which funnel jets of particles out along the two magnetic poles. 
* These accelerated particles produce very powerful beams of light.

## Image stacking
* We typically call something a detection if the flux density is more than five standard deviations higher than the noise in the local region.
* The grayscale is a measure of the flux density of emission from astronomical objects.
* We want to sort the values of each pixel in our image and create a final image using the middle pixel.
* Works well with mean, but median is a better average tool, and median does not scale well like mean.

## Better Algorithm
* We took a large set of images for which we could not detect any individual pulsars.
* When we lined the images up so all of the undetected pulsars are located in the center of image, and then calculate the median across all of the images, we can see a detection. 
* What we saw is a statistical detection of a population of pulsars that are too faint to see in our original data set. 