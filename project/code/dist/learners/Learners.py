
from Table import Table
import random
import numpy as np
import math
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.neighbors import KDTree
from ABCD import ABCD


class Learners(object):

    def __init__(self):
        super(Learners, self).__init__()

    def read_data(self, file_name):
        table = Table(file_name)
        self.data = table.rows

    def run_all_learners(self):
        pass

    def build_train_test_dats(self):
        len_of_data = len(self.data)
        train = self.data[0:len_of_data/2]
        test = self.data[len_of_data/2:]
        # print train, test
        self.train_label = []
        self.test_label = []
        self.data_train = []
        self.data_test = []
        for x in train:
            self.train_label.append(x[-1])
            self.data_train.append(x[:-1])
        for x in test:
            self.test_label.append(x[-1])
            self.data_test.append(x[:-1])

    def naive_bayes(self):
        NB = GaussianNB()
        NB.fit(np.array(self.data_train), self.train_label)
        predict=NB.predict(self.data_test)
        # print predict
        abcd = ABCD(before=self.test_label, after=predict)
        recall = np.array([j.stats()[0] for j in abcd()])
        print recall

    def kmeans(self):
        kmeans = MiniBatchKMeans(init='random',n_clusters=20, n_init=20,batch_size=20,compute_labels=True)
        kmeans.fit(self.data_train,self.train_label)
        k_means_cluster_centers = np.sort(kmeans.cluster_centers_, axis=0)
        k_means_labels = pairwise_distances_argmin(self.data_train, k_means_cluster_centers)
        predict=kmeans.predict(self.data_test)
        prediction=[]
        for y in predict:
            prediction.append(self.train_label[y])
        abcd = ABCD(before=self.test_label, after=prediction)
        recall = np.array([j.stats()[0] for j in abcd()])
        print recall

    def kd_tree(self):
        prediction=[]
        tree = KDTree(self.data_train, metric='euclidean')
        _, ind=tree.query(self.data_test,k=1)
        #print(ind)
        predict=[item for sublist in ind for item in sublist]
        for y in predict:
            prediction.append(self.train_label[y])
        abcd = ABCD(before=self.test_label, after=prediction)
        recall = np.array([j.stats()[0] for j in abcd()])
        print recall


if __name__ == '__main__':
    learner = Learners()
    learner.read_data('./data/ant-1.7.csv')
    learner.build_train_test_dats()
    learner.naive_bayes()
    learner.kmeans()
    learner.kd_tree()
