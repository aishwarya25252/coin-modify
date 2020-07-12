import numpy as np
class dat :
    def __init__(self,data,newdata,k):
        self.data=data
        self.newdata=newdata
        self.k=k
        self.clusters={}
        for i in range(k):
            self.clusters[i]=clus(self)
        pass

class clus :
    def __init__(self,parent):
        self.parent=parent
        self.labels=[]
        self.index=None
        pass
    def centroid(self,genes):
        d=self.parent.data
        i=list(set(genes)&set(d.index))
        d=d.loc[i,self.labels]
        m=d.to_numpy()
        if d.empty==True:
            return np.zeros(m.shape[0])
        return m.mean(axis=1)