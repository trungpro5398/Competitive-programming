def local_maximum(mat):
    m = len(mat)
    n = len(mat[0])
    if m == n == 1:
        return [0, 0]

    center_row = 0 + (len(mat) - 0) // 2
    l, r = 0, len(mat[center_row]) - 1
    keep_mid = False
    while l <= r:
        if not keep_mid:  # don't want to calculate mid again right after moving up or down
            mid = l + (r - l) // 2
        left = mat[center_row][mid - 1] if mid > 0 else -1
        right = mat[center_row][mid + 1] if mid < n - 1 else -1
        top = mat[center_row - 1][mid] if center_row > 0 else -1
        down = mat[center_row + 1][mid] if center_row < m - 1 else -1
        if left < mat[center_row][mid] > right:
            if top < mat[center_row][mid] > down:
                return [center_row, mid]
            elif top > mat[center_row][mid]:
                center_row -= 1
                l, r = 0, len(mat[center_row]) - 1
                keep_mid = True
            else:
                center_row += 1
                l, r = 0, len(mat[center_row]) - 1
                keep_mid = True
        elif left > mat[center_row][mid]:
            r = mid - 1
            keep_mid = False
        else:
            l = mid + 1
            keep_mid = False
M = [[1, 2, 27, 28, 29, 30, 49],
[3, 4, 25, 26, 31, 32, 48],
[5, 6, 23, 24, 33, 34, 47],
[7, 8, 21, 22, 35, 36, 46],
[9, 10, 19, 20, 37, 38, 45],
[11, 12, 17, 18, 39, 40, 44],
[13, 14, 15, 16, 41, 42, 43]]
print(local_maximum(M))