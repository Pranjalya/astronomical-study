## Classification

* Machine learning algorithms don't depend on specific rules. Instead, they try to discover or learn patterns from input data we've given them. 

* There are two broad types of machine learning algorithms,
unsupervised and supervised. Unsupervised algorithms try to discover patterns in data whereas supervised algorithms learn from classified input data, so they can classify unknown examples. 

* __Step 1__ : We start with a sample of galaxies we already know the answer for. We call this the _gold standard_. In this example, these are galaxies with measured spectroscopic red shifts. 
    - You typically need quite a large sample because the learner needs to be able to see enough instances of each type of object and its properties to correctly model and then predict the correct results.
    - You also want to be really confident about your initial classifications. In this example, the red shifts for the training data were calculated using spectroscopic techniques, which are generally a highly reliable way of calculating red shifts. In other cases you might use a gold standard data set classified by human experts.
    - Another option is to use training data classified by many non-experts. Galaxy Zoo is a massive citizen science project that has made scientific discovers through the work of dedicated amateurs and intelligent machine learning methods.

* __Step 2__ : So the next step is to extract features that represent your input data in some way. Sometimes it's obvious how to do this because the manual classification scheme we use is designed by specific features.
    - In this example, we'll use colors measured by comparing the magnitudes from five different Sloan filters U, G, R, I and Z.
    - Each filter measures the light from the galaxy in a particular wavelength range. To calculate colors, astronomers subtract the magnitudes measured in neighboring filters. For example, U minus G or I minus Z.
    - In other cases where you're not sure which features to use, you can extract as many features as you want from the original data and then leave the classifier to prioritize which are most important. 

* __Step 3__ : It's good to have some understanding of how these different algorithms work and how to choose the right one for your task.
    - For some tasks, Naive Bayes classifiers are typically very fast but don't have great accuracy. Whereas random forests classifies have high accuracy but can be much slower to run. 
    - Machine learning is a very empirical discipline. It's okay to test out a few different algorithms using off-the-shelf implementations such as Scikit-learn.

* __Step 4__ : Now we get to the most important parts. You have your data set of classified objects and you've selected features that can be used to represent these objects. You now train your classifier on this known data set. 
    - The process of training basically consists of building a model between your inputs and the result. The nature of the model depends on the classification algorithm being used. 

* __Step 5__ : Now, we measure accuracy. It's worth thinking about how you'd evaluate that for a human. 
    - In the early days of classification, most objects would only have been classified once. Classifiers like Annie Cannon were extremely expert and very careful. So their classifications were probably pretty reliable. But there's no doubt that even the most diligent human classifiers can make mistakes. 
    - An obvious way of evaluating the reliability of a human classifier would be to get another expert to classify the same set of data, and compare their results. This would give you a measure of how reliable their classifications are. 
    - If a classifier makes a mistake, an object of category A could be accidentally classified as category B. When all objects must be classified, each mistake introduces two classification errors, an extra B, a false positive and a missing A, a false negative.
    - Machine learning researchers typically quantify the reliability of a classifier using two measures, precision and recall.

* __Step 6__ : So how do we know our classifier will be accurate on unknown data if it's just trained on one data set? To answer this, we use _n-fold cross-validation_.
    - You split your sample of galaxies with known red shifts into ten sets or folds, which are usually chosen randomly.
    - You then train your classifier on the galaxies in nine of these sets and test it on the galaxies in the tenth set and record the precision and recall.
    - You repeat this process for each fold and calculate the mean and the standard deviation, which is how you get the name 10-fold Cross Validation.
    - You've now developed a system that learns the classificational regression from data and can evaluate how reliable it is.
    - You can now run it on some unknown galaxies, determine their red shifts and estimate to make their errors. 