## Morphological Classification of Galaxies

* We're going to use images of galaxies from the Sloan Digital Sky Survey, for which we have manual classifications. Each galaxy was classified by volunteers as part of the galaxy zoo project. 
    - And we've selected a subset for which the classifications had a high confidence. In other words, most volunteers chose the same option. 
    - The galaxies fall into three classes: ellipticals, spirals, and irregular galaxies that show evidence of a merger. 
    - Each individual galaxy has images taken in the five Sloan filters. In addition, we have several fitted parameters that are calculated as part of the Sloan data reduction pipeline. 

* To train a machine-learning classifier, we need to characterize each galaxy by a set of properties, or features. When we did decision tree regression in the last module, we only used the four Sloan colors, this time, we'll use a richer feature set. 

* The decision tree algorithm uses our training set to build a model to map these features to the correct classifications.
    - We'll use ten fold cross validation to evaluate the accuracy of our classifier before applying it to unknown data.
    - So the overall methodology is pretty clear and it's basically the process you should follow whenever you do supervise machine learning.
    - The place where a lot of the thinking happens from a scientists point of view is _feature selection_.

* One way of thinking about this is to consider the process
you'd go through if you were classifying the galaxies by hand. Galaxy Zoo has some great visualizations of the decision trees that the volunteer classifiers were required to follow. 
    - This tree starts with a very high-level decision about whether the object in the image is round, looks like a disk, or is a star.
    - Then for each of the two main classes, round or disc like, there is a series of increasingly specific questions that help provide a final classification.
    - Having a formal scheme like this is essential when you have thousands of different volunteers contributing. 

* However, for a machine learning algorithm, the features and questions need to be quantifiable. So lets think about the features we might use for automatic classification.
    - Perhaps the simplest option would just be to use every pixel in the image for every galaxy. 
    - So if we had 512x512 pixel images for each of the five Sloan filters, each galaxy would be represented by 1,310,720 features.
    - This approach of using the raw pixels as features has some advantages. 
        - irstly, you minimize the possible bias you might introduce through feature selection.
        - Secondly it's simpler, you don't have to implement any sophisticated image analysis features, you can just take the pixels as they are.
    - However, it also has some disadvantages. 
        - The downside to not introducing bias is that you're not taking advantage of your expert knowledge. Using raw pixels doesn't incorporate existing astronomy knowledge about the problem, like the fact that elliptical galaxies tend to be redder in color because they're made up of older stars. 
        - The second disadvantage is computational. Using every pixel in the image means you haven't reduced the dimensionality of the problem, which makes it computationally expensive. 

```
The degree of classification success largely depends on
the significance of the features selected for classification.           - Edwin Hubble
```

* Features that we could use : 
    - A few obvious ones might be the color of the galaxy.
        - This is a feature Hubble didn't have access to, since photographic plates only give a single intensity measurement.
        - But we now know it's a really important indicator of the age of the stars in each galaxy. 
    - A second one is the ellipticity of the galaxy.
        - We can get a rough idea of the shape of the galaxy by fitting an ellipse to its profile and then using the ratio of the semi-major to semi-minor axes to characterize this shape. 
    - And finally, the luminosity profile of the galaxy.
        - This is a measure of how the brightness of a galaxy varies as a function of the radius from its center. 

* These features attempt to replicate properties that the human eye identifies when looking at the image of the galaxy. 

* All features have limitations, just like human observations.
    - For example, the ellipticity of a galaxy is dependent on the inclination with respect to our viewing angle. 
    - That's okay because each feature only contributes part of the information that the classifier and uses to build this model. 

* We now train on decision tree classifier on our three classes, elliptical, spirals, and mergers.
    - Using ten fold cross validation to evaluate our accuracy.
    - And finally, here are our results (79 %).
    - Without sophisticated features or optimization of the classified parameters, we've correctly classified around 4/5ths of the galaxies into elliptical spiral emerges.