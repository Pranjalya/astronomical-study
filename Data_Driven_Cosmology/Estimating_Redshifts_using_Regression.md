## Estimating Redshifts using Regression

* The total light emitted by a galaxy is distributed
over the whole electromagnetic spectrum. 

* The Sloan Digital Sky Survey measured the flux of each object using 5 optical and infrared filters between 300 and 1,100 nanometers.

* Each of these fluxes tells us how much light the object emits in that wavelength range. The fluxes are converted to magnitudes also referred to by their filter names u,
g, r, i and z. 

* The spectrum on this plot comes from bright star Vega,
a blue white main sequence star about 25 light years away. It's a very hot star with an effective temperature of about 10,000 Kelvin.
    - Now we can say that it's brightest at short wavelengths. Now silent Vega actually much further away from us in a distant galaxy.
    - The expansion of space means that light from Vega would be red-shifted and the same spectrum would now peak at longer wavelengths, hence the same filters on the telescope would measure different fluxes in each band. 

* The measured property we can use to quantify this are colors. Colors are the ratio of the flats measurements in neighboring filters, which is equivalent to subtracting the magnitudes.
    - The five Sloan filters linked to four colors.
u-g, g-r, r-i and i-z.
    - A galaxy emits light with a spectrum that's basically the sum of all of the stars in the galaxy. The key to photometric red shift classification is that a red shifted galaxy will have different observed colors to what it would have at red shift zero. 

* However, there's a fundamental ambiguity about this idea that makes it impossible to solve in anything other than a data driven or empirical way. If the observed colors of two galaxies are different, how do we know if that difference is caused by red shift or whether it's because the spectrum of one galaxy is simply a different shape to the other one in the first place? 
    - Firstly, we take a large set of galaxies, say, 50,000, for which we have measured accurate spectroscopic red shifts and derived four photometric colors from this low magnitudes. We then train a decision tree regressor that builds a model mapping the features, in this case the four colors. To the results, in this case the red shifts measured from spectroscopy. 
    - The first decision splits the data, where the u-g color is less than or equal to 0.7475. This subset is then split again at g-r less than or equal to 0.372.
    - For each node, we say the regression value and the main square error that would be returned if it stopped making decisions at that point. 

* While the decisions of the model are easily followed, it's often hard to gain insight from the decision tree, since they can be large and complex. For example, the best performing decision tree for our experiment has a maximum depth of seven decisions.

* For the best possible classifications and predictions, we usually want to combine machine learning algorithms with our expert astronomy knowledge about the problem. For example, many photometric red shift classifiers use template spectra of different types of galaxies to help resolve these ambiguities. 

* Using only the four colours as features and a basic off the shelf classified with variable tuning. We've managed to predict reasonably accurate red shifts. 