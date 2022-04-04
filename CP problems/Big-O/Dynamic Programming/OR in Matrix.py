from sys import stdin

h, w = [int(x) for x in stdin.readline().split()]

mat = [[0 for i in range(w)] for j in range(h)]

for i in range(h):
    a = [int(x) for x in stdin.readline().split()]
    for j in range(w):
        mat[i][j] = a[j]
dp = [[1 for i in range(w)] for j in range(h)]

for i in range(h):
    for j in range(w):
        if mat[i][j] == 0:
            for k in range(w):
                dp[i][k] = 0
            for k in range(h):
                dp[k][j] = 0
dp1 = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        for k in range(w):
            if dp[i][k] == 1:
                dp1[i][j] = 1
        for k in range(h):
            if dp[k][j] == 1:
                dp1[i][j] = 1

if mat != dp1:
    print("NO")
else:
    print("YES")
    for i in range(h):
        for j in range(w):
            print(dp[i][j], end= " ")
        print()
