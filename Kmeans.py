import numpy as np
def distance(x, y):
    return (((x - y) ** 2).sum()) ** 0.5


def cencal(data, centroids, assignedCluster, live):
    templive = None
    for i in live:
        count = 0
        total = np.zeros(centroids.shape[1])
        previousValue = centroids[i]
        for j, v in assignedCluster.items():
            if v == i:
                total = total + data[j]
                count = count + 1
        if count == 0:
            count = 1
        newValue = total / count
        if (newValue != 0).all() | (newValue != previousValue).all():  # problem...
            templive = [l for l in live if l != i]
            centroids[i] = newValue
    return centroids, templive


def sse(data, assignedCluster, centroid, index):
    sums = np.zeros(centroid.shape)
    count = 1
    for i, v in assignedCluster.items():
        if v == index:
            sums = sums + (data[i] - centroid) ** 2
            count = count + 1
    return (count * sums.sum() * 1.0) / (count)


def kmeans(data, centroids):
    data=data.copy()
    centroids=centroids.copy()
    cases = data.shape[0]
    cases = cases - 1
    k = centroids.shape[0] - 1
    live = [i for i in range(k + 1)]
    assignedCluster = {}
    for i in range(cases + 1):
        smallDist = distance(data[i], centroids[0])
        cluster = 0
        for j in range(k + 1):
            dist = distance(data[i], centroids[j])
            if dist < smallDist:
                cluster = j
                smallDist = dist
        assignedCluster[i] = cluster
    centroids = cencal(data, centroids, assignedCluster, live)[0]
    assignedClusterTemp = assignedCluster.copy()
    while True:
        if(live==None):
            break
        for i in live:
            sse1 = sse(data, assignedCluster, centroids[i], i)
            clusterTemp = i
            for j in [l for l, v in assignedCluster.items() if v == j]:
                for k in live:
                    if k != i:
                        temp = assignedCluster.copy()
                        temp[j] = k
                        sse2 = sse(data, temp, centroids[k], k)
                        if sse2 < sse1:
                            sse1 = sse2
                            clusterTemp = k
                assignedClusterTemp[j] = clusterTemp
        assignedCluster = assignedClusterTemp.copy()
        centroids, live = cencal(data, centroids, assignedCluster, live)
    return assignedCluster, centroids
