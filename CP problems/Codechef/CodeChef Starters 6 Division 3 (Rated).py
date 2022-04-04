import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        r,w,c = a[0], a[1], a[2]
        a = [int(x) for x in stdin.readline().split()]
        r1, w1, c1 = a[0], a[1], a[2]
        cnt = 0
        if r > r1:
            cnt += 1
        else:
            cnt -= 1
        if w > w1:
            cnt += 1
        else:
            cnt -= 1
        if c > c1:
            cnt += 1
        else:
            cnt -= 1

        if cnt > 0:
            print("A")
        else:
            print("B")

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        x,y  = a[0], a[1]

        res = ((6-x-y)/6)

        print(max(0, res))

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n,m,l = a[0], a[1], a[2]

def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n, q = a[0], a[1]
        a = [int(x) for x in stdin.readline().split()]
        even = [0] * n
        odd = [0] * n
        for i in range(0, n):
            if i > 0:
                even[i] = even[i-1]
                odd[i] = odd[i-1]
            if a[i] % 2 == 0:
                even[i] += 1
            else:
                odd[i] += 1
        while q:
            q -= 1
            a = [int(x) for x in stdin.readline().split()]
            l, r = a[0], a[1]
            l-=1
            r-=1
            if l == 0:
                od = odd[r]
                ev = even[r]
            else:
                od = odd[r] - odd[l-1]
                ev = even[r] - even[l-1]

            res = ev * (ev-1) * (ev-2) / 6
            res1 = od * (od-1) / 2
            res1 *= ev
            print(int(max(0, res) + max(0, res1)))

def E():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n, k = a[0], a[1]
        k += 1
        a = [int(x) for x in stdin.readline().split()]
        dp = [0] * (n+1)
        for i in range(0, n):
            dp[i] = a[i]
        for i in range(0, n):
            if i > 0:
                dp[i] = min(dp[i], dp[i] + dp[i-1])
            if i + k < n:
                dp[i+k] += dp[i]
        res = 10**9
        for i in range(n-k-1, n):
            res = min(res, dp[i])
        print( res)

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n,m,l = a[0], a[1], a[2]
        dp = [0] * (n+1)
        for i in range(m):
            a = [int(x) for x in stdin.readline().split()]
            for j in range(1, len(a)):
                dp[a[j]] = i + 1
        a = [int(x) for x in stdin.readline().split()]
        res = 1
        for i in range(0, len(a)-1):
            if dp[a[i+1]] != dp[a[i]]:
                res += 1
        print(res)

from collections import defaultdict
import sys


class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped.Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        if smallest != idx:
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    def extractMin(self):

        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):

        # Get the index of v in  heap array

        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is
        # not hepified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] < self.array[int((i - 1) / 2)][1]:
            # Swap this node with its parent
            self.pos[self.array[i][0]] = int((i - 1) / 2)
            self.pos[self.array[int((i - 1) / 2)][0]] = i
            self.swapMinHeapNode(i, int((i - 1) / 2))

        # move to parent index
            i = int((i - 1) / 2);

        # A utility function to check if a given
        # vertex 'v' is in min heap or not
    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    # Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):

        # Add an edge from src to dest.  A new node
        # is added to the adjacency list of src. The
        # node is added at the beginning. The first
        # element of the node has the destination
        # and the second elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # Since graph is undirected, add an edge
        # from dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    # The main function that calulates distances
    # of shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def dijkstra(self, src, end):

        V = self.V  # Get the number of vertices in graph
        dist = []  # dist values used to pick minimum
        # weight edge in cut

        # minHeap represents set E
        minHeap = Heap()

        #  Initialize min heap with all vertices.
        # dist value of all vertices
        for v in range(V):
            dist.append(float('inf'))
            minHeap.array.append(minHeap.newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)

        # Make dist value of src vertex as 0 so
        # that it is extracted first
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])

        # Initially size of min heap is equal to V
        minHeap.size = V

        path = [-1] * V
        vis = [False] * V
        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:

            # Extract the vertex
            # with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]
            if vis[u]:
                continue

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:

                v = pCrawl[0]
                if vis[v]:
                    continue
                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if minHeap.isInMinHeap(v) and dist[u] != float('inf') and pCrawl[1] + dist[u] < dist[v]:
                    dist[v] = pCrawl[1] + dist[u]

                    # update distance value
                    # in min heap also
                    minHeap.decreaseKey(v, dist[v])
                    path[v] = u
                    vis[u] = True
        u = end
        path_result = [u]
        while path[u] != -1:
            u = path[u]
            path_result.append(u)
        path_result.pop(-1)
        path_result.reverse()


        return (dist[end], path_result)
def F():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n,m,k = a[0], a[1], a[2]
        s = input()
        graph = Graph(n)
        for i in range(m):
            a = [int(x) for x in stdin.readline().split()]
            graph.addEdge(a[0], a[1], a[2])

