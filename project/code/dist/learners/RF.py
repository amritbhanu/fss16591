from .Learner import Learner
from sklearn.ensemble import RandomForestClassifier
from dist.stats.ABCD import ABCD
import numpy as np
import sys
sys.dont_write_bytecode = True

class KNN(Learner):
    """docstring for KNN"""
    def __init__(self, **kwargs):
        super(KNN, self).__init__(**kwargs)

    def run(self):
        RF = RandomForestClassifier(criterion='entropy')
        RF.fit(self.data.get_train_data(), self.data.get_train_label())
        predict = RF.predict(self.data.get_test_data())
        # print predict
        abcd = ABCD(before=self.data.get_test_label(), after=predict)
        stats = np.array([j.stats() for j in abcd()])
        labels=list(set(self.data.get_test_label()))
        if labels[0] == 0:
            labelone=0
        else:
            labelone=1
        #return recall (0), prec(3), accuracy(4), fscore(5)
        return stats[labelone][0],stats[labelone][3],stats[labelone][4],stats[labelone][5]