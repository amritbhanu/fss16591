from config import LEARNERS
import sys
sys.dont_write_bytecode = True

class Learner(object):
    """docstring for Learner"""
    def __init__(self, data):
        super(Learner, self).__init__()
        self.data = data

    def run(self):
        pass


class LearnerExecutor(object):
    """docstring for LearnerExecutor"""
    def __init__(self, data, list_of_learners=None):
        super(LearnerExecutor, self).__init__()
        self.list_of_learners = list_of_learners

    def run_all(self):
        pass
