## Fault Prediction -- pre-release name

The following are steps to install.

  - Install virtual environment. (Optional but recommended)
  - Then run the following:
```sh
  $ cd code # Basically set cwd to code
  $ pip install --editable .
  $ learners --help # displays options
  $ learners f <path_to_file_or_dir>
```
  - Magic

## Experiments:
- 6 Learners [KNN, NB, SVM, LR, DT, RF]
- with smote and without smote, 5x5 cross val
- only 14 datasets, other datasets from openscience were very small.
- compared against 4 measures, [Precision, recall, accuracy, f_score]

## Conclusions:
- 

## Results: 
### With Smote:

![file](https://github.com/amritbhanu/fss16591/raw/master/project/Accuracy_smote.png | height=24 width=48)

![file](https://github.com/amritbhanu/fss16591/raw/master/project/Precision_smote.png)

![file](https://github.com/amritbhanu/fss16591/raw/master/project/Recall_smote.png)

![file](https://github.com/amritbhanu/fss16591/raw/master/project/F_score_smote.png)


### Without Smote:


![file](https://github.com/amritbhanu/fss16591/raw/master/project/Accuracy_nosmote.png)

![file](https://github.com/amritbhanu/fss16591/raw/master/project/Precision_nosmote.png)

![file](https://github.com/amritbhanu/fss16591/raw/master/project/Recall_nosmote.png)

![file](https://github.com/amritbhanu/fss16591/raw/master/project/F_score_nosmote.png)
