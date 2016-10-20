# Paper 6 summary

## (i) Reference : Martin Shepperd, David Bowes and Tracy Hall. "Researcher Bias: The Use of Machine Learning in Software Defect Prediction."

## (ii) Keywords:

* (ii1) **Software defect prediction**: Software Defect Prediction (SDP) is one of the most assisting activities of the Testing Phase of SDLC. It identifies the modules that are defect prone and require extensive testing. This way, the testing resources can be used efficiently without violating the constraints.

* (ii2) **Meta-Analysis**: In statistics, meta-analysis comprises statistical methods for contrasting and combining results from different studies, in the hope of identifying patterns among study results, sources of disagreement among those results, or other interesting relationships that may come to light in the context of multiple studies.

* (ii3) **Researcher Bias**: Research bias, also called experimenter bias, is a process where the scientists performing the research influence the results, in order to portray a certain outcome.

## (iii) Brief Notes:

* (iii1) **Motivation** : The ability to predict defect-prone software components would be valuable. Consequently, there have been many empirical studies to evaluate the performance of different techniques endeavouring to accomplish this effectively. However, no one technique dominates and so designing a reliable defect prediction model remains problematic. This paper seek to make sense of the many conflicting experimental results and understand which factors have the largest effect on predictive performance.

* (iii2) **Related Work** : There has been very substantial research effort put into software defect prediction. However, a consensus on what are the best prediction techniques, even for a specific context, remains elusive. This paper finds con- siderable diversity as to what form of classifier technique should be used and what inputs or metrics work best. In addition, in order to facilitate generalisation, researchers are using an increasing number of different defect data sets for empirical validation. Unfortunately the situation is somewhat complicated by the use of a wide range of validation schemes. The time is ripe to explore the underlying reasons for this lack of convergence in results hence we conduct a meta-analysis. This will provide pointers to the most effective way forward for future software defect prediction research.

* (iii3) **Patterns**: .

* (iii4) **Results**: What is striking, however, is the number of observations of the correlation coefficient being close to zero or even negative. This reveals that many classifiers are performing extremely poorly, since zero indicates no relationship at all and could therefore be achieved through guessing. A negative value means the prediction would be improved by adding an inverter. Moreover, the modal value lies in the range 0.3-0.4 which hardly engenders a great deal of confidence in terms of their practical use. The following table shows these results.

![alt tag](https://github.com/amritbhanu/fss16591/blob/master/read/6/Screenshot%202016-10-19%2021.51.17.png)

## (iv) Future Work:
- Until we move on from the situation where it doesn’t matter what you do, merely who does it, progress will be restricted since this research is not reproducible.
