# Paper 7 summary

## (i) Reference : Ghotra, Baljinder, Shane McIntosh, and Ahmed E. Hassan. "Revisiting the impact of classification techniques on the performance of defect prediction models." In Proceedings of the 37th International Conference on Software Engineering-Volume 1, pp. 789-800. IEEE Press, 2015.


## (ii) Keywords:

* (ii1) **MARS**: Multivariate Adaptive Regression Splines is a non-parametric regression technique and can be seen as an extension of linear models that automatically models nonlinearities and interactions between variables.
* (ii2) **LMT**: logistic model tree (LMT) is a classification model with an associated supervised training algorithm that combines logistic regression (LR) and decision tree learning.
* (ii3) **Expectation Maximization**: An EM algorithm is an iterative method for finding maximum likelihood or maximum a posteriori (MAP) estimates of parameters in statistical models, where the model depends on unobserved latent variables.
* (ii4) **SMO**: Sequential minimal optimization is an algorithm for solving the quadratic programming (QP) problem that arises during the training of support vector machines.

## (iii) Brief Notes:

* (iii1) **Motivation** : Their results suggest that some classification techniques tend to produce defect prediction models that outperform others on contrary to earlier research which stated the classification techniques didnt matter.

* (iii2) **Patterns** : logistic regression and linear regression, Multivariate Adaptive Regression Splines, Personalized Change Classification, and Logistic Model Trees. Ensemble methods that combine different machine learning techniques have also been explored. Lessmann et al. [34] conducted a study comparing the performance of 22 different classification techniques on the NASA corpus. Their results show that the performance of 17 of the 22 classification techniques are statistically indistinguishable from each other.
![alt tag](https://github.com/amritbhanu/fss16591/blob/master/read/7/learners.png)
* (iii3) **Assessment** : To compare the performance of defect prediction models, they used the Area Under the receiver operating characteristic Curve (AUC), which plots the false positive rate against the true positive rate. They ran the Scott-Knott test to group classification techniques into statistically distinct ranks.
* (iii4) **Datasets** : They used known-to-be noisy NASA corpus, with cleaned version of the NASA corpus and the PROMISE corpus.

## (iv) Improvisations:
- (iv1) They studied 2 datasets which have different predictor metrics, this difference might be the reason for their results. They should have unified the metrics properly and then have come out for a conclusion. This gives rise to cross project defect prediction and unifying the predictor metrics.
