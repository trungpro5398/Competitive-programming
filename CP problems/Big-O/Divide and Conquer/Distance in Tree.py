# from sys import stdin
#
# n, k = [int(x) for x in stdin.readline().split()]
#
# graph = [[] for _ in range(n+1)]
# dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# for i in range(n-1):
#     a, b = [int(x) for x in stdin.readline().split()]
#     graph[a].append(b)
#     graph[b].append(a)
#
# ans = 0
# # Function to find the number of distinct
# # pairs of the vertices which have a distance
# # of exactly k in a tree
# def dfs(v, pair):
#     global ans
#
#     dp[v][0] = 1
#
#     for i in graph[v]:
#         if i != pair:
#             dfs(i, v)
#             # Count the pair of vertices at
#             # distance k
#             for j in range(1, k+1):
#                 ans += dp[i][j-1] * dp[v][k-j]
#
#             # For all levels count vertices
#             for j in range(1, k + 1):
#                 dp[v][j] += dp[i][j - 1]
#
# dfs(1,0)
#
# print(ans)
import sys

sys.setrecursionlimit(1000000)


def get(graph, u, par):
    count = {0: 1}
    res = 0
    for v in graph[u]:
        if v != par:
            res_v, count_v = get(graph, v, u)
            res += res_v

            count_v[-1] = 0

            for key, val in count_v.items():
                res += val * count.get(k - 1 - key, 0)

            for key, val in count_v.items():
                count[key + 1] = count.get(key + 1, 0) + val

    return res, count


n, k = map(int, input().split())

graph = [[] for i in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

print(get(graph, 0, -1)[0])