from __future__ import print_function, division
from Table import Table
from random import random,shuffle,randint,seed
import time
import sys
import numpy as np
import pandas as pd
from sklearn.cluster import MiniBatchKMeans
from sklearn.neighbors import KDTree
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sk import rdivDemo
from ABCD import ABCD


sys.dont_write_bytecode = True

def train_test(corpus, folds=5, index=0):
    i_major = []
    i_minor = []
    l = len(corpus)
    corpus=pd.DataFrame({"A":corpus})
    for i in range(0, folds):
        if i == index:
            i_minor.extend(range(int(i * l / folds), int((i + 1) * l / folds)))
        else:
            i_major.extend(range(int(i * l / folds), int((i + 1) * l / folds)))
    return list(corpus.iloc[i_major,].values.flatten()), list(corpus.iloc[i_minor,].values.flatten())

if __name__ == '__main__':
    datasets=['diabetes.csv','camel-1.0.csv','arc.csv','ivy-2.0.csv','jedit-3.2.csv']
    folds=5
    seed(1)
    rec_dic={}
    fa_dic={}
    runtime={}
    trees=['width','interval','NB']
    for k in datasets:
        rec_dic[k]={}
        fa_dic[k] = {}
        runtime[k]={}
        for x in trees:
            rec_dic[k][x]=[]
            fa_dic[k][x] = []
            runtime[k][x] = 0
        print("### Dataset: "+k+ " ###\n")
        csvFile = '../4/data/'+k
        table = Table(csvFile)
        for i in xrange(folds):
            shuffle(table.rows)
            for index in xrange(folds):
                train,test=train_test(table.rows, folds=folds, index=index)
                data_train=[]
                data_test = []
                train_label = []
                test_label = []
                for x in train:
                    train_label.append(x[-1])
                    data_train.append(x[:-1])
                for x in test:
                    test_label.append(x[-1])
                    data_test.append(x[:-1])

                start_time = time.time()
                kmeans = MiniBatchKMeans(init='random',n_clusters=20, n_init=20,batch_size=20,compute_labels=True)
                kmeans.fit(data_train,train_label)
                k_means_cluster_centers = np.sort(kmeans.cluster_centers_, axis=0)
                k_means_labels = pairwise_distances_argmin(data_train, k_means_cluster_centers)
                predict=kmeans.predict(data_test)
                prediction=[]
                for y in predict:
                    prediction.append(train_label[y])
                abcd = ABCD(before=test_label, after=prediction)
                # recall for 1st target class
                #print(np.array([j.stats()[0] for j in abcd()]))
                rec_dic[k]['width'].append(np.array([j.stats()[0] for j in abcd()])[0])
                # false alarm for 1st target class
                fa_dic[k]['width'].append(([j.stats()[1] for j in abcd()])[0])
                runtime[k]['width'] += time.time() - start_time


                start_time = time.time()
                tree = KDTree(data_train, metric='euclidean')
                _, ind=tree.query(data_test,k=1)
                #print(ind)
                predict=[item for sublist in ind for item in sublist]

                for y in predict:
                    prediction.append(train_label[y])
                abcd = ABCD(before=test_label, after=prediction)
                # recall for 1st target class

                rec_dic[k]['NB'].append(np.array([j.stats()[0] for j in abcd()])[0])
                # false alarm for 1st target class
                fa_dic[k]['NB'].append(([j.stats()[1] for j in abcd()])[0])
                runtime[k]['NB'] += time.time() - start_time

                start_time = time.time()
                NB = GaussianNB()
                NB.fit(data_train,train_label)
                predict=NB.predict(data_test)

                abcd = ABCD(before=test_label, after=predict)
                # recall for 1st target class
                rec_dic[k]['interval'].append(np.array([j.stats()[0] for j in abcd()])[0])
                # false alarm for 1st target class
                fa_dic[k]['interval'].append(([j.stats()[1] for j in abcd()])[0])
                runtime[k]['interval'] += time.time() - start_time
    #print(rec_dic)
    #print(fa_dic)
    #print(runtime)

    ## scottknot code taken from Dr Menzies
    for feature in datasets:
        tmp = []
        temp1=[]
        print(feature)
        for is_shingle in trees:
                tmp.append([is_shingle] + rec_dic[feature][is_shingle])
                temp1.append([is_shingle] + fa_dic[feature][is_shingle])
        print("Recall")
        print(rdivDemo(tmp))
        print("False Alarm")
        print(rdivDemo(temp1))
        print("\n")
