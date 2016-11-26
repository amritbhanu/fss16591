from fault_prediction.LearnerExecutor import LearnerExecutor
import sys

sys.dont_write_bytecode = True

learner = LearnerExecutor('./data/ant.csv')
learner.run()
learner.display_stats()


