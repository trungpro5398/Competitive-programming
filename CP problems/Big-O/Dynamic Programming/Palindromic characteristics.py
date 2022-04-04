s = input()
n = len(s)
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
count = [0 for i in range(n + 1)]

for i in range(1,n+1):
    for j in range(0,n-i+1):
        r = j + i - 1
        if i == 1:
            dp[j][r] = 1
        elif i == 2:
            if s[j] == s[r]:
                dp[j][r] = 2
        else:
            if s[j] == s[r] and dp[j+1][r-1] > 0:
                dp[j][r] = dp[j][j+i//2-1] + 1
        count[dp[j][r]] += 1
for i in range(n - 1, 0, -1):
    count[i] += count[i + 1]

for i in range(1, n + 1):
    print(count[i], end=' ')

print()