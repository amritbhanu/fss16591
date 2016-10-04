from __future__ import division
from Table import Table
from random import random


class RawKNN(object):
    """docstring for RawKNN"""

    def __init__(self, table):
        self.table = table

    def classify(self, index, row):
        self.row = row
        closestRow = self.table.minDistance(index, row)
        # here we took only 1, because Dr.Menzies wants us to implement 1NN.
        # So we are returning actual class, predicted class.
        return row[-1], closestRow[-1]

class MiniBatchKMeans(object):

    def __init__(self, table):
        self.clusters = {}
        self.table = table
    
    def classify(self):
        miniBatchSize = 20
        numberOfClusters = 20
        iterations = 20
        nearestCenter = {}
        for i in xrange(iterations):
            learningData = random.sample(self.table.rows, miniBatchSize)
            for index, row in enumerate(learningData):
                nearestCenter[index] = table.minDistance(index, row)
            for index, row in enumerate(learningData):
                pass
                # WIP



if __name__ == '__main__':
    csvFile = './data/iris.csv'
    table = Table(csvFile)
    # for index, row in enumerate(table.rows):
    #     print "Current: " + str(index) + ", " + str(row)
    #     print "Closest: " + str(table.minDistance(row, index))
    #     print "Farthest: " + str(table.maxDistance(row, index))
    # print table.rows
    # Shuffle the list 5 times instead of 5x5 cross val.
    # for i in xrange(5):
    # trainData = table.rows[:8]
    # testData = table.rows[8:]
    print "########### Raw KNN ###########"
    rawKnn = RawKNN(table)
    for index, row in enumerate(table.rows):
        actual, predicted = rawKnn.classify(index, row)
        print str(actual) + ": " + str(predicted)
    print "########### KNN KMeans ###########"
    # kmeans = MiniBatchKMeans(table)


