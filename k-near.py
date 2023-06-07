def classify(points, p, k):
    distance = []
    for g in points:
        for xy in points[g]:
            eucdis = ((xy[0] - p[0]) ** 2 + (xy[1] - p[1]) ** 2) ** 0.5
            distance.append((eucdis, g))
    distance = sorted(distance)[:k]
    f1, f2 = 0, 0
    for d in distance:
        if d[1] == 0:
            f1 += 1
        elif d[1] == 1:
            f2 += 1
    return 0 if f1 > f2 else 1

points = {1: [(1, 1), (2, 2), (3, 1)], 0: [(5, 3), (4, 4), (6, 5)]}
p = (1, 2)
k = 3
ans = classify(points, p, k)
print(f"The value classified to unknown pointer is: {ans}")
