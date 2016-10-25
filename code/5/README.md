# Week 5
- Datasets used are Camel-1.0.csv which was downloaded from [Promise Repository] (http://openscience.us/repo/defect/ck/camel.html) and other one is diabetes.csv provided with ninja
- Datasets are available [here] (https://github.com/amritbhanu/fss16591/tree/master/code/4/data)
- Experiments are ran with 5 fold cross val ie. 80% training and 20% testing
- Results reported are false alarm, recall and runtimes.
- Scott-knot analysis is done to generate pretty figures.
- Run the code with **python CompareLearners.py**
- All predictions on test data are done with k=1 for the 2 trees ie, Minibatch K means, KD tree and compared against Naive Bayes.
## Results

### Scott-knott analysis
```
diabetes.csv

Recall
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,         mini ,    0.66  ,  0.10 (          ---* |              ), 0.62,  0.66,  0.72
   1 ,           kd ,    0.66  ,  0.10 (          ---* |              ), 0.62,  0.66,  0.72
   2 ,           NB ,    0.84  ,  0.03 (               |       -*     ), 0.83,  0.84,  0.86

False Alarm
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           NB ,    0.40  ,  0.07 (    --*        |              ), 0.37,  0.40,  0.44
   2 ,         mini ,    0.65  ,  0.17 (               | -----*       ), 0.58,  0.65,  0.75
   2 ,           kd ,    0.65  ,  0.17 (               | -----*       ), 0.58,  0.65,  0.75


camel-1.0.csv

Recall
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           NB ,    0.94  ,  0.06 (               |           -* ), 0.91,  0.94,  0.97
   1 ,         mini ,    1.00  ,  0.03 (               |             *), 0.97,  1.00,  1.00
   1 ,           kd ,    1.00  ,  0.03 (               |             *), 0.97,  1.00,  1.00
   
False Alarm
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           NB ,    0.50  ,  0.67 (--------------*|              ), 0.00,  0.50,  0.67
   2 ,         mini ,    1.00  ,  0.00 (               |             *), 1.00,  1.00,  1.00
   2 ,           kd ,    1.00  ,  0.00 (               |             *), 1.00,  1.00,  1.00

```

### Runtimes of just 1 cross val in seconds.
- 'diabetes.csv': {'mini': 1.1872940063476562, 'NB': 0.05073714256286621, 'kd': 0.05971837043762207}
- 'camel-1.0.csv': {'mini': 0.8251402378082275, 'NB': 0.04028034210205078, 'kd': 0.040816307067871094}

### Answers
- NB is faster than the fastest knn but NBs performance affects.