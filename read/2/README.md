# Paper 2 summary

## (i) Reference : Song, Qinbao, Zihan Jia, Martin Shepperd, Shi Ying, and Jin Liu. "A general software defect-proneness prediction framework." IEEE Transactions on Software Engineering 37, no. 3 (2011): 356-370.

## (ii) Keywords:

* (ii1) **InfoGain**: The expected information gain is the change in information entropy {H} from a prior state to a state that takes some information.

* (ii2) **Forward selection**:  It starts from an empty set and evaluates each attribute individually to find the best single attribute. It then tries
each of the remaining attributes in conjunction with the best to find the best pair of attributes. In the next iteration each of the remaining
attributes are tried in conjunction with the best pair to find the best group of three attributes.

* (ii3) **Backward elimination**: It starts with the whole set of attributes, and eliminates one attribute in each iteration until no single attribute elimination improves the evaluation of the subset.

* (ii4) **Wilcoxon signed-rank test**: It is a non-parametric statistical hypothesis test used when comparing two related samples, matched samples, or repeated measurements on a single sample to assess whether their population mean ranks differ. It can be used as an alternative to the paired Student's t-test, t-test for matched pairs, or the t-test for dependent samples when the population cannot be assumed to be normally distributed.

## (iii) Brief Notes:

* (iii1) **Motivation** : Different learning schemes are needed for different data sets (i.e. no scheme dominates), that small details in conducting how evaluations are conducted can completely reverse findings and lastly that their proposed framework is more effective, and less prone to bias than previous approaches.

* (iii2) **Related Work** : Capture-recapture (CR) models and detection profile methods (DPM) to estimate the number of defects remaining in software systems with inspection data and process quality data. Association rule mining algorithms reveal software defect associations. Other work classifies software components as defect-prone and non-defect-prone by means of metric-based classification. They work is mostly inspired by the work done by Menzies et al. "Data mining static
code attributes to learn defect predictors" published in TSE 2007. They comapred Rule Induction and Naive Bayes to predict software components containing defects.

* (iii3) **Patterns** : The framework should consist of two components: (i) scheme evaluation and (ii) defect prediction. Scheme evaluation will evaluate the machine learning algorithm (which performs better wrt historical data) before using it for defect prediction. At the first stage, we need attribute selection that can be categorized as either filters or wrappers and only used on the training set. There is slight difference between Menzies work and this work. Just the order in which cross validation, attribute selection and wrapping filters are applied. Defect prediction with different learning schemes. In short there are 12 comparisons based learning which includes 2 data preprocessors, two attribute selectors, and three learning schemes.

* (iii4) **Datasets** : The public NASA MDP repository [37], which was also used by Menzies and many others e.g. [24], [38], [39], and [22]. What’s more, the AR
data from the PROMISE repository4 was also used. Thus there are 17 data sets in total, 13 from NASA and the remaining 4 from the PROMISE repository.

## (iv) Improvisations:
- (iv1) They can report the results by including the other statistical tests. It can be quite assessment biased.
- (iv2) Data preprocessor/attribute selector can play different roles and they only reported the results with only couple of options.
- (iv3) They surely reported results with 3 different learners, but as they stated these can be quite learner biased. We will need to run many different learners for different datasets.
