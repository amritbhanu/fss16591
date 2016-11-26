from Learner import Learner
from sklearn.svm import SVC
import sys

sys.dont_write_bytecode = True


class SVM(Learner):
    """docstring for SVM"""
    def __init__(self, *args):
        super(SVM, self).__init__(*args)

    def __str__(self):
        return "Support Vector Machines"

    def run(self):
        svm = SVC(kernel='linear')
        svm.fit(self.data.get_train_data(), self.data.get_train_label())
        return svm.predict(self.data.get_test_data())
