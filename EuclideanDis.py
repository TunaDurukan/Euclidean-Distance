import math

def euclideanDistance(point1, point2):
    x1, x2 = point1[0], point1[1]
    y1, y2 = point2[0], point2[1]
    euclideanDis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return euclideanDis


points = [(1,3), (5,6), (4,9), (3,7), (1,5)]

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

minMesafe = min(distances)
print("Minimum mesafe:", minMesafe)
