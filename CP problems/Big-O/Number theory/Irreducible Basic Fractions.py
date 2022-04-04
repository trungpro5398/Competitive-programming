import copy
import math

def primeFactor(s):
    res = copy.deepcopy(s)
    n = copy.deepcopy(s)
    for i in range(2, int(math.sqrt(n)) + 1,1):
        if n % i == 0:
            while n % i == 0:
                n /= i
            res //= i
            res *= (i-1)

    if s != 1 and n !=1 :
        res //= n
        res *= (n-1)
    return res
while True:
    s = int(input())
    if s == 0:
        break
    print(int(primeFactor(s)))