from dist.Data import Data
from dist.Result import Result
from dist.Read import Read
from random import shuffle, randint, random, seed
from dist.learners.LearnerExecutor import LearnerExecutor
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import NearestNeighbors
from dist.stats.sk import rdivDemo
import numpy as np
import pickle
import sys
sys.dont_write_bytecode = True


class Handler(object):
    """
        This class is the entry point to any learners.
    """
    def __init__(self, list_of_files, m, n, list_of_learners):
        super(Handler, self).__init__()
        self.list_of_files = list_of_files
        self.list_of_learners = list_of_learners
        seed(0)
        for index, file in enumerate(list_of_files):
            data = Data()
            result = Result()
            Read(file, data)
            try:
                data.get_content()
                self.cross_validate(data, result, m, n)
            except:
                continue

    def split(self,inp, out, n_folds):
        skf = StratifiedKFold(n_splits=n_folds, random_state=None, shuffle=True)
        inp, out = np.array(inp), np.array(out)
        for train_index, test_index in skf.split(inp, out):
            yield inp[train_index], out[train_index], inp[test_index], out[test_index]

    def smote(self,data1, num, k=5):
        corpus = []
        nbrs = NearestNeighbors(n_neighbors=k + 1, algorithm='ball_tree').fit(data1)
        distances, indices = nbrs.kneighbors(data1)
        for i in range(0, num):
            mid = randint(0, len(data1) - 1)
            nn = indices[mid, randint(1, k)]
            datamade = []
            for j in range(0, len(data1[mid])):
                gap = random()
                datamade.append((data1[nn, j] - data1[mid, j]) * gap + data1[mid, j])
            corpus.append(datamade)
        corpus = np.array(corpus)
        return corpus

    def balance(self,data_train, train_label, neighbors=5):
        pos_train = []
        neg_train = []
        for j, i in enumerate(train_label):
            if i == 1:
                pos_train.append(data_train[j])
            else:
                neg_train.append(data_train[j])
        pos_train = np.array(pos_train)
        neg_train = np.array(neg_train)
        if len(pos_train) < len(neg_train):
            num = int((len(pos_train) + len(neg_train)) / 2)
            pos_train = self.smote(pos_train, num, k=neighbors)
            neg_train = neg_train[np.random.choice(len(neg_train), num, replace=False)]
            data_train1 = np.vstack((pos_train, neg_train))
            label_train = [1] * len(pos_train) + [0] * len(neg_train)
            return data_train1, label_train
        else:
            num = int((len(pos_train) + len(neg_train)) / 2)
            neg_train = self.smote(neg_train, num, k=neighbors)
            pos_train = pos_train[np.random.choice(len(pos_train), num, replace=False)]
            data_train1 = np.vstack((pos_train, neg_train))
            label_train = [1] * len(pos_train) + [0] * len(neg_train)
            return data_train1, label_train

    def cross_validate(self, data, result, m, n):
        if not n: splits = 2
        else: splits = n
        if not m: folds = 1
        else: folds = m
        for _ in xrange(folds):
            shuffle(data.get_content())
            labels = [1 if row[-1] > 0 else 0 for row in data.get_content()]
            content = self.split(data.get_content(), labels, splits)
            for train_inp, train_out, test_inp, test_out in content:
                ## Smoting the highly inbalanced class
                train_inp, train_out = self.balance(train_inp,
                                                    train_out,
                                                    neighbors=5)
                data.set_train_data(train_inp)
                data.set_train_label(train_out)
                data.set_test_data(test_inp)
                data.set_test_label(test_out)
                ## here run all learners
                self.run_learners(data, result)

        for k, v in result.scores.iteritems():
            print k
            self.stats(v())
            print ""

        ##dump results:
        f = {'dataset1':{'learner1':{'measure1':[1,1,1,1]}}}
        with open('./dump/result.pickle', 'wb') as handle:
            pickle.dump(f, handle)

    def run_learners(self, data, result):
        LearnerExecutor(self.list_of_learners, data, result)

    def stats(self, dict=[]):
        rdivDemo(dict)

    # Just for testing
    def test(self):
        print self.list_of_files
        