from dist.learners.Learner import Learner
from dist.stats.ABCD import ABCD
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import sys
sys.dont_write_bytecode = True

class DT(Learner):
    """docstring for DT"""
    def __init__(self, *args):
        super(DT, self).__init__(*args)

    def run(self):
        DT = DecisionTreeClassifier(criterion='entropy')
        DT.fit(self.data.get_train_data(), self.data.get_train_label())
        predict = DT.predict(self.data.get_test_data())
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