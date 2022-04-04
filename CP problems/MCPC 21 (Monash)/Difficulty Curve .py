import copy
from sys import stdin

t = int(input())

while t:
    t -= 1
    n,k = [int(x) for x in stdin.readline().split()]
    d = [int(x) for x in stdin.readline().split()]
    d.sort()
    
    while k:
        for j in range(len(d)-1,-1,-1):
            d.append((d[j] + d[j-1]) // 2)
            k -= 1
            break
        d.sort()
    res = 10 ** 9
    for i in range(0, len(d)-1):
        res = min(res,abs(d[i]-d[i+1]))
    print(res)


import copy
from sys import stdin

t = int(input())

while t:
    t -= 1
    n,k = [int(x) for x in stdin.readline().split()]
    d = [int(x) for x in stdin.readline().split()]
    d.sort()

    while k:
        for j in range(len(d)-1,-1,-1):
            d.append((d[j] + d[j-1]) // 2)
            k -= 1
            break
        d.sort()
    res = 10 ** 9
    for i in range(0, len(d)-1):
        res = min(res,abs(d[i]-d[i+1]))
    print(res)


