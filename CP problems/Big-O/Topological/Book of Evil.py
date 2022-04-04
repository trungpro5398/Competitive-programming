import heapq


def bfs(graph, start):
    n = len(graph)
    dist = [-1 for i in range(n+1)]
    visited = [False for i in range(n+1)]
    visited[start] = True
    stack = []
    dist[start] = 0
    heapq.heappush(stack, start)

    while stack:

        u = heapq.heappop(stack)

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                heapq.heappush(stack, v)

    return dist

n, m, d = map(int, input().split())



p = list(map(int, input().strip().split()))

graph = [[] for i in range(n+1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)



dist = bfs(graph, 1)

max_distance = -1
u = -1
v = -1
for i in p:
    if dist[i] > max_distance:
        max_distance = dist[i]
        u = i
dist = [-1] * n

distu = bfs(graph, u)

max_distance = -1
for i in p:
    if distu[i] > max_distance:
        max_distance = distu[i]
        v = i

distv = bfs(graph, v)

cnt = 0

for i in range(1, n+1):
    if 0 <= distu[i] <= d and 0 <= distv[i] <= d:
        cnt += 1

print(cnt)