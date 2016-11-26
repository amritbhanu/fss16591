from Learner import Learner
from sklearn import neighbors
import sys

sys.dont_write_bytecode = True


class KNN(Learner):
    """docstring for KNN"""
    def __init__(self, *args):
        super(KNN, self).__init__(*args)

    def __str__(self):
        return "K-Nearest Neighbours"

    def run(self):
        knn = neighbors.KNeighborsClassifier(n_neighbors=8)
        knn.fit(self.data.get_train_data(), self.data.get_train_label())
        return knn.predict(self.data.get_test_data())
