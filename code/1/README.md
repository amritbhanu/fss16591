# Week 1

## eg0
- First it finds text with "attribute" in the dataset weather.arff/
- It selects 5 columns, separated by "," and sort the data from A-Z on the attribute Outlook
- Now these columns which are separated by "," are put into proper format by putting each column separated by a "tab".
- On the weather.arff dataset j48 learner is used by 10 cross validation and as a output only para 3 is selected.

## eg1
- It selects 5 columns, separated by "," and sort the data from A-Z on the attribute Outlook
- Now these columns which are separated by "," are put into proper format by putting each column separated by a "tab".

## eg2
- On the weather.arff dataset j48 learner is used by 10 cross validation and each line is appending with line nos.

## eg3
- j48 learner is provided with training dataset and testing dataset, which are actually same.
- That's the reason why we got Predictions with 100% accuracy.

## eg4
- just an echo statement to print on the screen.
- function eg3 is called and piped through another function "wantgot".
- wantgot function is just making the output of eg3 readable to human eyes.
- this function skips the first row and then prints the Actual and Predicted values from the learner results.

## eg5
- eg4 function is called which printed just the actual and predicted values.
- the output is piped through another function "abcd".
- abcd function is evaluating few of the metrics such as precision, accuracy, recall and fscore for the 2 binary classes "yes" and "no".
- Here we are getting 100% results for everything because training and testing set was the same.

## eg6
- crossval is a function which took couple of arguments with 1,3 as how many crossvals, then dataset which needs to be divided into training and testing set.
- It then takes the crossover probability to shuffle data. 2 learners are run through which are j48 and jrip.
- It is a stratified crossval as it divides the dataset into 3 bins and randomise data for testing on 1 bin and training on the other 2 bins.
- Since we have 3 different training and testing sets, each learner ran 3 times.
- This time we got different precision, recall, accuracy, and fscores.

## eg7
- There is a temprory out directory set to store results. 
- This time 5x5 crossval is used. Dataset is divided into 5 bins and ran 5 times with a random seed to shuffle the data.
- 2 learners are used j48 and jrip but this time they ran 5 times each.
- The output is saved using gawk by extracting yes class with its false alarm and recall into 2 files. Files are saved in a temporary folder out.

## eg8
- eg8 is similar to eg7 but this time false alarm and recall is saved in the out directory by actually specifying the column names.
- column is provided to actually retrieve the results based on column name rather than gawk

## eg9
- The output which was saved in a temporary files after running eg8 is made use here.
- This is a statistical test (scott-knott) to separate which learner performed better based on median and IQR values.
- Both learners performed, ie wrt false alarm and recall, the same according to scott-knott test. 

## eg10
- the dataset used is jedit.arff and ran with 5 learners j48, jrip, nb, rbfnet and bnet. 
- crossval of 5x5 with random seed to shuffle data. The results (false alarm and recall) are saved in local out directory.
- scott knott is ran again but we can see from recall we got different learners different ranks. This is because different ranges of median with higher IQR.
- but for false alarm we got the same rankings.
- Learners
  - j48 is a a decision tree learner which implements C4.5 algorithm. Based on different entropy values, it finds which attributes are the most important ones to identify a particular class. Down the tree, it starts pruning those leaves depending on its entropy.
  - jrip is an propositional rule learner. Repeated Incremental Pruning to Produce Error Reduction. It starts with an error rate >= 50% and then it starts growing and keeps adding the conditions until it makes rules 100% accurate. It uses a pruning strategy to rule out some of the conditions.
