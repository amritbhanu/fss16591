from dist.learners.Learner import Learner
from sklearn.naive_bayes import GaussianNB
from dist.stats.ABCD import ABCD
import numpy as np
import sys
sys.dont_write_bytecode = True


class NB(Learner):
    """docstring for NB"""
    def __init__(self, *args):
        super(NB, self).__init__(*args)

    def run(self):
        NB = GaussianNB()
        NB.fit(self.data.get_train_data(), self.data.get_train_label())
        predict = NB.predict(self.data.get_test_data())
        # print predict
        abcd = ABCD(before=self.data.get_test_label(), after=predict)
        stats = np.array([j.stats() for j in abcd()])
        labels = list(set(self.data.get_test_label()))
        if labels[0] == 0:
            labelone = 0
        else:
            labelone = 1
        # return recall (0), prec(3), accuracy(4), fscore(5)
        return stats[labelone][0], stats[labelone][3], \
               stats[labelone][4], stats[labelone][5]
