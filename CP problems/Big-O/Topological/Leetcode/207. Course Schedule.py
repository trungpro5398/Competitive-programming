from typing import List

import queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for i in prerequisites:
            x, y = i
            graph[y].append(x)

        result = []
        v = len(graph)
        indegree = [0] * v
        zero_indegree = queue.Queue()
        for i in range(v):
            for j in graph[i]:
                indegree[j] += 1
        for i in range(v):
            if indegree[i] == 0:
                zero_indegree.put(i)
        if zero_indegree.empty():
            return False
        cnt = 0
        while not zero_indegree.empty():
            u = zero_indegree.get()
            cnt += 1
            result.append(u)
            for i in graph[u]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    zero_indegree.put(i)
        return cnt == numCourses