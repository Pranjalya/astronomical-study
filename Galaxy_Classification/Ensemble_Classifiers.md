## Ensemble Classifiers

* Decision trees are highly susceptible to noisy training data and have a tendency to overfit. This 'noise' could either be from the Galaxy Zoo volunteer classifications or it could be from the features derived from physical observations.

* One of the most popular and simple techniques for making a classifier which is robust to noisy data is called _ensemble learning_ when multiple models are trained and their results are combined together in some way.
    - For classification, this typically includes voting and for aggression, it typically involves taking the mean of each ensembled learner. 

* The idea behind ensemble learning is, that the combined classifications of multiple week learners can give a more reliable, robust result, in the face of imperfect training data, and any non-determinism in the training process.
    - For ensembles to work better than individual classifiers, the members of the ensemble must be different in some way; they must give independent results.
    - If they all gave the same predictions on each instance, then having more of them would make no difference at all.
    - There are many ways to achieve this model independence, including using different machine learning algorithms, different parameters, for example the tree depth, or different training data.

* One of the most popular methods is called _bootstrap aggregating_, or _bagging_ for short. 
    - In bagging, samples of the training data are bootstrapped. In other words, selected with replacement from the original training set. The models are trained on each sample. 
    - Bagging makes each training set different with an emphasis on different training instances.
    - A random forest classifier is a supervised machine learning algorithm that uses an ensemble of decision tree classifiers. It builds an ensemble by randomly selecting, either subsets of training instances, bagging, or selecting a subset of features of each decision point.
    - Which variant of a random forest classifier you get depends on which programming language and library you're using.
        - Sci-kit learn’s Random Forest implementation using bagging, but R's uses feature selection.

* We can use exactly the same features and methodologies before but substitute the random forest classifier for the decision tree classifier.
    - We have a number of extra parameters to consider setting but the most important is the number of decision trees that the random forest builds.
    - A larger number will use more samples from the original data and be more robust to noise and overfitting. 
    - Because each classifier in the ensemble returns a vote we can not only find the most popular category but we can look at the distribution of votes over all the categories.
    - This allow us to calculate an estimated probability that our classification is correct, and identify which test instances are particularly hard for the system to classify.
    - This probabilities can also let you identify out liners, objects that are not similar to any of the training classes.
    - This can be a great way of identifying those rare objects that need further scientific investigation. 

* Ultimately, the goal of classification is to increase our
physical understanding of the universe. 
    - The morphological classification of galaxies helps us understand galaxy formation and evolution. How did the galaxies become the complex systems we observe today?
    - We know that part of the story is hierarchical clustering, the formation of larger galaxies through the merger of many small ones.
    - We also know that internal processes in the galaxies are necessary to explain the ongoing star formation in spiral galaxies.
    - Any models of galaxy formation that we develop have to explain the incredible range of morphologies we observe when we look out into the universe. 