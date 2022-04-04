from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        def lower_bound(lst, num):
            l, r = 0, len(lst) - 1
            while l < r:
                m = ( l + r ) // 2
                if lst[m] >= num:
                    r = m
                else:
                    l = m + 1
            return l
           

