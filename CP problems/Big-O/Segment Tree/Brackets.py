from math import ceil, log2


def buildTree(a, segtree,segtree_min, left, right, index):
    if left == right:
        segtree[index] = a[left]
        segtree_min[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree,segtree_min, left, mid, 2 * index + 1)
    buildTree(a, segtree, segtree_min,mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[ 2 * index + 1] + segtree[2 * index + 2]
    segtree_min[index] = min(segtree_min[2*index+1], segtree[2*index+1] + segtree_min[2*index+2])

def updateQuery(segtree,segtree_min, a, left, right, index, pos, value):
    if pos < left or right < pos:
        return
    if left == right:
        segtree[index] = segtree_min[index] = -segtree[index]
        return
    mid = (left+right) // 2
    if pos <= mid:
        updateQuery(segtree,segtree_min, a, left, mid, 2 * index + 1, pos ,value)
    else:
        updateQuery(segtree,segtree_min, a, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] + segtree[ 2 * index + 2]
    segtree_min[index] = min(segtree_min[2 * index + 1], segtree[2 * index + 1] + segtree_min[2 * index + 2])





for o in range(1, 10+1):
    print("Test {}:".format(o))
    n = int(input())
    s = input()
    a = []
    for i in s:
        if i == '(':
            a.append(1)
        else:
            a.append(-1)
    n = len(a)
    h = ceil(log2(n))
    sizeTree = 2 * ( 2 ** h ) - 1
    segTree = [float('inf')] * sizeTree
    segTree_min = [float('inf')] * sizeTree
    lazy = [0] * sizeTree
    buildTree(a, segTree, segTree_min,0, n-1, 0)
    q = int(input())
    while q:
        q -= 1
        l = int(input())
        if l != 0:
            updateQuery(segTree,segTree_min, a, 0 , n-1, 0, l-1, 0)
        else:
            if segTree[0] == segTree_min[0] == 0:
                print("YES")
            else:
                print("NO")