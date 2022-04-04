# Python program to print topological sorting of a DAG
from collections import defaultdict


# Class to represent a graph
from sys import stdin


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):

            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        stack.reverse()
        return stack

a =  [int(x) for x in stdin.readline().split()]
n, k = a[0], a[1]
g = Graph(n)

for i in range(k):
    a = [int(x) for x in stdin.readline().split()]
    for j in range(1, len(a)):
        g.addEdge(i, a[j] - 1)

k = g.topologicalSort()
for i in range(len(k)):
    k[i] += 1

dp = [0] * (n+1)
l = 1
sav = k[0]
while k:
    node = k[0]
    k.pop(0)
    dp[node] = l
    l = node

for i in range(1, len(dp)):
    if i == sav:
        print(0, end=" ")
        continue
    print(dp[i], end=" ")
import sys
sys.setrecursionlimit(10 ** 6)
def sol():


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
