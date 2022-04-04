def dfs(u, graph, visited, result):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited, result)
    result.append(u)

def topological(graph, result):
    V = len(graph)
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            dfs(i, graph, visited, result)
    result.reverse()

import queue

def topological_kahn(graph, result):
    V = len(graph)
    indegree = [0] * V
    zero_indegree = queue.Queue
    for u in range(V):
        for v in graph[u]:
            indegree[v] += 1
    for i in range(V):
        if indegree[i] == 0:
            zero_indegree.append(i)

    while not zero_indegree.empty():
        u =  zero_indegree.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.append(v)
    for i in range(V):
        if indegree[i] != 0:
            return False
    return True