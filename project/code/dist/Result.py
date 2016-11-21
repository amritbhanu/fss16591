import sys
sys.dont_write_bytecode = True


class Result(object):
    """docstring for Result"""
    def __init__(self):
        super(Result, self).__init__()
        self.recall = {}
        self.precision = {}
        self.accuracy = {}
        self.f_score = {}
        self.scores = {
            "Recall": self.get_recall,
            "Precision": self.get_precision,
            "Accuracy": self.get_accuracy,
            "F_score": self.get_f_score,
        }

    def set_recall(self, learner, recall_score):
        self.recall[learner] = self.recall.get(learner, []) + [recall_score]

    def get_recall(self):
        recall = []
        for k, v in self.recall.iteritems():
            recall.append([k] + v)
        return recall

    def set_precision(self, learner, precision_score):
        self.precision[learner] = self.precision.get(learner, []) + \
                                  [precision_score]

    def get_precision(self):
        precision = []
        for k, v in self.precision.iteritems():
            precision.append([k] + v)
        return precision

    def set_accuracy(self, learner, accuracy_score):
        self.accuracy[learner] = self.accuracy.get(learner, []) + \
                                 [accuracy_score]

    def get_accuracy(self):
        accuracy = []
        for k, v in self.accuracy.iteritems():
            accuracy.append([k] + v)
        return accuracy

    def set_f_score(self, learner, f_score_val):
        self.f_score[learner] = self.f_score.get(learner, []) + [f_score_val]

    def get_f_score(self):
        f_score = []
        for k, v in self.f_score.iteritems():
            f_score.append([k] + v)
        return f_score
