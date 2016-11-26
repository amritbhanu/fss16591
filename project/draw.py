__author__ = 'amrit'

import matplotlib.pyplot as plt
import os, pickle
import operator
import numpy as np
import matplotlib.cm as cmx
import matplotlib.colors as colors

if __name__ == '__main__':

    fileB = ["ant", "arc", "camel", "ivy", "jedit", "log4j", "poi", "prop", "redaktor", "synapse", "tomcat", "velocity",
             "xalan", "xerces"]
    F_final1 = {}
    current_dic1 = {}
    para_dict1 = {}
    time1 = {}
    path = '/Users/amrit/GITHUB/fss16591/project/fault_prediction/dump/smote/'
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            a = os.path.join(root, name)
            with open(a, 'rb') as handle:
                F_final = pickle.load(handle)
                F_final1 = dict(F_final1.items() + F_final.items())
    #print(F_final1)

    font = {
        'size': 60}

    plt.rc('font', **font)
    paras = {'lines.linewidth': 10, 'legend.fontsize': 35, 'axes.labelsize': 60, 'legend.frameon': False,
             'figure.autolayout': True}
    plt.rcParams.update(paras)
    X = range(len(fileB))
    measure_med = {}
    measure_iqr = {}
    l = ["Recall", "Precision", "Accuracy", "F_score"]
    for i in l:
        measure_med[i] = {}
        measure_iqr[i] = {}
    for f, measures in F_final1.iteritems():
        for mea, values in measures.iteritems():
            for k in values:
                try:
                    measure_med[mea][k[0]].append(np.median(k[1:]))
                    measure_iqr[mea][k[0]].append(np.percentile(k[1:], 75) - np.percentile(k[1:], 25))
                except KeyError:
                    measure_med[mea][k[0]] = [np.median(k[1:])]
                    measure_iqr[mea][k[0]] = [np.percentile(k[1:], 75) - np.percentile(k[1:], 25)]

    for i,j in enumerate(measure_iqr.keys()):
        plt.figure(num=i, figsize=(25, 15))
        for k in measure_iqr[j].keys():
            line,=plt.plot(X, measure_med[j][k],marker='*', markersize=20, label=k+' median')
            plt.plot(X, measure_iqr[j][k],linestyle="-.", markersize=20,color=line.get_color(),label=k+' iqr')
            #plt.ytext(0.04, 0.5, va='center', rotation='vertical', fontsize=11)
            #plt.text(0.04, 0.5,"Rn (Raw Score)", labelpad=100)
        plt.ylim(0.0, 1.0)
        plt.xticks(X, fileB,rotation=90)
        plt.ylabel(j, labelpad=30)
        plt.xlabel("No of Datasets", labelpad=30)
        plt.legend(bbox_to_anchor=(1.00, 1.13), loc=1, ncol=4, borderaxespad=0.1)
        plt.savefig(j+"_smote.png")
