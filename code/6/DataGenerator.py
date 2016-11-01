from Table import Table
import random
import numpy as np
from sklearn.naive_bayes import GaussianNB
from ABCD import ABCD


class DataGenerator(object):
    """docstring for DataGenerator"""

    def __init__(self, filename):
        # random.seed(50)
        table = Table(filename)
        self.data = table.rows
        self.data = self.data*20
        self.randomIndexType1 = []
        self.randomIndexType2 = []
        self.randomDataType1 = []
        self.randomDataType2 = []
        self.random_type1()
        self.random_type2()
        print len(self.randomDataType1), len(self.randomDataType2)
        self.newData = self.randomDataType1 + self.randomDataType2

    def random_type1(self):
        class_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        label = class_labels[0]

        while len(self.randomIndexType1) < 500:
            randIndex = random.randint(0, len(self.data) - 1)
            randomRow = self.data[randIndex]
            if ((randomRow[-1] == label) & (randIndex not in self.randomIndexType1)):
                self.randomIndexType1.append(randIndex)
                self.randomDataType1.append(randomRow)

        label = class_labels[1]
        while len(self.randomIndexType1) < 1000:
            randIndex = random.randint(0, len(self.data) - 1)
            randomRow = self.data[randIndex]
            if ((randomRow[-1] == label) & (randIndex not in self.randomIndexType1)):
                self.randomIndexType1.append(randIndex)
                self.randomDataType1.append(randomRow)

    def random_type2(self):
        class_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        label = class_labels[0]

        while len(self.randomIndexType2) < 100:
            randIndex = random.randint(0, len(self.data) - 1)
            randomRow = self.data[randIndex]
            if ((randomRow[-1] == label) & (randIndex not in self.randomIndexType2)):
                self.randomIndexType2.append(randIndex)
                self.randomDataType2.append(randomRow)

        label = class_labels[1]
        while len(self.randomIndexType2) < 400:
            randIndex = random.randint(0, len(self.data) - 1)
            randomRow = self.data[randIndex]
            if ((randomRow[-1] == label) & (randIndex not in self.randomIndexType2)):
                self.randomIndexType2.append(randIndex)
                self.randomDataType2.append(randomRow)

        label = class_labels[2]
        while len(self.randomIndexType2) < 1000:
            randIndex = random.randint(0, len(self.data) - 1)
            randomRow = self.data[randIndex]
            if ((randomRow[-1] == label) & (randIndex not in self.randomIndexType2)):
                self.randomIndexType2.append(randIndex)
                self.randomDataType2.append(randomRow)


    def naiveBayes(self):
        for i in xrange(1, 21):
            print len(self.newData)
            print "Era #" + str(i) + ":"
            startIndex = (i-1)*100
            endIndex = (i)*100
            train = self.newData[startIndex:((endIndex/2)-1)]
            test = self.newData[(endIndex/2):endIndex]
            train_label = []
            test_label = []
            data_train = []
            data_test = []
            for x in train:
                train_label.append(x[-1])
                data_train.append(x[:-1])
            for x in test:
                test_label.append(x[-1])
                data_test.append(x[:-1])
            NB = GaussianNB()
            NB.fit(data_train,train_label)
            predict=NB.predict(data_test)
            print predict
            # abcd = ABCD(before=test_label, after=predict)
            # recall for 1st target class
            # print np.array([j.stats()[0] for j in abcd()])[0]

    # Dr.Menzies code.
    def a12(list1, list2):
        more = same = 0.0
        for x in sorted(list1):
            for y in sorted(list2):
                if   x==y :
                    same += 1
                elif x > y :
                    more += 1
        return (more + 0.5*same) / (len(list1)*len(list2))


if __name__ == "__main__":
    dg = DataGenerator("data.csv")
    dg.naiveBayes()