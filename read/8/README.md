# Paper 7 summary

## (i) Reference : Chakkrit Tantithamthavorn, Shane McIntosh, Ahmed E. Hassanl and Kenichi Matsumoto. "Automated Parameter Optimization of Classification Techniques for Defect Prediction Models."

## (ii) Keywords:

* (ii1) **Software defect prediction**: Software Defect Prediction (SDP) is one of the most assisting activities of the Testing Phase of SDLC. It identifies the modules that are defect prone and require extensive testing. This way, the testing resources can be used efficiently without violating the constraints.

* (ii2) **Experimental Design**: The design of experiments (DOE, DOX, or experimental design) is the design of any task that aims to describe or explain the variation of information under conditions that are hypothesized to reflect the variation.

* (ii3) **Classification Techniques**: In machine learning and statistics, classification is the problem of identifying to which of a set of categories (sub-populations) a new observation belongs, on the basis of a training set of data containing observations (or instances) whose category membership is known. Eg. Naive Bayes classifier, Logistic regression etc.

* (ii4) **Parameter Optimization**: In the context of machine learning, parameter optimization or model selection is the problem of choosing a set of parameters for a learning algorithm, usually with the goal of optimizing a measure of the algorithm's performance on an independent data set. Often cross-validation is used to estimate this generalization performance.

## (iii) Brief Notes:

* (iii1) **Motivation** : Defect prediction models are classifiers that are trained to identify defect-prone software modules. Such classifiers have configurable parameters that control their characteristics (e.g., the number of trees in a random forest classifier). Recent studies show that these classifiers may underperform due to the use of suboptimal default parameter settings. However, it is impractical to assess all of the possible settings in the parameter spaces. This paper investigates the performance of defect prediction models where Caret — an automated parameter optimization technique — has been applied.

* (iii2) **Related Work** : Recent research has raised concerns about parameter settings of classification techniques when applied to defect prediction models. For example, Koru et al. and Mende et al. point out that selecting different parameter settings can impact the performance of defect models. Jiang et al. and Tosun et al. also point out that the default parameter settings of research toolkits (e.g., R, Weka, Scikit-learn, MATLAB) are suboptimal. Although prior work suggests that defect prediction models may underperform if they are trained using suboptimal parameter settings, parameters are often left at their default values. Recent research voices concerns about the stability of performance estimates that are obtained from classification techniques when applied to defect prediction models. For example, Menzies et al. and Mittas et al. argue that unstable classification techniques can make replication of defect prediction studies more difficult. Like any form of classifier optimization, automated parameter optimization may increase the risk of overfitting, i.e., producing a classifier that is too specialized for the data from which it was trained to apply to other datasets. 

* (iii3) **Informative Visualization**: The below figure summarises this paper beautifully.

![alt tag](https://github.com/amritbhanu/fss16591/blob/master/read/8/Read%208.png)

* (iii4) **Results**: C5.0 boosting tends to yield top-performing defect prediction models more frequently than the other studied classification techniques. Automated parameter optimization increases the likelihood of appearing in the top Scott-Knott ESD rank by as much as 83%. Automated parameter optimization increases the likelihood of 11 of the studied 26 classification techniques by as much as 83% (i.e., C5.0 boosting). This suggests that automated parameter optimization can substantially shift the ranking of classification techniques.


## (iv) Future Work:
- Since automated parameter optimization techniques like Caret yield substantially benefits in terms of performance improvement and stability, while incurring a manageable additional computational cost, this paper suggests they should be included in future defect prediction studies.
