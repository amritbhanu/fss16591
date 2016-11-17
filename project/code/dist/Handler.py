from dist.Data import Data
from dist.Read import Read
from random import randint
from dist.learners.Learner import LearnerExecutor

class Handler(object):
    """docstring for Handler"""
    def __init__(self, list_of_files, m, n):
        super(Handler, self).__init__()
        self.list_of_files = list_of_files
        dict_of_data = {}
        for index, file in enumerate(list_of_files):
            data = Data()
            Read(file, data)
            self.cross_validate(data, m, n)
            self.run_learners(data)
            # dict_of_data[index] = data.get_results()

    def cross_validate(self, data, m, n):
        len_of_content = len(data.get_content())
        if not m: m = len_of_content/2
        if not n: n = len_of_content/2
        data.set_train_data([data.get_content()[randint(0, len_of_content - 1)]
                             for _ in xrange(m)])
        data.set_train_label()
        data.set_test_data([data.get_content()[randint(0, len_of_content - 1)]
                            for _ in xrange(n)])
        data.set_test_label()

    def run_learners(self, data):
        learner = LearnerExecutor(data)


    # Just for testing
    def test(self):
        print self.list_of_files
        