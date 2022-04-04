import sys

sys.setrecursionlimit(100000)
from queue import PriorityQueue


def dfs(u, graph, res, check):
    cycle = False
    if check[u] == 0:
        check[u] = 1
        for v in graph[u]:
            cycle = cycle or dfs(v, graph, res, check)
        check[u] = 2
        res.append(u + 1)
    elif check[u] == 1:
        cycle = True
    return cycle


def schedule(n, k, graph, needed_courses):
    cycle = False
    res = []
    check = [0] * n
    for u in needed_courses:
        if dfs(u, graph, res, check):
            cycle = True
            break

    if cycle:
        return -1

    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    needed_courses = list(map(int, input().split()))
    needed_courses = list(map(lambda x: x - 1, needed_courses))
    sorted(needed_courses)
    graph = [[] for _ in range(n)]
    for u in range(n):
        num, *adj = map(int, input().split())
        for v in adj:
            graph[u].append(v - 1)

    res = schedule(n, k, graph, needed_courses)
    if res == -1:
        print(res)
    else:
        print(len(res))
        print(' '.join(map(str, res)))