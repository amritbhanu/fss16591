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
        r = l.run()
        content = [str(learner)] + [round(val, 3) for val in r]
        result.set_content(content)
