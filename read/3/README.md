# Paper 1 summary

## (i) Reference : D'Ambros, Marco, Michele Lanza, and Romain Robbes. "An extensive comparison of bug prediction approaches." In 2010 7th IEEE Working Conference on Mining Software Repositories (MSR 2010), pp. 31-41. IEEE, 2010.

## (ii) Keywords:

* (ii1) **Change Log Approaches**: It uses information extracted from the versioning system, assuming that recently or frequently changed files are the most probable source of future bugs.
* (ii2) **Single-version approaches**: It assumes that the current design and behavior of the program influences the presence of future defects. These approaches do not require the history of the system, but analyze its current state in more detail, using a variety of metrics.
* (ii3) **Principal Component Analysis (PCA)**: Principal component analysis (PCA) is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components. The number of principal components is less than or equal to the number of original variables.
* (ii3) **EDHCM**: Exponentially Decayed HCM, every file modified in the considered period i gets the entropy of the system in the considered time interval.

## (iii) Brief Notes:

* (iii1) **Motivation** : The driving scenario is resource allocation: Time and manpower being finite resources, it makes sense to assign personnel and/or resources to areas of a software system with a higher probable quantity of bugs. They are making it more automated so that it takes less man power.
* (iii2) **Related Work** : To tackle there were many approaches suggested code metrics (lines of code, complexity), process metrics (number of changes, recent activity) or previous defects. Relative code churn was a better predictor than absolute churn. The bug-introducing changes are identified from the SCM logs.  Comparative study among process metrics, system metrics, defect information related and bi-weekly models of each system version if new metrics need to be computed. Entropy was compared to amount of changes and the amount of previous bugs. Chidamber and Kemerer (CK) metrics suite, McCabe’s cyclomatic complexity, Briand’s coupling metrics, code metrics, dependencies between binaries, cohesion measurement based on LSI.
* (iii3) **Patterns** : Predictions at the package-level are less helpful since packages are significantly larger. Package-level information can be derived from class-level information, while the opposite is not true. They used PCA, built regression model. Approaches based on churn and entropy of source code
metrics have good and stable explanative and predictive power, better than all the other applied approaches. Using the source code metrics, CK+OO to predict
bugs has several advantages: They are lightweight to compute, have good explanative and predictive power and do not require historical information. Using the CK and the OO metric sets together is preferable to using them in isolation, as the performances are more stable across case studies. Bug prediction approaches based on a single metric are not stable over the case studies. The best weighting for past metrics is the linear one. Using string matching on versioning system comments, without validating it on the bug database, decreases the accuracy of bug prediction. Combining bugs and OO metrics improves predictive power. Adding this data to WCHU improves explanation, but degrades prediction, while adding it to LDHH improves both explanation and prediction.
* (iii4) **Results** :
![alt tag](https://github.com/amritbhanu/fss16591/blob/master/read/3/results.png)
* (iii5) **Datasets** : Six open-source systems: FreeBSD, NetBSD, OpenBSD, KDE, KOffice, and PostgreSQL. Apache, PostgreSQL, Subversion, Mozilla, JEdit, Columba, and Eclipse. Datasets publicly available at http://bug.inf.usi.ch

## (iv) Improvisations:
- (iv1) Set of bugs which are linked to commit comments is not a fair representation of the full population of bugs. Need to have better sampling technique.
- (iv2) Considerable fraction of problem reports marked as bugs in Bugzilla (according to their severity) are indeed "non bugs". Need an automated technique to find bugs or not bugs.
