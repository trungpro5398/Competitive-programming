import sys

sys.setrecursionlimit(10 ** 6)
from sys import stdin

n = int(input())
a = [int(x) for x in stdin.readline().split()]


def div(left, right, height):
    if right <= left:
        return 0
    sav = left
    k = min(a[left:right])
    for i in range(left, right):
        if a[i] == k:
            sav = i
            break
    left_min = div(left, sav, a[sav])
    right_min = div(sav + 1, right, a[sav])
    return min(right - left , left_min + right_min + a[sav] - height)


ans = div(0, n , 0)
print(ans)