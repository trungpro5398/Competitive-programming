import copy
from sys import stdin

a = [int(x) for x in stdin.readline().split()]

p, q, r = a[0], a[1], a[2]
a = p + q
ans = 1
for i in range(r+1):
    ans *= a
    a -= 1
a = p + q
ans1 = 1
q1 = copy.deepcopy(q)
for i in range(r+1):
    if a + q1 >= p + q:
        a1 = copy.deepcopy(a)
        ans1 *= p + q1
        q1 = a1 - p
    else:
        ans1 *= a
    a -= 1

print( ans/ans1)

