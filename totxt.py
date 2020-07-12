def totxt(clustermatrix,weightmatrix,name):
    f = open(name, "w")
    n=clustermatrix.shape[0]
    for i in range(n):
        for j in range(n):
            if clustermatrix[i][j]==1 :
                f.write(str(i)+","+str(j)+","+str(weightmatrix[i][j])+"\n")
    f.close()
    return
