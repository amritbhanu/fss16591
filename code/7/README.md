# Week 7
- Datasets used are 'camel-1.0.csv','arc.csv','ivy-2.0.csv','jedit-3.2.csv' which were downloaded from [Promise Repository] (http://openscience.us/repo/defect/ck/) and other one is diabetes.csv provided within ninja
- Datasets are available [here] (https://github.com/amritbhanu/fss16591/tree/master/code/4/data)
- Experiments are ran with 5 fold cross val ie. 80% training and 20% testing
- Scott-knot analysis is done to generate pretty figures.
- All predictions on test data are done Naive Bayes.

## Answers
- Discretization helped recall scores for Diabetes dataset. 
- But for most other datasets, normal NB classifier with discretization doesnt hurt much.
- But in some cases like arc.csv, discretization with NB performed really poor.

### Scott-knott analysis
```

diabetes.csv
Recall

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        width ,    0.59  ,  0.14 (     ---*      |              ), 0.54,  0.59,  0.68
   1 ,           NB ,    0.59  ,  0.14 (     ---*      |              ), 0.54,  0.59,  0.68
   2 ,     interval ,    0.84  ,  0.03 (               |       -*     ), 0.83,  0.84,  0.86
[(0, 0.58585858585858586, <sk.Num instance at 0x10c9b9638>), (1, 0.83999999999999997, <sk.Num instance at 0x10c9b9758>), (0, 0.58585858585858586, <sk.Num instance at 0x10c9b93f8>)]
False Alarm

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.40  ,  0.07 (    -*         |              ), 0.37,  0.40,  0.44
   2 ,        width ,    0.69  ,  0.15 (               | ----*        ), 0.62,  0.69,  0.77
   2 ,           NB ,    0.69  ,  0.15 (               | ----*        ), 0.62,  0.69,  0.77
[(1, 0.6938775510204082, <sk.Num instance at 0x10c9b9638>), (0, 0.39622641509433965, <sk.Num instance at 0x10c9b9758>), (1, 0.6938775510204082, <sk.Num instance at 0x10c9b93f8>)]


camel-1.0.csv
Recall

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.94  ,  0.06 (               |           -* ), 0.91,  0.94,  0.97
   1 ,        width ,    1.00  ,  0.07 (               |           --*), 0.93,  1.00,  1.00
   1 ,           NB ,    1.00  ,  0.07 (               |           --*), 0.93,  1.00,  1.00
[(0, 1.0, <sk.Num instance at 0x10c9b9638>), (0, 0.93846153846153846, <sk.Num instance at 0x10c9b9758>), (0, 1.0, <sk.Num instance at 0x10c9b93f8>)]
False Alarm

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.50  ,  0.67 (--------------*|              ), 0.00,  0.50,  0.67
   2 ,        width ,    1.00  ,  0.00 (               |             *), 1.00,  1.00,  1.00
   2 ,           NB ,    1.00  ,  0.00 (               |             *), 1.00,  1.00,  1.00
[(1, 1.0, <sk.Num instance at 0x10c9b9638>), (0, 0.5, <sk.Num instance at 0x10c9b9758>), (1, 1.0, <sk.Num instance at 0x10c9b93f8>)]


arc.csv
Recall

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.49  ,  0.13 (             -*|              ), 0.44,  0.49,  0.57
   2 ,        width ,    0.93  ,  0.16 (               |         --*  ), 0.84,  0.93,  1.00
   2 ,           NB ,    0.93  ,  0.16 (               |         --*  ), 0.84,  0.93,  1.00
[(1, 0.9285714285714286, <sk.Num instance at 0x10c9b9638>), (0, 0.48888888888888887, <sk.Num instance at 0x10c9b9758>), (1, 0.9285714285714286, <sk.Num instance at 0x10c9b93f8>)]
False Alarm

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.50  ,  0.60 (--------------*|              ), 0.00,  0.50,  0.60
   2 ,        width ,    1.00  ,  0.20 (               |       ------*), 0.80,  1.00,  1.00
   2 ,           NB ,    1.00  ,  0.20 (               |       ------*), 0.80,  1.00,  1.00
[(1, 1.0, <sk.Num instance at 0x10c9b9638>), (0, 0.5, <sk.Num instance at 0x10c9b9758>), (1, 1.0, <sk.Num instance at 0x10c9b93f8>)]


ivy-2.0.csv
Recall

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.84  ,  0.03 (         -*    |              ), 0.83,  0.84,  0.85
   2 ,        width ,    0.95  ,  0.11 (               | -------*     ), 0.89,  0.95,  1.00
   2 ,           NB ,    0.95  ,  0.11 (               | -------*     ), 0.89,  0.95,  1.00
[(1, 0.95081967213114749, <sk.Num instance at 0x10c9b9638>), (0, 0.83606557377049184, <sk.Num instance at 0x10c9b9758>), (1, 0.95081967213114749, <sk.Num instance at 0x10c9b93f8>)]
False Alarm

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.75  ,  0.21 (               |   ---*       ), 0.67,  0.75,  0.88
   2 ,        width ,    1.00  ,  0.11 (               |          ---*), 0.89,  1.00,  1.00
   2 ,           NB ,    1.00  ,  0.11 (               |          ---*), 0.89,  1.00,  1.00
[(1, 1.0, <sk.Num instance at 0x10c9b9638>), (0, 0.75, <sk.Num instance at 0x10c9b9758>), (1, 1.0, <sk.Num instance at 0x10c9b93f8>)]


jedit-3.2.csv
Recall

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.19  ,  0.15 (   ---*        |              ), 0.11,  0.19,  0.26
   2 ,        width ,    0.67  ,  0.15 (               |    ---*      ), 0.57,  0.67,  0.73
   2 ,           NB ,    0.67  ,  0.15 (               |    ---*      ), 0.57,  0.67,  0.73
[(1, 0.66666666666666663, <sk.Num instance at 0x10c9b9638>), (0, 0.18604651162790697, <sk.Num instance at 0x10c9b9758>), (1, 0.66666666666666663, <sk.Num instance at 0x10c9b93f8>)]
False Alarm

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     interval ,    0.25  ,  0.50 (-------*       |              ), 0.00,  0.25,  0.50
   2 ,        width ,    0.92  ,  0.18 (               |        ---*  ), 0.82,  0.92,  1.00
   2 ,           NB ,    0.92  ,  0.18 (               |        ---*  ), 0.82,  0.92,  1.00
[(1, 0.9230769230769231, <sk.Num instance at 0x10c9b8c68>), (0, 0.25, <sk.Num instance at 0x10c9c5d88>), (1, 0.9230769230769231, <sk.Num instance at 0x10c9987e8>)]

```