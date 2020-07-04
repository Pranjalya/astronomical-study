## Binapprox algorithm

* If there were a way to calculate a "running median" you could save space by only having one image loaded at a time. Unfortunately, there’s no way to do an exact running median, but there are ways to do it approximately.

* The binapprox algorithm does just this. The idea behind it is to find the median from the data's histogram. As an example, say we have a list of 30 numbers between 7 and 16 and its histogram is:

* The median is the average of the 15th and 16th numbers in the ordered list (we can think of this as the 15.5th number). So, starting from the left, if we sum up the counts in the histogram bins until we get to just over 15.5 then we know the last bin we added must have contained the median.

* In our example, the first 3 bins sum to 9 and the first 4 bins sum to 18, so we know that the median falls into the 4th bin (marked in red), and so it must be between 10 and 11.

* We choose the middle (or midpoint) giving an estimate of 10.5.


### Working

The binapprox algorithm uses the method from the previous slide, but it saves even more time and space by only looking for the median within one standard deviation of the mean (see the link if you’d like to know why that works).

The full algorithm for a set of N data points works as follows:

1. Calculate their mean and standard deviation, μ and σ;
2. Set the bounds: minval = μ-σ and maxval = μ+σ. Any value >= maxval is ignored;
3. Set the bin width: width=  2σ/B;
4. Make an ignore bin for counting value < minval;
5. Make B bins for counting values i minval and maxval, e.g. th first bin is minval < value < minval + width;
6. Count the number of values that fall into each bin;
7. Sum these counts until total >= (N + 1)/2. Remember to start from the ignore bin;
8. Return the midpoint of the bin that exceeded (N + 1)/2.


The midpoint of a bin is just the average of its min and max boundaries, i.e. the lower boundary + width/2.


As soon as the relevant bin is updated the data point being binned can be removed from memory. So if you're finding the median of a bunch of FITS files you only need to have one loaded at any time. (The mean and standard deviation can both be calculated from running sums so that still applies to the first step).


The downside of using binapprox is that you only get an answer accurate to  σ/B by using B bins. Scientific data comeswith its own uncertaintiesthough, so as long as youkeep B large enough this isn't necessarily a problem.