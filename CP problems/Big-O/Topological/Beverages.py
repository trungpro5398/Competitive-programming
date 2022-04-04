

from collections import defaultdict


# Class to represent a graph
from sys import stdin

import heapq
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # The function to do Topological Sort.
    def topologicalSort(self):

        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0] * (self.V)

        # Traverse adjacency lists to fill indegrees of
        # vertices.  This step takes O(V + E) time
        for i in self.graph:
            self.graph[i].sort()
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        li = []
        heapq.heapify(li)
        for i in range(self.V):
            if in_degree[i] == 0:
                heapq.heappush(li,i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while li:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = heapq.heappop(li)
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    heapq.heappush(li, i)

            cnt += 1

        # Check if there was a cycle
        return top_order


l = 1
while True:
    try:
        n = int(input())
        g = {}
        g2 = {}
        for i in range(n):
            s = str(input())
            g[s] = i
            g2[i] = s
        e = int(input())
        g1 = Graph(n)
        for i in range(e):
            f, t = list(map(str, input().split()))
            k = g[f]
            k1 = g[t]
            g1.addEdge(k, k1)

        order = []
        for i in g1.topologicalSort():
            order.append(g2[i])

        order = " ".join(order)
        print("Case #{}: Dilbert should drink beverages in this order: {}.".format(l, order))
        print()
        input()

        l += 1
    except(EOFError):
        break
from heapq import heappush, heappop


def topological_sort(graph, indegree, ordering):
    global N
    global names
    zero_indegree = []

    for u in range(N):
        if indegree[u] == 0:
            heappush(zero_indegree, u)

    while zero_indegree:
        u = heappop(zero_indegree)
        ordering.append(names[u])

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(zero_indegree, v)


tc = 1
while True:
    try:
        N = int(input())
    except EOFError:
        exit()

    vertices = dict()
    names = []
    graph = [[] for _ in range(N)]
    indegree = [0] * N

    for i in range(N):
        beverage = input()
        vertices[beverage] = i
        names.append(beverage)

    M = int(input())
    for _ in range(M):
        beverage_1, beverage_2 = input().split()
        u, v = vertices[beverage_1], vertices[beverage_2]
        graph[u].append(v)
        indegree[v] += 1

    ordering = []
    topological_sort(graph, indegree, ordering)

    print('Case #{}: Dilbert should drink beverages in this order: '.format(tc), end='')
    print(*ordering, end='.\n\n')
    tc += 1
    input()

from heapq import heappush, heappop


def topological_sort(graph, indegree, ordering):
    global N
    global names
    zero_indegree = []

    for u in range(N):
        if indegree[u] == 0:
            heappush(zero_indegree, u)

    while zero_indegree:
        u = heappop(zero_indegree)
        ordering.append(names[u])

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(zero_indegree, v)


tc = 1
while True:
    try:
        N = int(input())
    except EOFError:
        exit()

    vertices = dict()
    names = []
    graph = [[] for _ in range(N)]
    indegree = [0] * N

    for i in range(N):
        beverage = input()
        vertices[beverage] = i
        names.append(beverage)

    M = int(input())
    for _ in range(M):
        beverage_1, beverage_2 = input().split()
        u, v = vertices[beverage_1], vertices[beverage_2]
        graph[u].append(v)
        indegree[v] += 1

    ordering = []
    topological_sort(graph, indegree, ordering)

    print('Case #{}: Dilbert should drink beverages in this order: '.format(tc), end='')
    print(*ordering, end='.\n\n')
    tc += 1
    input()



def topoSort(adj, indegree):
    zero_indegree = queue.PriorityQueue()
    topoSorted = []

    for i in range(n):
        if indegree[i] == 0:
            zero_indegree.put(i)

    while not zero_indegree.empty():
        u = zero_indegree.get()
        topoSorted.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)

    return topoSorted


def main():
    global n, m
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]

    for i in range(m):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        indegree[v-1] += 1

    res = topoSort(adj, indegree)
    if (len(res) < n):
        print("Sandro fails.")
        return 0

    for i in range(n):
        print("{} ".format(res[i] + 1), end="")


if __name__ == "__main__":
    main()

import sys

sys.setrecursionlimit(10 ** 6)


def dfs(u, graph, visited, ordering):
    global parent
    visited[u] = True

    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited, ordering)

    ordering.append(u)


def topological_sort(graph, ordering):
    global N
    visited = [False] * (N + 1)
    for u in range(1, N + 1):
        if not visited[u]:
            dfs(u, graph, visited, ordering)


N, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for u in range(1, K + 1):
    n, *adj_u = list(map(int, input().split()))
    graph[u] = adj_u

parent = [0] * (N + 1)
ordering = []
topological_sort(graph, ordering)

for i in range(N - 1):
    parent[ordering[i]] = ordering[i + 1]

for u in range(1, N + 1):
    print(parent[u])

from sys import stdin

t = int(input())

while t:
    a = [int(x) for x in stdin.readline().split()]

    ans = 0
    while True:
        b = [int(x) for x in stdin.readline().split()]
        dp = [[0 for i in range(len(b))] for j in range(len(a))]
        if len(b) == 1:
            break

        for i in range(len(a)):
            for j in range(len(b)):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]  + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        ans = max(dp[-1][-1], ans)
    print(ans)
    t -= 1

from sys import stdin

t1 = int(input())

while t1:
    t1 -= 1
    n, w = [int(x) for x in stdin.readline().split()]
    c = [0] * (n+1)
    p = [0] *  (n+1)
    t = [0] *  (n+1)
    for i in range(1,n+1):
        c[i], p[i], t[i] =  [int(x) for x in stdin.readline().split()]
    dp = [[0] * (w+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1,w+1):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if j >= t[i]:
                dp[i][j] = max(dp[i][j] , p[i]*c[i] + dp[i-1][j-t[i]])

    print(dp[n][w])