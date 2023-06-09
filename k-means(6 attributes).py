from ctypes import sizeof
import math

def euclidean_distance(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    return math.sqrt((x1 - x2) * 2 + (y1 - y2) * 2 + (x3 - y3) * 2 + (x4 - y4) * 2 + (x5 - y5) * 2 + (x6 - y6) * 2)

def predict_classification(data, var1, var2, var3, var4, var5, var6, k):
    centroids = data[:k]
    distances = []

    for centroid in centroids:
        distance = euclidean_distance(var1, var2, centroid[0], centroid[1], var3, var4, centroid[2], centroid[3], var5, var6, centroid[4], centroid[5])
        distances.append(distance)

    nearest_cluster_index = distances.index(min(distances))
    predicted_classification = data[nearest_cluster_index][6]

    return predicted_classification

data = [
    (1.713, 1.586, 0.123, 0.456, 0.789, 1.234, 0),
    (0.180, 1.786, 0.345, 0.678, 0.912, 1.345, 1),
    (0.353, 1.240, 0.567, 0.890, 0.123, 1.678, 1),
    (0.940, 1.566, 0.789, 0.123, 0.456, 1.901, 0),
    (1.486, 0.759, 0.912, 0.345, 0.678, 0.234, 1),
    (1.266, 1.106, 0.123, 0.567, 0.890, 0.567, 0),
    (1.540, 0.419, 0.345, 0.789, 0.123, 0.890, 1),
    (0.459, 1.799, 0.567, 0.912, 0.345, 0.123, 1),
    (0.773, 0.186, 0.789, 0.234, 0.567, 0.456, 1)
]

var1 = 0.906
var2 = 0.606
var3 = 0.123
var4 = 0.345
var5 = 0.678
var6 = 0.890
k = 3

predicted_classification = predict_classification(data, var1, var2, var3, var4, var5, var6, k)
print(f"The predicted classification for VAR1={var1}, VAR2={var2}, VAR3={var3}, VAR4={var4}, VAR5={var5}, VAR6={var6} is: {predicted_classification}")

# Output:
# The predicted classification for VAR1=0.906, VAR2=0.606, VAR3=0.123, VAR4=0.345, VAR5=0.678, VAR6=0.89 is: 1
