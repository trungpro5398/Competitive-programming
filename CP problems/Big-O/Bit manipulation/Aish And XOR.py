from sys import stdin

n = int(stdin.readline())
a =  [int(x) for x in stdin.readline().split()]
q = int(stdin.readline())
dp = [0] * n
dp_bit = [0] * n
for i in range(0, n):
    if i == 0:
        dp[i] = a[i] ^ 1
        dp_bit[i] = a[i]
    else:
        dp[i] += dp[i-1]
        dp[i] += a[i] ^ 1
        dp_bit[i] ^= dp_bit[i-1] ^ a[i]

for i in range(q):
    l, r = [int(x) for x in stdin.readline().split()]
    l -= 1
    r -= 1




    if l == 0:
        print(dp_bit[r], end=" ")
        print(dp[r])
    else:
        print(dp_bit[r] ^ dp_bit[l-1], end=" ")
        print(dp[r] - dp[l-1])

