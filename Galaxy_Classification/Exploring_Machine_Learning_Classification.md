## Exploring Machine Learning Classification

### Classification vs Regression

* In classification, the predictions are from a fixed set of classes, whereas in regression the prediction typically corresponds to a continuum of possible values.

* In regression, we measure accuracy by looking at the size of the differences between the predicted values and the actual values. In contrast, in classification problems a prediction can either be correct or incorrect. This makes measuring the accuracy of our model a lot simpler.

* In terms of implementation using decision trees, there is very little difference between classification and regression. The only notable difference is that our targets are classes rather than real values. When calculating the accuracy, we check whether the predicted class matches as the actual class. 

* __For Decision Tree__ : In decision tree regression, the possible outputs are a finite set of values that correspond to the number of leaves/end points in the tree. Ideally we want as many points as possible to give a good approximation of the 'continuous' parameter space, whilst avoiding overfitting. 