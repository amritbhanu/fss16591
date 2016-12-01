from fault_prediction import Learner
import sys
import os
import pickle

sys.dont_write_bytecode = True

files=['synapse', 'xerces', 'camel', 'prop', 'ant', 'arc', 'poi', 'ivy', 'velocity', 'redaktor', 'log4j', 'jedit']
other=['tomcat', 'xalan']

for f in files:
    file=f
    learner = Learner('./data/'+file+'.csv')
    learner.run()
    result={}
    x={}
    x["Accuracy"]=learner.get_accuracy()
    x["F_score"]=learner.get_f_score()
    x["Precision"]=learner.get_precision()
    x["Recall"]=learner.get_recall()
    x["False_alarm"]=learner.get_false_alarm()
    result[file]=x
    print result
    with open('./dump/smote/'+file + '.pickle', 'wb') as handle:
        pickle.dump(result, handle)

