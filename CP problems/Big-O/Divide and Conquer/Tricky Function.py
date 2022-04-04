from sys import stdin
import math

INF = 1e9


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def dis(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return (x * x + y * y)


def bruteForce(points, left, right):
    min_dist = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_dist = min(min_dist, dis(points[i], points[j]))
    return min_dist


def stripCloset(point_set, left, right, mid, dist_min):
    point_mid = point_set[mid]
    splitted_points = []
    for i in range(left, right):
        if abs(point_set[i].x - point_mid.x) <= dist_min:
            splitted_points.append(point_set[i])
    splitted_points.sort(key=lambda p: p.y)
    smallest = dist_min
    l = len(splitted_points)
    for i in range(l):
        for j in range(i + 1, l):
            if not dis(splitted_points[i], splitted_points[j]) < smallest:
                break
            d = dis(splitted_points[i], splitted_points[j])
            smallest = min(d, smallest)
    return smallest


def minimalDistance(point_set, left, right):
    if right - left <= 3:
        return bruteForce(point_set, left, right)
    mid = (left + right) // 2
    dist_left = minimalDistance(point_set, left, mid)
    dist_right = minimalDistance(point_set, mid + 1, right)
    dist_min = min(dist_left, dist_right)
    return min(dist_min, stripCloset(point_set, left, right, mid, dist_min))


n = int(input())
a = [int(x) for x in stdin.readline().split()]

g = [0] * n
g[0] = a[0]
for i in range(1, n):
    g[i] = a[i] + g[i - 1]
point_set = []
for i in range(0, n):
    point_set.append(Point(i, g[i]))

ans = (minimalDistance(point_set, 0, n))
print(ans)