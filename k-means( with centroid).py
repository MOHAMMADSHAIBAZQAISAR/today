import numpy as np

X=[[1.713,1.586],[0.180,1.786],[0.353,1.240],[0.940,1.566],[1.486,0.759],[1.266,1.106],[1.540,0.419],[0.459,1.799],[0.773,0.186]]

target=[0,1,1,0,1,0,1,1,1]

k = 3
clusters = []
centroids= []

for i in range(k):
    clusters.append([X[i]])
for i in range(k):
    centroids.append([X[i]])
print(clusters)

def calculate_clusters(point, centroids, k,clusters):
    dist = []
    for data in centroids:
        dist.append(np.linalg.norm(np.array(data) - np.array(point)))
    index=dist.index(min(dist))
    clusters[index].append(point)
    centroids=calculate_centroids(centroids, clusters, k)
    return clusters,centroids

def calculate_centroids(centroids, clusters, k):
    for i in range(k):
        centroids[i] = np.average(clusters[i], axis=0)
    return centroids

def func(centroids,test):
    mindist=99999
    i=-1
    ans=0
    for point in centroids:
        i+=1
        dist=np.linalg.norm(point - test)
        print(dist)
        if mindist>dist:
            mindist=dist
            ans=i
    return ans

for i in range(3,len(X)):
    clusters,centroids=calculate_clusters(X[i], centroids, k,clusters)
    print(clusters)
    print(centroids)
    print()

test_data=np.array([0.906,0.606])
c=func(centroids,test_data)
print("cluster: ",c)
a,b=0,0
for point in clusters[c]:
    for i in range(len(X)):
        if np.array_equal(point,X[i]):
            if target[i]==0:
                a+=1
            else:
                b+=1
            break
print("class label : ",0 if a>b else 1)
