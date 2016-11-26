#!/usr/bin/env python
from __future__ import print_function

from config import LEARNERS
from random import seed
from Data import Data
from Result import Result
from ReadFile import ReadFile
from stats.sk import rdivDemo
from stats.ABCD import ABCD
import numpy as np
import sys

sys.dont_write_bytecode = True


class Learner(object):
    """
        1) This class is the entry point to execute learners.
        2) :params list_of_learners --> provide a list of learners.
           :params folds --> Data object.
           :params result --> Result object.
        3) Learner names can be found in config.py
    """
    def __init__(self, file_name, folds=2, splits=2):
        super(Learner, self).__init__()
        self.file_name = file_name
        self.folds = folds
        self.splits = splits
        if not file_name:
            raise Exception("Filename is required.")
        seed(0)
        self.data = Data()
        self.result = Result()
        self.predict = None
        ReadFile(file_name, self.data)

    @staticmethod
    def show_available_learners():
        return ", ".join([k for k in LEARNERS])

    def run(self, learners=[k for k in LEARNERS], round_results=3):
        for learner_name in learners:
            learner = LEARNERS[learner_name](self.data, self.result,
                                             self.folds, self.splits)
            self.predict = learner.execute()
            for prediction in self.predict:
                def generate_stats(predict):
                    abcd = ABCD(before=self.data.get_test_label(), after=predict)
                    stats = np.array([j.stats() for j in abcd()])
                    labels = list(set(self.data.get_test_label()))
                    if labels[0] == 0:
                        target_label = 0
                    else:
                        target_label = 1
                    r_val = stats[target_label][0]
                    p_val = stats[target_label][3]
                    a_val = stats[target_label][4]
                    f_score_val = stats[target_label][5]
                    return r_val, p_val, a_val, f_score_val

                recall, precision, accuracy, f_score = generate_stats(prediction)
                self.result.set_recall(learner_name, round(recall, round_results))
                self.result.set_precision(learner_name, round(precision, round_results))
                self.result.set_accuracy(learner_name, round(accuracy, round_results))
                self.result.set_f_score(learner_name, round(f_score, round_results))

    def get_recall(self):
        return self.result.get_recall()

    def get_precision(self):
        return self.result.get_precision()

    def get_accuracy(self):
        return self.result.get_accuracy()

    def get_f_score(self):
        return self.result.get_f_score()

    def display_stats(self):
        for k, v in self.result.scores.items():
            print(k)
            rdivDemo(v())
            print("")