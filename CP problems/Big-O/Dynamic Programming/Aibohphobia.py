import copy

s = input()
s = list(s)
s1 = copy.deepcopy(s)
s1.reverse()

dp = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]

for i in range(len(s)+1):
    for j in range(len(s)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif s[i - 1] == s1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(len(s) - dp[-1][-1])