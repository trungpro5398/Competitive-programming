from math import ceil, log2


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[ 2 * index + 1] + segtree[2 * index + 2]

def updateQuery(segtree, a, left, right, index, pos, value):
    if pos < left or right < pos:
        return
    if left == right:
        a[pos] += value
        segtree[index] += value
        return
    mid = (left+right) // 2
    if pos <= mid:
        updateQuery(segtree, a, left, mid, 2 * index + 1, pos ,value)
    else:
        updateQuery(segtree, a, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] + segtree[ 2 * index + 2]

def sumRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 0
    mid = ( left + right ) // 2
    return sumRange(segtree, left, mid, fr, to, 2 * index + 1) + sumRange(segtree, mid + 1, right, fr, to, 2 * index + 2)


t = int(input())

for o in range(1, t+1):
    print("Case {}:".format(o))
    n, q =  list(map(int, input().split()))
    a =  list(map(int, input().split()))
    n = len(a)
    h = ceil(log2(n))
    sizeTree = 2 * ( 2 ** h ) - 1
    segTree = [float('inf')] * sizeTree
    lazy = [0] * sizeTree
    buildTree(a, segTree, 0, n-1, 0)
    while q:
        q -= 1
        b = list(map(int, input().split()))
        if b[0] == 1:
            print(a[b[1]])
            updateQuery(segTree, a, 0, n - 1, 0, b[1], -a[b[1]])
            a[b[1]] = 0
        elif b[0] == 2:

            updateQuery(segTree, a, 0,n-1,0, b[1], b[2] )
        else:
            print(sumRange(segTree, 0, n - 1, b[1], b[2], 0))