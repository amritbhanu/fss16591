# Paper 4 summary

## (i) Reference : Bird, Christian, Nachiappan Nagappan, Harald Gall, Brendan Murphy, and Premkumar Devanbu. "Putting it all together: Using socio-technical networks to predict failures." In 2009 20th International Symposium on Software Reliability Engineering, pp. 109-119. IEEE, 2009.

## (ii) Keywords:

* (ii1) **SNA**: Social network analysis (SNA) is the process of investigating social structures through the use of network and graph theories.
* (ii2) **Contribution network**: Contribution network captures the contributions of developers to software components within the system.
* (ii3) **Dependency network**: Dependency network models the dependency relationships between the software components within the system.
* (ii4) **Socio-technical Network**: A socio-technical network is created by combining dependency and contribution relationships into on graph. Both of the above networks deal with information & control flow. The joint network then, captures the interaction between the two.

## (iii) Brief Notes:

* (iii1) **Motivation** : Task assignment (i.e. who worked on which components and how much) and dependency structure (which components have dependencies on others) together interact to influence the quality of the resulting software. It can be very difficult and expensive to test all of the components of a large and complex system. However, the complexity inherent in large software systems can be leveraged to aid in locating those components which are particularly defect prone. Components which play key roles and are central in these networks tend to be more failure prone than components in the surrounding areas.

* (iii2) **Related Work** : Results shows that models built on social network metrics were better indicators of future failures than models based on standard source code metrics. This approach leveraged SNA metrics to capture both local and global effects of network connectivity on defect-proneness. Software artifacts such as email interactions, and developers contribution history have also influenced SNA. That global connectivity measures such as _betweenness_ were better indicators of development activity than local measures such as _degree centrality_. But by studying contribution history, degree centrality, closeness centrality, and Bonacich power have very good predictive power.

* (iii3) **Patterns**: The role of a software component in the dependency network and its role in the developer contribution network together influence defect proneness. Software components that play key roles in the joint socio-technical network are more prone to defects than those that don't. Logistic regression to examine the relationship between social network analysis metrics and post-release failures. They used PCA to reduce the dimensionality of feature space.

* (iii3) **Assessment**: Global measures examine the position of the component within the context of the entire network and include betweenness, Bonacich Power, and eigenvector centrality. Local measures only take into account the neighborhood of nodes within one or two hops of software component. These include measures such as degree, size of the network, and edge density. Broad description on these measures are available in this paper. And to evaluate their prediction results, they reported precision, recall and fscore.

## (iv) Improvisations:
- (iv1) They studied 2 projects, one from an industrial setting and another from open source community, but we can argue that based on previous studies, these results can be helpful only few datasets. It can still get affected from external validity. More datasets results should be reported.
- (iv2) Its an interesting study of using socio technical graph for predicting the efforts. It would be great to see the results of previous defect predictions combined with socio technical network.
