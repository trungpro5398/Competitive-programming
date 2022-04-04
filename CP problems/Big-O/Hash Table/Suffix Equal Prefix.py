
import sys

# Quang Trung Nguyen ID:30936179
def get_z_value(pattern, Z):

    n = len(pattern)
    k, l, r = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and pattern[r-l] == pattern[r]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < n and pattern[r-l] == pattern[r]:
                    r += 1
                Z[i] = r - l
                r -= 1

def Z_al():
    t = int(input())
    for j in range(1, t + 1):
        s = input()
        Z = [0] * len(s)
        cnt = 0
        get_z_value(s, Z)
        for i in range(1, len(Z)):
            if Z[i] + i == len(Z):
                cnt += 1
        print("Case {}: {}".format(j, cnt))


#pre Compute Pow
Pow = [0] * 1000005

base = 33
Pow[0] = 1

mod = 10**9+7
for i in range(1, 1000005):
    Pow[i] =(Pow[i-1]*base) % mod

def get_hashS(l, r):
    if l <= 0:
        return hashS[r]

    return (hashS[r] - hashS[l-1] * Pow[r-l+1] + mod * mod)% mod

t = int(input())
for j in range(1, t + 1):
    s = input()

    n = len(s)
    hashS = [0] * n
    hashS[0] = ord(s[0]) - ord('a') + 1
    for i in range(1,n):
        hashS[i] = (hashS[i-1] * base + ord(s[i]) - ord('a') + 1 ) % mod

    cnt = 0
    for i in range(0, n-1):
        if hashS[i] == get_hashS(n-1-i, n-1):
            cnt += 1
    print("Case {}: {}".format(j, cnt))



