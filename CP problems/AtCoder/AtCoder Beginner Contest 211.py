import sys
from collections import deque
from sys import maxsize as INT_MAX


# Traverses graph in BFS manner. It fills
# dist[] and paths[]
def BFS(adj: list, src: int, dist: list, paths: list, n: int):
    visited = [False] * (n + 1)
    dist[src] = 0
    paths[src] = 1

    q = deque()
    q.append(src)
    visited[src] = True
    while q:
        curr = q[0]
        q.popleft()

        # For all neighbors of current vertex do:
        for x in adj[curr]:

            # if the current vertex is not yet
            # visited, then push it to the queue.
            if not visited[x]:
                q.append(x)
                visited[x] = True

            # check if there is a better path.
            if dist[x] > dist[curr] + 1:
                dist[x] = dist[curr] + 1
                paths[x] = paths[curr]

            # additional shortest paths found
            elif dist[x] == dist[curr] + 1:
                paths[x] += paths[curr]


# function to find number of different
# shortest paths form given vertex s.
# n is number of vertices.
def findShortestPaths(adj: list, s: int, n: int):
    dist = [INT_MAX] * (n + 1)
    paths = [0] * (n + 1)
    BFS(adj, s, dist, paths, n)
    print(paths[n] % (10**9+7))


# A utility function to add an edge in a
# directed graph.
def addEdge(adj: list, u: int, v: int):
    adj[u].append(v)


def D():
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for i in range(n + 1):
        adj[i] = []

    for i in range(m):
        a = [int(x) for x in sys.stdin.readline().split()]
        addEdge(adj, a[0], a[1])
        addEdge(adj, a[1], a[0])

    findShortestPaths(adj, 1, n)


A()