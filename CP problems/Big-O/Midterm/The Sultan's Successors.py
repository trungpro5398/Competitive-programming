from sys import stdin

t = int(input())

matrix = [[0 for _ in range(8)] for _ in range(8)]
b = [0] * 16
c = [0] * 16
col = [0] * 8
def dfs(n):
    global sum, ans

    if n == 8 :
        ans = max(ans,sum)
        return

    for i in range(8):

        if not col[i] and not b[n - i + 1] and not c[n+i]:
            col[i] = 1
            b[n - i + 1] = 1
            c[n+i] = 1
            sum += matrix[n][i]
            dfs(n+1)
            col[i] = 0
            b[n - i + 1] = 0
            c[n + i] = 0
            sum -= matrix[n][i]
while t:
    t -= 1
    for i in range(8):
        a = [int(x) for x in stdin.readline().split()]
        for j in range(8):
            matrix[i][j] = a[j]
    ans = - 1
    sum = 0
    dfs(0)
    print(ans)
