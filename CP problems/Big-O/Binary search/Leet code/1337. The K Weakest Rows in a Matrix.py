import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        def bin_search(list):
            l, h = 0, len(list) - 1
            boundary = -1
            while l <= h:
                m = ( l + h ) // 2
                if list[m] == 1:
                    boundary = m
                    l = m + 1
                else:
                    h = m - 1
            return boundary

        res = []

        for i, lst in enumerate(mat):
            index = bin_search(lst)
            res.append((index+1, i))

        res.sort()
        ans = []
        for i in range(k):
            x, y = res[i]
            ans.append(y)
        return ans


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            t = (sum(row), i)
            heapq.heappush(heap, t)

        res = []
        for i in range(k):
            row = heapq.heappop(heap)
            res.append(row[1])
        return res

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr=sorted([[i,mat[i].count(1)] for i in range(len(mat))], key=lambda x:x[1])
        return [x[0] for x in arr[:k]]
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr=[[i,mat[i].count(1)] for i in range(len(mat))]
        arr.sort(key=lambda x: x[1])
        return [x[0] for x in arr[:k]]