from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        def bin_search(list):
            l = 0
            h = len(list) - 1
            boundary = -1
            while l <= h:
                m = ( l + h ) // 2
                if list[m] < 0:
                    boundary = m
                    h = m - 1
                else:
                    l = m + 1
            return boundary
        count = 0
        for lis in grid:
            # Returns -1 when there are no negative numbers in the list
            negInd = bin_search(lis)
            count += len(lis) - negInd if negInd >= 0 else 0
        return count