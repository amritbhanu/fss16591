from dist.learners import NB, KNN, DT, SVM, RF, LR
from config import LEARNERS
import sys
sys.dont_write_bytecode = True


class LearnerExecutor(object):
    """docstring for LearnerExecutor"""
    def __init__(self, list_of_learners, data, result):
        super(LearnerExecutor, self).__init__()
        for learner in list_of_learners:
            self.run_learner(learner, data, result)

    def run_learner(self, learner, data, result):
        l = LEARNERS[learner](data)
        recall, precision, accuracy, f_score = l.run()
        result.set_recall(learner, round(recall, 3))
        result.set_precision(learner, round(precision, 3))
        result.set_accuracy(learner, round(accuracy, 3))
        result.set_f_score(learner, round(f_score, 3))
