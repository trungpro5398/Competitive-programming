import copy
import math
from sys import stdin

t = int(input())

while t:
    t -= 1
    a, b = [int(x) for x in stdin.readline().split()]
    c = max(a,b) * max(a,b) - min(a,b) * min(a,b)
    d = copy.deepcopy(c)
    d =int( math.sqrt(d))
    e = max(a,b) * max(a,b) + min(a,b) * min(a,b)
    f = copy.deepcopy(e)
    f =int( math.sqrt(f))
    if d * d == c:
        print(int(d))
    elif f * f == e:
        print(int(f))
    else:
        print(-1)