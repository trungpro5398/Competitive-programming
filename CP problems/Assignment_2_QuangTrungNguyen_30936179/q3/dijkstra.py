import sys
from sys import stdin


class FibonacciHeap:
    # pointer to the root node and the minimum node in the root list
    root_list, min_node = None, None
    # the total nodes in full fibonacci heap
    cnt_nodes = 0

    # internal node class
    class Node:
        def __init__(self, key, payload):
            self.key = key
            self.payload = payload
            self.parent = self.children = self.leftSibling = self.rightSibling = None
            self.degree = 0
            self.mark = False

    def remove_node_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.rightSibling
        node.leftSibling.rightSibling = node.rightSibling
        node.rightSibling.leftSibling = node.leftSibling

    def remove_node_from_parent_in_child_list(self, parent, node):
        if parent.children == parent.children.rightSibling:
            parent.children = None
        elif parent.children == node:
            parent.children = node.rightSibling
            node.rightSibling.parent = parent
        node.leftSibling.rightSibling = node.rightSibling
        node.rightSibling.leftSibling = node.leftSibling

    def merge_node_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.rightSibling = self.root_list.rightSibling
            node.leftSibling = self.root_list
            self.root_list.rightSibling.leftSibling = node
            self.root_list.rightSibling = node

    def merge_node_with_parent_in_child_list(self, parent, node):
        if parent.children is None:
            parent.children = node
        else:
            node.rightSibling = parent.children.rightSibling
            node.leftSibling = parent.children
            parent.children.rightSibling.leftSibling = node
            parent.children.rightSibling = node

    # Function to traverse a doubly linked list
    def iterate_the_link_list(self, head):
        node = stop = head
        mark = False
        while True:
            if node == stop and mark:
                break
            elif node == stop:
                mark = True
            yield node
            node = node.rightSibling

    # get the value min node in O(1) time
    def min(self):
        return self.min_node

    # Concatenate the root lists of two fibonacci heaps to merge them in O(1) time.
    # the root of the new root list is equal to the first and second lists
    # The list is simply added at the end (then the proper min node is determined)
    def merge(self, H1, H2):
        H1.min_node.leftSibling.rightSibling = H2.min_node.rightSibling
        H2.min_node.rightSibling.leftSibling = H1.min_node.leftSibling
        H2.min_node.rightSibling = H1.min_node
        H1.min_node.leftSibling = H2.min_node
        # Create a new Fibonacci heap
        H = FibonacciHeap()
        # Set H_min to which ever of H1_min and H2_min has the smaller key
        H.min_node = min(H1.min_node, H2.min_node)
        H.cnt_nodes = H1.cnt_nodes + H2.cnt_nodes
        return H

    # in O(1) time, place a new node into the unordered root list
    def insert(self, key, payload):
        nodeToInsert = self.Node(key, payload)
        nodeToInsert.leftSibling = nodeToInsert.rightSibling = nodeToInsert
        self.merge_node_with_root_list(nodeToInsert)
        if self.min_node is None or nodeToInsert.key < self.min_node.key:
            self.min_node = nodeToInsert
        self.cnt_nodes += 1
        return nodeToInsert

    # separate (erase) the min hub from the store in O(log n) time
    def extract_min(self):
        h_min = self.min_node
        if h_min is not None:
            if h_min.children is not None:
                children = [_ for _ in self.iterate_the_link_list(h_min.children)]
                for i in range(0, len(children)):
                    self.merge_node_with_root_list(children[i])
                    children[i].parent = None
            self.remove_node_from_root_list(h_min)
            if h_min == h_min.rightSibling:
                self.min_node = self.root_list = None
            else:
                self.min_node = h_min.rightSibling
                self.consolidate()
            self.cnt_nodes -= 1
        return h_min

    # join root nodes of equivalent degree to combine the pile
    # by making a rundown of unordered binomial trees
    def consolidate(self):
        A = [None] * self.cnt_nodes
        nodes = [_ for _ in self.iterate_the_link_list(self.root_list)]
        for i in range(0, len(nodes)):
            node = nodes[i]
            degree = node.degree
            while A[degree] != None:
                temp_node = A[degree]
                if node.key > temp_node.key:
                    temp = node
                    node, temp_node = temp_node, temp
                self.link_to_node(temp_node, node)
                A[degree] = None
                degree += 1
            A[degree] = node
        for i in range(0, len(A)):
            if A[i] is not None:
                if A[i].key < self.min_node.key:
                    self.min_node = A[i]

    # change the key of some hub in the store in O(1) time
    def decrease_key(self, node, key):
        if key > node.key:
            return None
        node.key = key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self.cut_node(node, parent)
            self.cut_cascades(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    """
    1. Call decline key(x, −∞) to set the key of x to −∞. 
    2. Run separate min to eliminate x from the load.
    """

    def delete(self, node):
        self.decrease_key(node, -float('inf'))
        self.extract_min()

    # if a child node smaller than parent node
    # it will be cut and i will put it to the root list
    def cut_node(self, node_a, node_b):
        self.remove_node_from_parent_in_child_list(node_b, node_a)
        node_b.degree -= 1
        self.merge_node_with_root_list(node_a)
        node_a.parent = None
        node_a.mark = False

    # cascading cut of parent node
    def cut_cascades(self, node):
        temp_node = node.parent
        if temp_node is not None:
            if node.mark is False:
                node.mark = True
            else:
                self.cut_node(node, temp_node)
                self.cut_cascades(temp_node)

    # actual association of a node with another node in the original list
    # also update the sublinked list
    def link_to_node(self, node_b, node_a):
        self.remove_node_from_root_list(node_b)
        node_b.leftSibling = node_b.rightSibling = node_b
        self.merge_node_with_parent_in_child_list(node_a, node_b)
        node_a.degree += 1
        node_b.parent = node_a
        node_b.mark = False


def dijkstra(list_nodes, source):
    n = len(list_nodes)
    marked_node = [False] * n
    distance_2_nodes = [float('inf')] * n

    heap_nodes = [None] * n
    heap = FibonacciHeap()
    for i in range(0, n):
        heap_nodes[i] = heap.insert(float('inf'), i)  # crate an infinity distance, and label

    distance_2_nodes[source] = 0
    heap.decrease_key(heap_nodes[source], 0)

    while heap.cnt_nodes:
        current_node = heap.extract_min().payload  # get the min node in the fibonaci heap and rearrange thhis
        marked_node[current_node] = True  # mark this node and never visit again

        for (u, w) in list_nodes[current_node]:  # get all children of this

            if not marked_node[u]:  # if no visited
                if distance_2_nodes[current_node] + w < distance_2_nodes[u]:
                    distance_2_nodes[u] = distance_2_nodes[current_node] + w
                    heap.decrease_key(heap_nodes[u],
                                      distance_2_nodes[u])  # push it to the fibonaci heap and rearrange this

    return distance_2_nodes


def write_result(output):
    file_name = 'output_dijkstra.txt'
    with open(file_name, 'w') as file:
        for line in output:
            file.write('{0} {1}\n'.format(line[0], line[1]))


if __name__ == '__main__':
    txtFileName = sys.argv[1]
    txt = [line.strip().split() for line in open(txtFileName, 'r')]
    n, m = int(txt[0][0]), int(txt[0][1])

    adjList = [[] for _ in range(n + 1)]

    for i in range(m):
        vx, vy, weight = int(txt[i + 1][0]), int(txt[i + 1][1]), int(txt[i + 1][2])
        adjList[vx].append((vy, weight))
        adjList[vy].append((vx, weight))

    distance = dijkstra(adjList, 0)
    res = []
    for i in range(0, n):
        res.append((i, distance[i]))
    write_result(res)
