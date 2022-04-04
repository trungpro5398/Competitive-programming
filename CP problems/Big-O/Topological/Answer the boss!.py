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

            for j in self.graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []
        dp = [0] * self.V
        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)
                    dp[i] = dp[u] + 1
            cnt += 1

        return (top_order, dp)





t = int(input())
l = 1
while t:
    t -= 1

    a = [int(x) for x in stdin.readline().split()]
    n, r = a[0], a[1]

    g = Graph(n)

    for i in range(r):
        a = [int(x) for x in stdin.readline().split()]
        x, y = a[0], a[1]
        g.addEdge(y, x)


    print("Scenario #{}:".format(l))
    k = g.topologicalSort()
    k1, k2 = k[0], k[1]
    k3 = []
    for i in range(0, len(k1)):

        k3.append((k2[k1[i]]+1,k1[i] ))
    k3.sort()
    for i in k3:
        print(i[0], end=" ")
        print(i[1])
    l+= 1


def main():
    t = int(input())
    for testNumber in range(1, t + 1):
        solveTest(testNumber)


def solveTest(testNumber):
    n, r = map(int, input().split())

    adj = [[] for u in range(n)]
    in_deg = [0 for u in range(n)]

    for i in range(r):
        u, v = map(int, input().split())
        adj[v].append(u)
        in_deg[u] += 1

    topo_order = topo_sort(adj)
    rank = [0 for i in range(n)]

    for u in topo_order:
        if in_deg[u] == 0:
            rank[u] = 1
        for v in adj[u]:
            rank[v] = max(rank[v], rank[u] + 1)

    employees = [Employee(u, rank[u]) for u in range(n)]
    employees.sort(key=lambda e: (e.rank, e.index))

    print("Scenario #{0}:".format(testNumber))

    for e in employees:
        print("{0} {1}".format(e.rank, e.index))


def topo_sort(adj):
    topo_order = []
    n = len(adj)
    visited = [False for u in range(n)]

    for u in range(n):
        if not visited[u]:
            dfs(u, adj, visited, topo_order)

    topo_order.reverse()

    return topo_order


def dfs(u, adj, visited, topo_order):
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj, visited, topo_order)

    topo_order.append(u)


class Employee:
    def __init__(self, index, rank):
        self.index = index
        self.rank = rank


if __name__ == "__main__":
    main()