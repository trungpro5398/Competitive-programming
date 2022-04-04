
def B():
    N, X = map(int, input().split())
    a = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(0, len(a)):
        if i % 2 == 1:
            even.append(a[i])
        else:
            odd.append(a[i])
    for i in odd:
        X -= i

    if X < 0:
        print("No")
    else:
        for i in even:
            X -= (i - 1)
        if X < 0:
            print("No")
        else:
            print("Yes")
import sys
def C():
    N = int(sys.stdin.buffer.readline())
    a = list(map(int, sys.stdin.buffer.readline().split()))
    a.sort()
    res = 1
    for i in range(0, len(a)):
        res *= (a[i] - i)
        res %=  ( pow(10,9) + 7 )

    print(res % ( pow(10,9) + 7 ))
C()