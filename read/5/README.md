# Paper 5 summary

## (i) Reference : Danijel Radjenovic, Marjan Hericˇko, Richard Torkar, Aleš Zˇivkovicˇ. "Software fault prediction metrics: A systematic literature review."

## (ii) Keywords:

* (ii1) **Software metric**: A software metric is a standard of measure of a degree to which a software system or process possesses some property.
* (ii2) **Software fault prediction**: A fault is a structural imperfection in a software system that may lead to the system's eventually failing. Software fault prediction aim to identify the faults in a software using certain models. 
* (ii3) **Systematic literature review**: Systematic reviews aim to address the problems by identifying, critically evaluating and integrating the findings of all relevant, high-quality individual studies addressing one or more research questions.

## (iii) Brief Notes:

* (iii1) **Motivation** : In software fault prediction many software metrics have been proposed. Many of them have been validated only in a small number of studies. Some of them have been proposed but never used. Contradictory results across studies have been reported. Even withing a single study, different resuslts have been obtained when different environments or methods have been used. The aim of this paper is to depict current state-of-the-art metrics in software fault prediction.

* (iii2) **Related Work** : A systematic review of software fault prediction studies was performed by Catal and Diri. Later, a literature reiew on the same topic was published. They included all papers concering software fault prediction. In 2012, a review similar in design to Catal and Diri's, but more comprehensive in terms of the number of included studies and analyses, was published by Hall et al. In the review, papers on software fault prediction were included focusing again on empirical studies. This paper is different from the above reviews in both the aim and scope of selected  studies. The objective of this review are to asses primary studies that empirically validate software metrics in software fault prediction and to assess metrics used in these studies according to several properties.

* (iii3) **Patterns**: Validations shoud be performed in the most realistic environment possible in order to acquire results relevant for the industry. In realistic environments, faults are fairly random and data sets are highly unbalanced (few faults, many correct modules). The number of faults and their distribution between two releases can be significantly different. Validation techniques, like a 10-fold cross-validation, 2/3 for training and 1/3 for testing, do not take into account all the factors that real environment validation does. Only validation where models are trained on release i and evaluated on i+1, can determine the impact of all these, and other unpredictable factors, of the environment.

* (iii4) **Results**: Object-oriented metrics (49%) were used nearly twice as often compared to traditional source code metrics (27%) or process metrics (24%). Chidamber and Kemerer's (CK) objected-oriented metrics were most frequently used. According to the selected studies there are significant differences between the metrics used in fault prediction performance. Objected-oriented and process metrics have been reported to be more successful in finding faults faults compared to any traditional size and complexity metrics.

## (iv) Future Work:
- More studies should be performed on large industrial software systems to find metrics more relevant for the industry and to answer the question as to which metrics should be used in a given context.
