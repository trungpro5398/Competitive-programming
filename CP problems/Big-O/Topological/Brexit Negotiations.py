import queue
from sys import stdin


def topoSort(adj, indegree, time):
    zero_indegree = queue.PriorityQueue()

    vis = [False] * len(adj)
    for i in range(n):
        if indegree[i] == 0:
            zero_indegree.put((time[i],i))


    ans = 0
    sum = n

    while not zero_indegree.empty():
        u = zero_indegree.get()
        sum -= 1
        ans = max(ans, u[0] + sum)

        for v in adj[u[1]]:
            indegree[v] -= 1
            if indegree[v] == 0 :

                zero_indegree.put((time[v],v))

    return ans


def main():
    global n, m
    n = int(input())
    adj = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]
    time = [0] * n
    for i in range(n):
        a = [int(x) for x in stdin.readline().split()]
        time[i] = a[0]
        if a[1] == 0:
            continue
        else:
            for j in range(2, len(a)):
                adj[i].append(a[j]-1)
                indegree[a[j]-1] += 1

    res = topoSort(adj, indegree, time)
    print(res)


if __name__ == "__main__":
    main()