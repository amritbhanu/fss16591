from .Learner import Learner
from sklearn.naive_bayes import GaussianNB
from stats import ABCD


class NaiveBayes(Learner):
    """docstring for NaiveBayes"""
    def __init__(self, *args):
        super(NaiveBayes, self).__init__(*args)

    def run(self):
        NB = GaussianNB()
        NB.fit(self.data.get_train_data(), self.data.get_train_label())
        predict = NB.predict(self.data.get_test_data())
        # print predict
        abcd = ABCD(before=self.data.get_test_label, after=predict)
        recall = np.array([j.stats()[0] for j in abcd()])
        return recall
