from Table import Table
import random
import numpy as np
import math
from sklearn.naive_bayes import GaussianNB
from ABCD import ABCD


class DataGenerator(object):
    """docstring for DataGenerator"""

    def __init__(self, filename):
        table = Table(filename)
        self.data = table.rows
        while len(self.data) < 2000:
            self.data.append(table.rows[random.randint(0, len(table.rows) - 1)])
        self.randomIndexType1 = []
        self.randomIndexType2 = []
        self.randomDataType1 = []
        self.randomDataType2 = []
        self.random_type1()
        self.random_type2()
        # print self.randomDataType1
        # print self.randomDataType2
        random.shuffle(self.randomDataType1)
        random.shuffle(self.randomDataType2)
        self.newData =  self.randomDataType1 + self.randomDataType2 

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
        list1 = list2 = []
        a12Score = olda12Score = 0
        for i in xrange(0, 20):
            if i==0:
                endIndexTrainData = 100
                startIndex = 0
                endIndexTestData = 100
            else:
                endIndexTrainData = (i)*100
                endIndexTestData = (i+1)*100
                startIndex = endIndexTrainData + 1
            # print startIndex, endIndexTrainData, endIndexTestData
            train = self.newData[0:endIndexTrainData]
            test = self.newData[startIndex:endIndexTestData]
            # print train, test
            train_label = []
            test_label = []
            data_train = []
            data_test = []
            labelMap = {
                'Iris-setosa': -1,
                'Iris-versicolor': 0,
                'Iris-virginica': 1
            }
            for x in train:
                train_label.append(labelMap[x[-1]])
                data_train.append(x[:-1])
            for x in test:
                test_label.append(labelMap[x[-1]])
                data_test.append(x[:-1])
            NB = GaussianNB()
            NB.fit(np.array(data_train),train_label)
            predict=NB.predict(data_test)
            # print predict
            abcd = ABCD(before=test_label, after=predict)
            recall = np.array([j.stats()[0] for j in abcd()])
            # recall for 1st target class
            class1 = recall[0]
            class2 = recall[1]
            try:
                class3 = recall[2]
            except:
                class3 = 0
            print "Era " + str(i)
            print "Class 1: " + str(class1)
            print "Class 2: " + str(class2)
            print "Class 3: " + str(class3)
            if i == 0:
                list1 = [class1, class2, class3]
                list2 = list1
            else:
                list1 = list2
                list2 = [class1, class2, class3]
                olda12Score = a12Score
                a12Score = self.a12(list1, list2)
            print "A12 Score: " + str(a12Score)
            if math.fabs(olda12Score - a12Score) > 0.2 * olda12Score:
                print "Anamoly detected!!"
            print ""

    # Dr.Menzies code.
    def a12(self, list1, list2):
        more = same = 0.0
        for x in sorted(list1):
            for y in sorted(list2):
                if x == y:
                    same += 1
                elif x > y:
                    more += 1
        return (more + 0.5*same) / (len(list1)*len(list2))


if __name__ == "__main__":
    dg = DataGenerator("data.csv")
    dg.naiveBayes()