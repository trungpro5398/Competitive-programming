from math import ceil, log2


def buildTree(a, segtree, left, right, index, degree):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1, degree - 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2, degree - 1)
    if degree % 2 == 1:
        segtree[index] = segtree[ 2 * index + 1] | segtree[2 * index + 2]
    else:
        segtree[index] = segtree[2 * index + 1] ^ segtree[2 * index + 2]

def updateQuery(segtree, a, left, right, index, pos, value, degree):
    if pos < left or right < pos:
        return
    if left == right:
        a[pos] = value
        segtree[index] = value
        return
    mid = (left+right) // 2
    if pos <= mid:
        updateQuery(segtree, a, left, mid, 2 * index + 1, pos ,value, degree-1)
    else:
        updateQuery(segtree, a, mid + 1, right, 2 * index + 2, pos, value, degree-1)
    if degree % 2 == 1:
        segtree[index] = segtree[2 * index + 1] | segtree[ 2 * index + 2]
    else:
        segtree[index] = segtree[2 * index + 1] ^ segtree[2 * index + 2]


def sumRange(segtree, left, right, fr, to, index, degree):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 0
    mid = ( left + right ) // 2
    leftSum = sumRange(segtree, left, mid, fr, to, 2 * index + 1, degree - 1)
    rightSum = sumRange(segtree, mid + 1, right, fr, to, 2 * index + 2, degree - 1)
    if degree % 2 == 1:
        return leftSum | rightSum
    else:
        return leftSum ^ rightSum

n, m = list(map(int, input().split()))
a =  list(map(int, input().split()))
n = len(a)
h = ceil(log2(n))
sizeTree = 2 * ( 2 ** h ) - 1
segTree = [float('inf')] * sizeTree
lazy = [0] * sizeTree
buildTree(a, segTree, 0, n-1, 0, h)

for i in range(m):
    p, b = list(map(int, input().split()))
    updateQuery(segTree, a, 0, n - 1, 0, p - 1, b, h)
    print(sumRange(segTree, 0, n - 1, 0, n-1, 0,h))