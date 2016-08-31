# Paper 1 summary

## (i) Reference : Hall, Tracy, Sarah Beecham, David Bowes, David Gray, and Steve Counsell. "A systematic literature review on fault prediction performance in software engineering." IEEE Transactions on Software Engineering 38, no. 6 (2012): 1276-1304.

## (ii) Keywords:

* (ii1) **Search Based Software Engineering** : A systematic review is a type of literature review that collects and critically analyzes multiple research studies or papers.
* (ii1) **Software fault prediction**

## (iii) Brief Notes:

* (iii1) **Motivation** : Context is important in fault prediction modelling as it can affect the performance of models in a particular context and the transferability of models between contexts. There are a range of independent variables that have been used in fault prediction models. Fault prediction models are based on a wide variety of both machine learning and regression model techniques. Currently the impact context have on transferability of models, the impact individual independent variables have on model performance and the impact modelling technique has on model performance is not clear. This makes it difficult for model builders to make effective technique selections. This paper aims to present a synthesis of current knowledge on the impact of context, independent variables and model techniques on model performance. 
* (iii2) **Assessment**: The paper's approach to identify papers suitable for synthesis is motivated by Kitchenham and Charter’s notion of a quality check. The assessment is focused specifically on identifying only papers reporting sufficient information to allow synthesis across studies in terms of answering the research questions. To allow this, a basic set of information must be reported in papers. Without this it is difficult to properly understand what has been done in a study and equally difficult to adequately contextualize the findings reported by a study. The authors have developed and applied a set of criteria focused on ensuring sufficient contextual and methodological information is reported in fault prediction studies.
* (iii3) **Related Work**: Fenton and Neil conducted a critical review of software fault prediction research up to 1999. Catal and Diri’s review covers work published between 1990 and 2007. Catal and Diri did not report on how they sourced their studies, stating that they adapted Jørgensen and Shepperd’s methodology. Fenton and Neil did not apply the systematic approach introduced by Kitchenham and Charters as their study was published well before these guidelines were produced.
* (iii4) **Informative Visualizations**: Results of applying Assessment criteria are mentioned in below table.

![alt tag](https://github.com/amritbhanu/fss16591/blob/master/read/1/table.png)

## (iv) Improvisations:
We need more studies which are based on a reliable methodology and which consistently report the context in which models are built and the methodology used to build them. A larger set of such studies will enable reliable cross-study metaanalysis of model performance. It will also give practitioners the confidence to appropriately select and apply models to their systems. Without this increase in reliable models that are appropriately reported, fault prediction will continue to have limited impact on the quality and cost of industrial software systems.
