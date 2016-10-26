## Week 8

- All datasets are coming from Weka.
- All datasets got binary classes
- all classification is using Naive Bayes

### Feature selection using j48 M=2 trick 

| Datasets     | number of selected features   | precision | recall | irregularities|
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
|  diabetes.arff |  4 / 8 | 0.794 / 0.802 | 0.866 / 0.844 | |
|  breast-cancer.arff | 3 / 9  | 0.756 / 0.778  | 0.925 / 0.836 | |
|  german_credit.arff | 9 / 20 | 0.774 / 0.800 | 0.874 / 0.864 | |
|  ionosphere.arff | 5 / 34  | 0.794 / 0.712  | 0.794 / 0.865 |  Classic example of overfitting|
|  vote.arff | 5 / 16 | 0.974 / 0.944 | 0.966 / 0.891 | |
|  weather.arff | - / 4 | - / 0.636 | - / 0.778 |  it didnt run |

### Wrapper feature selection 
- classifier subset eval and classifier used is NB (selected features/all features)

| Datasets     | selected features   | precision | recall |  irregularities|
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
|  diabetes.arff |  5 / 8 | 0.799 / 0.802 | 0.880 / 0.844 | |
|  breast-cancer.arff | 6 / 9  | 0.772 / 0.778  | 0.891 / 0.836 | |
|  german_credit.arff | 15 / 20 | 0.798 / 0.800 | 0.866 / 0.864 | | 
|  ionosphere.arff | 5 / 34  | 0.893 / 0.712  | 0.865 / 0.865 |  Classic example of overfitting|
|  vote.arff | 3 / 16 | 0.947 / 0.944 | 0.940 / 0.891 | |
|  weather.arff | 3 / 4 | 0.600 / 0.636 | 0.667 / 0.778 | |

### Filter feature selection 
- infogain

| Datasets     | number of selected features   | precision | recall |  irregularities|
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
|  diabetes.arff |  2 / 8 | 0.776 / 0.802 | 0.896 / 0.844 | |
|  breast-cancer.arff | 2 / 9  | 0.764 / 0.778  | 0.935 / 0.836 | |
|  german_credit.arff | 5 / 20 | 0.781 / 0.800 | 0.866 / 0.864 | |
|  ionosphere.arff | 7 / 34  | 0.846 / 0.712  | 0.825 / 0.865 |  |
|  vote.arff | 3 / 16 | 0.966 / 0.944 | 0.948 / 0.891 | |
|  weather.arff | 2 / 4 | 0.800 / 0.636 | 0.889 / 0.778 | | 
