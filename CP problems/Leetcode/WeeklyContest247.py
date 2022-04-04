class Solution:
    def maxProductDifference(self, nums) -> int:
        nums.sort()
        print((nums[len(nums)-1] * nums[len(nums)-2]) - (nums[0]*nums[1]))

def B():
    grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    k = 2
    n, m = len(grid), len(grid[0])
    mat = [[0 for x in range(m)] for x in range(n)]
    l = 0
    r = n
    l1 = 0
    r1 = m
    while l < r:
        sav = r1 * (r - 1)
        for i in range(l1, r1):
            res = i + k
            res %= sav
            if l1 <= res <= r1 - 1:
                mat[l][i] = grid[l][res]
            elif l1 + r1 - 1<= res <= r1 + r - 2:
                mat[l][i] = grid[res - (l1 + r1 - 1)][r1-1]
            elif l1 + r1 - 1 + r - 1 <= res <= r1 + r - 2 + r1 - 1:
                mat[l][i] = grid[r-1][res - (l1 + r1 - 1 + r - 1)]
            else:
                mat[l][i] = grid[abs(res - (l1 + r1 - 1 + r - 1 + r1 - 1))][l]
        print(mat)
        for i in range(l + 1, r):
            res = i + k + r1 - 1
            res %= sav

            if l1 <= res <= r1 - 1:
                mat[i][r-1] = grid[l][res]
            elif l1 + r1 - 1<= res <= r1 + r - 2:
                mat[i][r-1] = grid[res - (l1 + r1 - 1)][r1-1]
            elif l1 + r1 - 1 + r - 1 <= res <= r1 + r - 2 + r1 - 1:
                mat[i][r-1] = grid[r-1][res - (l1 + r1 - 1 + r - 1)]
            else:

                mat[i][r-1] = grid[abs(res - (l1 + r1 - 1 + r - 1 + r1 - 1))%r][l]
        print(mat)
        for i in range(l1 + 1, r1):
            res = i + k + r1 - 1 + r - 1
            res %= sav
            if l1 <= res <= r1 - 1:
                mat[r-1][i] = grid[l][res]
            elif l1 + r1 - 1<= res <= r1 + r - 2:
                mat[r-1][i] = grid[res - (l1 + r1 - 1)][r1-1]
            elif l1 + r1 - 1 + r - 1 <= res <= r1 + r - 2 + r1 - 1:
                mat[r-1][i] = grid[r-1][res - (l1 + r1 - 1 + r - 1)]
            else:
                mat[r-1][i] = grid[abs(res - (l1 + r1 - 1 + r - 1 + r1 - 1))%r][l]
        print(mat)
        for i in range(l + 1, r):
            res = i + k + r1 - 1 + r - 1 + r1 - 1
            res %= sav
            if l1 <= res <= r1 - 1:
                mat[i][l] = grid[l][res]
            elif l1 + r1 - 1<= res <= r1 + r - 2:
                mat[i][l] = grid[res - (l1 + r1 - 1)][r1-1]
            elif l1 + r1 - 1 + r - 1 <= res <= r1 + r - 2 + r1 - 1:
                mat[i][l] = grid[r-1][res - (l1 + r1 - 1 + r - 1)]
            else:
                mat[i][l] = grid[abs(res - (l1 + r1 - 1 + r - 1 + r1 - 1))][l]
        print(mat)
        l += 1
        r -= 1
        l1 += 1
        r1 -= 1
    print(mat)



B()