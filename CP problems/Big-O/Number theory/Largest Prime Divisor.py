import copy
import math

def primeFactor(n):
    s = copy.deepcopy(n)
    res = []
    for i in range(2, int(math.sqrt(n)) + 1,1):
        if n % i == 0:
            while n % i == 0:
                n /= i
                res.append(i)
    return res
    if n !=1 :
        res.append(n)
    if len(res) < 2:
        return -1
    return res[-1]
while True:
    n =int(input())
    if n == 0:
        break
    print((primeFactor(n)))