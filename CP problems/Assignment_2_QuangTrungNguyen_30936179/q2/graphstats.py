import sys


def hammingDistance(words):
    l = len(words[0])

    assert all(len(w) == l for w in words)

    added_groups = set()
    graph = {}

    for i in range(l - 1):
        for j in range(i + 1, l):
            groups = {}
            for k, word in enumerate(words):
                w = word[:i] + word[i + 1:j] + word[j + 1:]
                if w in groups:
                    groups[w].append(k)
                else:
                    groups[w] = [k]

            for w in groups:
                group = tuple(groups[w])
                if group in added_groups:
                    continue
                added_groups.add(group)
                for x, a in enumerate(group):
                    for b in group[x + 1:]:
                        edge = (a, b)
                        graph[edge] = 2

    for i in range(l):
        groups = {}
        for k, word in enumerate(words):
            w = word[:i] + word[i + 1:]
            if w in groups:
                groups[w].append(k)
            else:
                groups[w] = [k]

        for w in groups:
            group = groups[w]
            for x, a in enumerate(group):
                for b in group[x + 1:]:
                    edge = (a, b)
                    graph[edge] = 1
    return graph


def dfs(u):
    global sum_weight, vis, adjList, cnt
    vis[u] = True
    cnt += 1
    for i in adjList[u]:
        v, w = i
        if not vis[v]:
            sum_weight += w
            dfs(v)


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parents = [-1] * vertices

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, a):
        # find root of the tree containing ‘a’
        if self.parents[a] < 0:  # root is reached
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        root_a = self.find(a) # find root of tree containing ‘a’
        root_b = self.find(b) # find root of tree containing ‘b’

        if root_a == root_b: # ‘a’ and ‘b’ in the same tree
            return
        height_a = -self.parents[root_a] # height+1 of tree containing ‘a’
        height_b = -self.parents[root_b] # height+1 of tree containing ‘b’
        if height_a > height_b:
            self.parents[root_b] = root_a # link shorter tree’s root to taller
        elif height_b > height_a:
            self.parents[root_a] = root_b
        else: # if (height_a == height_b)
            self.parents[root_a] = root_b
            self.parents[root_b] = -(height_b + 1) # update: height grows by 1

    #  Applying Kruskal algorithm
    """
    1. Sort all the edges in non-decreasing order of their weight. 
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
3. Repeat step#2 until there are (V-1) edges in the spanning tree.
    """
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(u)
            y = self.find(v)
            if x != y:
                e = e + 1
                # we got the edge u,v having the smallest weight w
                result.append([u, v, w])
                self.union(x, y)
        global sum_weight, vis, adjList, cnt
        adjList = [[] for _ in range(self.V + 1)]
        for u, v, weight in result:
            adjList[u].append((v, weight))
            adjList[v].append((u, weight))
        res = []
        vis = [False] * self.V
        """
        Now I need to find the connected vertices in the graph using dfs to find the number of vertices in that subgraph 
        component and the minimum weight of the spanning tree on that subgraph. 
        Every time dfs reaches each vertex I will mark it as True and will never go to it again.
        """
        for i in range(0, self.V):
            sum_weight = 0
            cnt = 0
            if not vis[i]:
                dfs(i)
            if cnt == 0 and sum_weight == 0:
                continue
            res.append((cnt, sum_weight))
        # when disjoint components have the same size, sort their weights in descending order
        res.sort()
        return len(res), res[::-1]


def write_result(vertices, edges, numberOfDisJointSet, output):
    file_name = 'output_graphstats.txt'
    with open(file_name, 'w') as file:
        file.write('{0} {1}\n'.format(vertices, edges))
        file.write('{}\n'.format(numberOfDisJointSet))
        for line in output:
            file.write('{0} {1}\n'.format(line[0], line[1]))


if __name__ == '__main__':
    txtFileName = sys.argv[1]

    words = [line.strip() for line in open(txtFileName, 'r')]
    g = Graph(len(words))
    graphs = hammingDistance(words)
    for i in graphs:
        u, v = i
        w = graphs[i]
        g.add_edge(u, v, w)
        g.add_edge(v, u, w)
    disJonS, res = g.kruskal()
    write_result(len(words), len(graphs), disJonS, res)
