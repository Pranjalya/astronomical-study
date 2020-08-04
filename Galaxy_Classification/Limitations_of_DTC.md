## Limitations of Decision Tree Classifier

* We extracted a small number of features that we knew were likely to characterize and differentiate these galaxies reasonably well and then used a decision tree classifier to get our first results. 

* How do we understand these results beyond the single classifier accuracy figure? For example, which types of galaxies are hardest to classify accurately? 

* One common way to represent the results from machine learning and answer questions like these is a _confusion matrix_. 
    - A confusion matrix visualizes the relationship between the true labels from our gold standard and the predicted labels from our classifier.
    - Our confusion matrix shows how many galaxies of one type, say ellipticals, have been classified correctly as that type. And how many have been classified incorrectly as a different type, say spirals.
    - The confusion matrix allows us to calculate our overall accuracy, precision, and recall. And the accuracy for each category.
    - The cells on the diagonal show the true positives, where predicted classes equal true classes.
    - And the other cells visualize false positives, summing the rest of the column, and the false negatives, summing the rest of the row. 

![Galaxy Zoo Decision Tree](https://github.com/Pranjalya/astronomical-study/tree/master/Galaxy_Classification/data/galaxyzoo.png)

#### Setting Baslines

* As an absolute minimum baseline accuracy, you could consider the result you'd get by classifying your entire testing set by randomly assigning a class.

* In our case, we have three classes that are evenly distributed, so our baseline accuracy would be 33%.

* If you had a clear majority class, then assigning everything to that class would make more sense as a baseline. But we're aiming to get much better results than from random chance.

* 
So a more sensible baseline system that machine learning researchers use is to run a naive solution without much tuning. You can then compare all future improvements to this baseline. 

#### Some problems

* If you run your basic classifier and you get results like 99% accuracy, there are a couple of things that could be going on.

* The first option is that maybe your problem is just really, really easy. In cases like these, you probably don't need to be doing machine learning at all. 
    - You could easily write a rule based system to solve the problem.
    - This is what we'd call a trivial classification problem. 

* The more likely problem for real world astronomy tasks is that you've got a mistake in your methodology. For example, _gold standard leakage_ is occurring in your training process. 
    - Leakage occurs when gold standard information, in other words the correct classes, leaks into the test set. And the classifier can use it to cheat - kind of like sneaking a peek at the exam beforehand.
    - The simplest case of this is accidentally including the category in the set of features. Or evaluating a classifier  on the training data itself, rather than using a separate test set. 

* What if your classifier evaluation reports high accuracy, but when you apply the classifier to your full data set, it appears to perform much worse than predicted? There are several possibilities for this.
    1. Firstly your training and test sets may not actually be representative of your full data set, in which case the trained model is not a good fit for the data. This means the test set may give a false impression of accuracy on the real distribution of the data. 
    2. Secondly your machine learner may be overfitting your data. Producing a complex model that worked really well on your training data, But that doesn't generalize well when applied to unseen data sets. 
        - For example a deeply nested decision tree can accurately reproduce the training data, but fails to capture any generalizations that are necessary for classifying other instances.
    3. Finally, in the process of optimizing your choice of machine learner, we may have optimized for the specific training set, and not the real distribution.
        - This can be largely overcome by using the 10-fold cross validation to test your final system, or using a separate held-out test set that is only used to evaluate your final model. 

##### Some of the manual classification projects

_If you want to do further reading on machine learning classification, and on the science that comes from Galaxy Zoo, there are a list of Galaxy Zoo publications here: https://www.zooniverse.org/about/publications._