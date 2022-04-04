from sys import stdin
global n,m
n,m,q =[int(x) for x in stdin.readline().split()]
arr = [[0 for i in range(m)] for j in range(n)]
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]
for i in range(n):
    a = [int(x) for x in stdin.readline().split()]
    for j in range(m):
        arr[i][j] = a[j]


def isValid(vis, row, col):
    # If cell lies out of bounds
    global n,m
    if (row < 0 or col < 0 or row >= n or col >= m):
        return False

    # If cell is already visited
    if (row,col) in vis:
        return False

    # Otherwise
    return True


# Function to perform the BFS traversal
def BFS(arr, vis, row, col,s):
    # Stores indices of the matrix cells
    q = []
    cnt = 1
    # Mark the starting cell as visited
    # and push it into the queue
    q.append((row, col))
    vis[(row,col)] = 1

    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        cell = q.pop(0)
        x = cell[0]
        y = cell[1]
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy)) and abs(arr[adjx][adjy] - arr[x][y]) <= s:
                q.append((adjx, adjy))
                vis[(adjx, adjy)] = 1
                cnt += 1
    print(cnt)
while q:
    q -= 1
    a,b,s = [int(x) for x in stdin.readline().split()]
    vis = {}
    BFS(arr, vis, b-1,a-1,s)