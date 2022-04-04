dp = [[0 for i in range(1006)] for j in range(1006)]
c = [[0 for i in range(1006)] for j in range(1006)]
while True:
     n = int(input())
     if n == 0:
         break
     a = input()
     a = "0" + a
     b = input()
     b = "0" + b

     if len(b) == 1:
         break
     ans = 0
     for i in range(1, len(a)):
         for j in range(1, len(b)):
             if a[i] == b[j]:
                 c[i][j] = c[i - 1][j - 1] + 1
             else:
                 c[i][j] = 0
             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
             for e in range(n, c[i][j]+1):
                 dp[i][j] = max(dp[i][j], dp[i-e][j-e] + e)

     ans = max(dp[len(a)-1][len(b)-1], ans)
     print(ans)