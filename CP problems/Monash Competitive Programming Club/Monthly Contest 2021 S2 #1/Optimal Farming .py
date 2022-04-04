rows, cols =  map(int, input().split())
arr = [[0 for i in range(cols)] for j in range(rows)]
vis = [[True for i in range(cols)] for j in range(rows)]
for i in range(rows):
    s = input()
    for j in range(cols):
        if s[j] == 'T':
            arr[i][j] = 1
        else:
            arr[i][j] = 0
            vis[i][j] = False
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]


def isValid(vis, row, col):
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= rows or col >= cols):
        return False

    # If cell is already visited
    if vis[row][col]:
        return False

    # Otherwise
    return True


# Function to perform the BFS traversal
def BFS(grid, vis, row, col):
    # Stores indices of the matrix cells
    q = []

    # Mark the starting cell as visited
    # and push it into the queue
    q.append((row, col))
    vis[row][col] = True

    # Iterate while the queue
    # is not empty
    cnt = 0
    res = []
    res1 = []
    while q:
        cell = q.pop(0)
        x = cell[0]
        y = cell[1]
        cnt += 1
        res.append(x)
        res1.append(y)
        # q.pop()

        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
    res.sort()
    res1.sort()
    sav = max(res) - min(res) + 1
    sav1 = max(res1) - min(res1) + 1

    if len(res) == 1:
        return cnt
    if cnt > max(sav,sav1):
        return max(sav,sav1)
    return cnt
res = 0
for i in range(rows):
    for j in range(cols):
        if not arr[i][j] and not vis[i][j]:
            res += BFS(arr, vis, i, j)

print(res)