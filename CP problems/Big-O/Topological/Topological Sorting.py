
import queue
def topological(graph, result, indegree):
    V = len(graph)
    zero_indegree = queue.PriorityQueue()
    for i in range(V):
        if indegree[i] == 0:
            zero_indegree.put(i)
    while not zero_indegree.empty():
        u = zero_indegree.get()
        result.append(u)
        for i in graph[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                zero_indegree.put(i)
    for i in range(V):
        if indegree[i]:
            return False
    return True
def main():
    global n, m
    n, m = map(int, input().split())
    indegree = [0] * n
    adj = [[] for _ in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
        indegree[y-1] += 1
    result = []
    res = topological(adj, result, indegree)
    if not res:
        print("Sandro fails.")
    else:
        for i in result:
            print("{}".format(i+1), end=" ")

if __name__ == "__main__":
    main()