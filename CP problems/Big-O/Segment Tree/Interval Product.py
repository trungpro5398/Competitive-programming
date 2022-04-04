from math import ceil, log2


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[ 2 * index + 1] * segtree[2 * index + 2]

def updateQuery(segtree, a, left, right, index, pos, value):
    if pos < left or right < pos:
        return
    if left == right:
        a[pos] = value
        segtree[index] = value
        return
    mid = (left+right) // 2
    if pos <= mid:
        updateQuery(segtree, a, left, mid, 2 * index + 1, pos ,value)
    else:
        updateQuery(segtree, a, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] * segtree[ 2 * index + 2]

def productRange(segtree, left, right, fr, to, index):

    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 1
    mid = ( left + right ) // 2
    return productRange(segtree, left, mid, fr, to, 2 * index + 1) * productRange(segtree, mid + 1, right, fr, to, 2 * index + 2)




try:
    while True:
        n, q = list(map(int, input().split()))
        a = list(map(int, input().split()))
        n = len(a)
        h = ceil(log2(n))
        sizeTree = 2 * (2 ** h) - 1
        segTree = [float('inf')] * sizeTree
        lazy = [0] * sizeTree
        buildTree(a, segTree, 0, n - 1, 0)
        for _ in range(q):
            b = input().split()
            b[1] = int(b[1]) - 1
            b[2] = int(b[2])
            if b[0] == 'C':
                updateQuery(segTree, a, 0, n - 1, 0, b[1], b[2])
            else:
                ans = productRange(segTree, 0, n - 1, b[1], b[2]-1, 0)
                if ans == 0:
                    print(0, end = "")
                elif ans < 0:
                    print('-', end ="")
                else:
                    print('+', end ="")
        print()


except:
    pass