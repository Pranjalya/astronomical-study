## Resolving Overfitting

* Over fitting the data means they try to account for the outlying data points at the cost of the prediction accuracy of the general trend.

* We will also look at k-fold cross validation. This is a more robust method of validation than the held-out method we used previously.

* In k-fold cross validation, we can test every example once. This is done by splitting the data set into k subsets and training/testing the model k times using different combinations of the subsets.

* Finally, we look at how accurate our model is on QSOs compared with other galaxies. As mentioned in the lectures, QSOs are galaxies that have an Active Galactic Nucleus (AGN). The AGN makes the galaxy brighter and as such they are detectable with the SDSS instruments out to much higher redshifts. 

### Overfitting and Team Depth

* Decision trees have many advantages: they are simple to implement, easy to interpret, the data doesn't require too much preparation, and they are reasonably efficient computationally.

* Decision trees do have some limitations though, one of the biggest being they tend to over fit the data. What this means is that if they are left unchecked they will create an overly complicated tree that attempts to account for outliers in the data. This comes at the expense of the accuracy of the general trend.

* Part of the reason for this over-fitting is that the algorithm works by trying to optimise the decision locally at each node. There are ways in which this can be mitigated and in the next problem we will see how constraining the number of decision node rows (the tree depth) impacts on the accuracy of our predictions. 

* Overfitting is a common problem with decision trees and can be circumvented by adjusting parameters like the tree depth or setting a minimum number of cases at each node.

### Cros Validation

* The method we used to validate our model so far is known as hold-out validation. Hold out validation splits the data in two, one set to test with and the other to train with. Hold out validation is the most basic form of validation.

* While hold-out validation is better than no validation, the measured accuracy (i.e. our median of differences) will vary depending on how we split the data into testing and training subsets. The med_diff that we get from one randomly sampled training set will vary to that of a different random training set of the same size.

* In order to be more certain of our models accuracy we should use k-fold cross validation. k-fold validation works in a similar way to hold-out except that we split the data into k subsets. We train and test the model k times, recording the accuracy each time. Each time we use a different combination of k−1 subsets to train the model and the final kth subset to test. We take the average of the k accuracy measurements to be the overall accuracy of the the model. 

## KFold

* The KFold library is designed to split the data into training and testing subsets. It does this by offering an iterable object that can be initialised with
```
kf = KFold(n_splits=k, shuffle=True)
```
The n_splits=k specifies the number of subsets to use.

* By default shuffle is set to false. It is generally good practice to shuffle the data for cross validation as sometimes during collection and storage, data of a similar type can be stored adjacently which would lead to some learning bias when training the tree. For example, if the data was sorted by redshift, on the first iteration the model might be trained with redshifts 0 to 3 and tested on galaxies with redshifts ~4.

* In the next couple of problems we will use the sklearn library KFold to help us split our data into our k−1 training subsets and remaining test subset. In the first problem we will use the convenience of KFolds to help us calculate the k-fold cross validated accuracy of our model. In the second we will extend this to provide a k-folded cross validated prediction for every galaxy in our data set. 

## QSOs vs Galaxies

* Our sample of galaxies consists of two different populations: regular galaxies and quasi-stellar objects (QSOs). QSOs are a type of galaxy that contain an actively (and intensly) accreting supermassive black hole. This is often referred to as an Active Galactic Nucleus (AGN).
Galaxy with an AGN.

* The light emitted from the AGN is significantly brighter than the rest of the galaxy and we are able to detect these QSOs out to much higher redshifts. In fact, most of the normal galaxies we have been using to create our models have redshifts less than z≈0.4, while the QSOs have redshifts all the way out to z≈6. Due to this contribution from the AGN, the flux magnitudes measured at different wavelengths might not follow the typical profile we assumed when predicting redshifts. 

