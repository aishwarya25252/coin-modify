class GeneSet:
    def __init__(self, dataSets, g, n ,pd):
        self.pd=pd
        self.dataSets = self.preprocess(dataSets)
        self.finalGeneSet = self.calculate(self.dataSets, g, n)

    def preprocess(self, dataSets):
        for i in range(len(dataSets)):
            dataSets[i] = self.process(dataSets[i])
        return dataSets

    def process(self, dataFrame):
        dataFrame = dataFrame.T
        dataFrame.columns = dataFrame.iloc[0]
        dataFrame = dataFrame.drop("ID_REF")
        dataFrame[:] = dataFrame[:].astype(float)
        return dataFrame

    def calculate(self, dataSets, g, n):
        Ggene = set()#self.Ggene(dataSets, g) changed temporary
        for i in range(len(dataSets)):
            Ggene = Ggene.union(self.Ngene(dataSets[i], n))
        return Ggene

    def Ngene(self, dataFrame, n):
        ngene = set(dataFrame.mad().sort_values(ascending=False)[:n].index)
        return ngene

    def Ggene(self, dataSets, g):
        initialSet = set()
        for i in dataSets:
            initialSet=initialSet.union(set(i.index))
        initialSet = list(initialSet)
        data = self.pd.DataFrame(index=initialSet)
        for i in range(len(dataSets)):
            temp = []
            for j in range(len(initialSet)):
                temp.append(self.collectRank(dataSets[i], initialSet[j]))
            data[i] = temp
        finalSet = list(data.median(axis=1).sort_values().index)
        finalSet = set(finalSet[:g])
        return finalSet

    def collectRank(self, dataFrame, label):
        try :
            l = list(dataFrame.mad().sort_values(ascending=False)[:].index)
            rank=l.index(label)
        except ValueError :
            rank=100
        return rank


