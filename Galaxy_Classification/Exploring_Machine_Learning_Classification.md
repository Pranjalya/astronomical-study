## Exploring Machine Learning Classification

### Classification vs Regression

* In classification, the predictions are from a fixed set of classes, whereas in regression the prediction typically corresponds to a continuum of possible values.

* In regression, we measure accuracy by looking at the size of the differences between the predicted values and the actual values. In contrast, in classification problems a prediction can either be correct or incorrect. This makes measuring the accuracy of our model a lot simpler.

* In terms of implementation using decision trees, there is very little difference between classification and regression. The only notable difference is that our targets are classes rather than real values. When calculating the accuracy, we check whether the predicted class matches as the actual class. 

* __For Decision Tree__ : In decision tree regression, the possible outputs are a finite set of values that correspond to the number of leaves/end points in the tree. Ideally we want as many points as possible to give a good approximation of the 'continuous' parameter space, whilst avoiding overfitting. 

### Selecting Features for Galaxy Classification

* *The features that we will be using to do our galaxy classification are _colour index_, _adaptive moments_, _eccentricities_ and _concentrations_. These features are provided as part of the SDSS catalogue.

* We briefly describe these below. Further information how they are calculated can be found [here](http://skyserver.sdss.org/dr7/en/help/docs/algorithm.asp).

* __Colour indices__ are the same colours (u-g, g-r, r-i, and i-z) we used for regression. Studies of galaxy evolution tell us that spiral galaxies have younger star populations and therefore are 'bluer' (brighter at lower wavelengths). Elliptical galaxies have an older star population and are brighter at higher wavelengths ('redder').

* __Eccentricity__ approximates the shape of the galaxy by fitting an ellipse to its profile. Eccentricity is the ratio of the two axis (semi-major and semi-minor). The De Vaucouleurs model was used to attain these two axis. To simplify our experiments, we will use the median eccentricity across the 5 filters. 

* __Adaptive moments__ also describe the shape of a galaxy. They are used in image analysis to detect similar objects at different sizes and orientations. We use the fourth moment here for each band.

* __Concentration__ is similar to the luminosity profile of the galaxy, which measures what proportion of a galaxy's total light is emitted within what radius. A simplified way to represent this is to take the ratio of the radii containing 50% and 90% of the Petrosian flux. 

*  The Petrosian method allows us to compare the radial profiles of galaxies at different distances. If you are interested, you can read more here on the need for Petrosian approach.

For these experiments, we will define concentration as:
```
conc = petro(R50) / petro(R90)
```
We will use the concentration from the u, r and z bands. 

### Accuracy and Model Score

* The accuracy of classification problems is a lot simpler to calculate than for regression problems. The simplest measure is the fraction of objects that are correctly classified. That is

```
accuracy = # correct predictions / # predictions 
accuracy = (∑(i=1)(n)predicted[i] = actual[i]) / n
```

* The accuracy measure is often called the model score. While the way of calculating the score can vary depending on the model, the accuracy is the most common for classification problems.

* Note: sklearn has methods to get the model score. Most models will have a score method which in the case of the decision tree classifier uses the above formula. The cross_val_score function in the model_selection module can be used to get k cross validated scores. 

### Random Forest Classifiers

* We can improve the accuracy of our classification by using a collection (or ensemble) of trees as known as a random forest.

* A random forest is a collection of decision trees that have each been independently trained using different subsets of the training data and/or different combinations of features in those subsets.

* When making a prediction, every tree in the forest gives its own prediction and the most common classification is taken as the overall forest prediction (in regression the mean prediction is used). 

* Random forests help to mitigate overfitting in decision trees.

* __Training data__ is spread across decision trees. The subsets are created by taking random samples with replacement. This means that a given data point can be used in several subsets. (This is different from the subsets used in cross validation where each data point belongs to one subset).

* __Individual trees__ are trained with different subsets of features. So in our current problem, one tree might be trained using eccentricity and another using concentration and the 4th adaptive moment. By using different combinations of input features you create expert trees that are can better identify classes by a given feature.

* The sklearn random forest only uses the first form of sampling. 