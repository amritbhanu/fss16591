from __future__ import print_function, division

__author__ = 'amrit'
import sys

def readarff(file=''):
    yes=0
    no=0
    l=[]
    with open(file,'r') as f:
        for doc in f.readlines():
            if doc.startswith('@') or doc.startswith('\n'):
                continue
            else:
                values=doc.strip().split(',')
                if values[-1]=='yes' or values[-1]=='true':
                    yes+=1
                    l.append('1:yes')
                else:
                    no+=1
                    l.append('2:no')
    if yes>no:
        return "1:yes",l
    else:
        return "2:no",l
def predict(value='',l=[]):
    print("=== Predictions on test data ===\n")
    print("inst#\tactual\tpredicted\terror prediction")
    for i in range(1,len(l)+1):
        waste=1
        if l[i-1]!=value:
            waste=0
        print('   '+str(i)+'\t '+l[i-1]+'\t   '+value+'\t\t'+str(waste))


if __name__ == '__main__':
    #training
    value, waste =readarff(sys.argv[1])
    #testing
    waste, l=readarff(sys.argv[2])
    predict(value, l)