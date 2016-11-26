from fault_prediction import Learner
import sys
import os

sys.dont_write_bytecode = True

print os.getcwd()
learner = Learner('./data/ant.csv')
learner.run()
learner.display_stats()


