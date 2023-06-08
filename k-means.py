from ctypes import sizeof
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def predict_classification(data, var1, var2,k):
    centroids = data[:k]
    distances = []

    for centroid in centroids:
        distance = euclidean_distance(var1, var2, centroid[0], centroid[1])
        distances.append(distance)

    nearest_cluster_index = distances.index(min(distances))
    predicted_classification = data[nearest_cluster_index][2]

    return predicted_classification

data = [
    (1.713, 1.586, 0),
    (0.180, 1.786, 1),
    (0.353, 1.240, 1),
    (0.940, 1.566, 0),
    (1.486, 0.759, 1),
    (1.266, 1.106, 0),
    (1.540, 0.419, 1),
    (0.459, 1.799, 1),
    (0.773, 0.186, 1)
]

var1 = 0.906
var2 = 0.606
k=3
predicted_classification = predict_classification(data, var1, var2,k)
print(f"The predicted classification for VAR1={var1} and VAR2={var2} is: {predicted_classification}")


# output:
#   The predicted classification for VAR1=0.906 and VAR2=0.606 is: 1
