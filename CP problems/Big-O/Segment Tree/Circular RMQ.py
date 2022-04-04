from math import ceil, log2


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = min(segtree[ 2 * index + 1], segtree[2 * index + 2])

def updateQuerry_sumQueryLazy(segtree, lazy, left, right, fr, to, delta, index):

    if lazy[index] != 0:
        segtree[index] += lazy[index]
        if left != right:
            lazy[2*index+1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0
    if fr <= left and right <= to:
        segtree[index] += delta
        if left != right:
            lazy[2 * index + 1] += delta
            lazy[2 * index + 2] += delta
        return
    if min(right,to) < max(left, fr):
        return

    mid = (left + right) // 2
    updateQuerry_sumQueryLazy(segtree, lazy, left, mid, fr, to, delta, 2 * index + 1)
    updateQuerry_sumQueryLazy(segtree, lazy, mid + 1, right, fr, to, delta, 2 * index + 2)
    segtree[index] = min(segtree[2*index+1], segtree[2*index+2])

def minQueryLazy(segtree, lazy, left, right, fr, to, index):
    if min(right, to) < max(left, fr):
        return 10**9
    if lazy[index] != 0:
        segtree[index] += lazy[index]
        if left != right:
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0

    if fr <= left and to >= right:
        return segtree[index]

    mid = (left + right) // 2
    return min(minQueryLazy(segtree, lazy, left, mid, fr, to, 2 * index + 1), minQueryLazy(segtree, lazy, mid+1, right, fr, to, 2 * index + 2))

n = int(input())
a =  list(map(int, input().split()))
n = len(a)
h = ceil(log2(n))
sizeTree = 2 * ( 2 ** h ) - 1
segTree = [float('inf')] * sizeTree
lazy = [0] * sizeTree
buildTree(a, segTree, 0, n-1, 0)
m = int(input())

for i in range(m):
    b = list(map(int, input().split()))
    if len(b) == 2:
        if b[0] <= b[1]:
            print(minQueryLazy(segTree, lazy, 0, n - 1, b[0], b[1], 0))
        else:
            print(min(minQueryLazy(segTree, lazy, 0, n - 1, b[0], n-1, 0), minQueryLazy(segTree, lazy, 0, n - 1, 0, b[1], 0)))

    else:
        if b[0] <= b[1]:
            updateQuerry_sumQueryLazy(segTree, lazy, 0, n - 1, b[0], b[1], b[2], 0)
        else:
            updateQuerry_sumQueryLazy(segTree, lazy, 0, n - 1, b[0], n-1, b[2], 0)
            updateQuerry_sumQueryLazy(segTree, lazy, 0, n - 1, 0, b[1], b[2], 0)


