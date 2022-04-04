from sys import stdin

k1 = int(input())
t = 1
p = 1000000007
# while k1:
#     k1 -= 1
#     n, k = [int(x) for x in stdin.readline().split()]
#     dp = [ [0 for _ in range(k+1)]  for _ in range(n+1)]
#     dp[1][1] = 1
#     for i in range(2, k+1):
#         dp[1][i] += dp[1][i-1] + 1
#     for i in range(2, n+1):
#         for j in range(1, k+1):
#             if j == 1:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] += dp[i-1][j] + dp[i][j-1]
#                 dp[i][j] %= p
#
#     print("Case {}: {}".format(t, dp[n][k] % p))
#     t += 1
maxx = 20000001
mod = 1000000007
fact = [0] * maxx

def init():
    fact[0] = 1
    for i in range(1, maxx):
        fact[i] = (i * fact[i - 1]) % mod

def modularExponentiation(a, b):
    res = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % mod
        b //= 2
        a = (a * a) % mod
    return res

def modInverse(b):
    return modularExponentiation(b, mod - 2)

def getC(n, k):
    nu = fact[n+k-1]
    de = fact[n] * fact[k-1] % mod
    return nu * modInverse(de) % mod
def modPow(a, b):
    r = 1
    while b:
        if b & 1:
            r = ( r * a) % p
        a = ( a * a ) % p
        b >>= 1
    return r

fact = [0 for _ in range(2000009)]
fact[0] = 1
for i in range(1, 2000002):
    fact[i] = ( fact[i-1] % p * i) % p
while k1:
    k1 -= 1
    n, k = [int(x) for x in stdin.readline().split()]
    ans = fact[n+k-1]
    div = (fact[n] * fact[k-1]) % p
    ans = ( ans * modPow(div, p-2)) % p
    print("Case {}: {}".format(t, ans))
    t += 1