from fault_prediction import Learner
import sys

sys.dont_write_bytecode = True

learner = Learner('./data/ant.csv')
learner.run()
learner.display_stats()


