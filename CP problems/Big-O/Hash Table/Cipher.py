import sys

n,k = [int(x) for x in sys.stdin.readline().split()]

s = input()
c = 0
b = []
for i in range(0,n):
    if i >= k:
        c ^= b[i-k]
    b.append(c ^ int(s[i]))
    c ^= b[-1]
for i in b:
    print(i, end="")