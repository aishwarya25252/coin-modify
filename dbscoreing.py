import pandas as pd
import numpy as np
from sklearn.metrics import davies_bouldin_score
def dbscoreing(metacluster,clustermap):
    finalindex=set(clustermap[0].parent.newdata.index)
    totallabel=0
    n=len(clustermap)
    for i in range(n):
        finalindex.intersection_update(set(clustermap[i].parent.newdata.index))
        totallabel=totallabel+len(clustermap[i].labels)
    finalindex=list(finalindex)
    matrix=np.zeros([totallabel,len(finalindex)])
    labelmatrix=np.zeros(totallabel)
    t=0
    for i in range(len(metacluster)):
        for j in list(metacluster[i]):
            d=clustermap[j].parent.newdata
            for k in range(len(clustermap[j].labels)):
                for l in range(len(finalindex)):
                    matrix[t][l]=d[clustermap[j].labels[k]][finalindex[l]]
                    labelmatrix[t]=i
                t=t+1
    index=davies_bouldin_score(matrix,labelmatrix)
    return index , matrix , labelmatrix