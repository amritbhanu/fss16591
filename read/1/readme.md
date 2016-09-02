# Paper 1 summary

## (i) Reference : Hall, Tracy, Sarah Beecham, David Bowes, David Gray, and Steve Counsell. "A systematic literature review on fault prediction performance in software engineering." IEEE Transactions on Software Engineering 38, no. 6 (2012): 1276-1304.

## (ii) Keywords:

* (ii1) **Systematic Literature Review**: A systematic review is a type of literature review that collects and critically analyzes multiple research studies or papers.
* (ii2) **Mean Standard Error**: The MSE is the standard deviation of the sample-mean's estimate of a population mean.
* (ii3) **Area Under Curve**: The area under a curve between two points can be found by doing a definite integral between the two points. To find the area under the curve y = f(x) between x = a and x = b, integrate y = f(x) between the limits of a and b.
* (ii3) **Receiver operating characteristic Curve**: A graphical plot of the sensitivity (or pd) vs. 1 – specificity (or pf) for a binary classification system where its discrimination threshold is varied

## (iii) Brief Notes:

* (iii1) **Motivation** : Context is important in fault prediction modelling as it can affect the performance of models in a particular context and the transferability of models between contexts. There are a range of independent variables that have been used in fault prediction models. Fault prediction models are based on a wide variety of both machine learning and regression model techniques. Currently the impact context have on transferability of models, the impact individual independent variables have on model performance and the impact modelling technique has on model performance is not clear. This makes it difficult for model builders to make effective technique selections. This paper aims to present a synthesis of current knowledge on the impact of context, independent variables and model techniques on model performance. 
* (iii2) **Assessment**: The paper's approach to identify papers suitable for synthesis is motivated by Kitchenham and Charter’s notion of a quality check. The assessment is focused specifically on identifying only papers reporting sufficient information to allow synthesis across studies in terms of answering the research questions. To allow this, a basic set of information must be reported in papers. Without this it is difficult to properly understand what has been done in a study and equally difficult to adequately contextualize the findings reported by a study. The authors have developed and applied a set of criteria focused on ensuring sufficient contextual and methodological information is reported in fault prediction studies.
* (iii3) **Sampling Procedures**: They defined various criterias to come up with those papers that can be of utmost importance. They defined the papers, inclusion and exclusion criteria, Paper selection and validation process, Prediction criteria, context criteria, model building criteria, data criteria.
* (iii4) **Informative Visualizations**: Results of applying Assessment criteria are mentioned in below table.

![alt tag](https://github.com/amritbhanu/fss16591/blob/master/read/1/table.png)

## (iv) Improvisations:
- (iv1) We need more studies which are based on a reliable methodology and which consistently report the context in which models are built and the methodology used to build them.
- (iv2) A larger set of such studies will enable reliable cross-study metaanalysis of model performance. It will also give practitioners the confidence to appropriately select and apply models to their systems.
- (iv3) Cross project defect/fault prediction can be done too, where privacy of data is of concern.
