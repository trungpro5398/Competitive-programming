import queue
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for i in prerequisites:
            x, y = i
            graph[y].append(x)

        v = len(graph)
        indegree = [0] * v
        zero_indegree = queue.Queue()
        for i in range(v):
            for j in graph[i]:
                indegree[j] += 1

        for i in range(v):
            if indegree[i] == 0:
                zero_indegree.put(i)

        result = []
        cnt = 0
        while not zero_indegree.empty():
            u = zero_indegree.get()
            result.append(u)
            cnt += 1
            for i in graph[u]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    zero_indegree.put(i)
        if cnt != numCourses:
            return  []
        return result