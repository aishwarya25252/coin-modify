from sklearn.cluster import KMeans
def kmeans(data, centroids):
    cases = data.shape[0]
    k = centroids.shape[0]
    kmean = KMeans(n_clusters=k, random_state=0).fit(data)
    assignedCluster={}
    for i in range(cases):
        assignedCluster[i]=kmean.labels_[i]
    centroids=kmean.cluster_centers_
    return assignedCluster, centroids