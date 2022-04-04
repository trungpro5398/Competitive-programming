import queue

def topological(graph, result, indegree):
    V = len(graph)
    zero_indegree = queue.PriorityQueue()
    for i in range(V):
        if indegree[i] == 0:
            zero_indegree.put(i)
    cnt = 0
    while not zero_indegree.empty():
        u = zero_indegree.get()
        result.append(u)
        for i in graph[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                zero_indegree.put(i)
        cnt += 1
    if cnt != 26:
        print("Impossible")
    else:
        for i in result:
            print(chr(i + ord('a')), end="")

def main():
    t = int(input())
    s = [""] * t
    for l in range(t):
        s[l] = input()

    graph = [[] for _ in range(26)]
    for i in range(t-1):
        c = False
        for j in range(min(len(s[i]), len(s[i+1]))):
            if s[i][j] != s[i+1][j]:
                c = True
                temp = ord(s[i][j]) - ord('a')
                temp1 = ord(s[i+1][j]) - ord('a')
                graph[temp].append(temp1)
                break
        if not c and len(s[i]) > len(s[i + 1]):
            print("Impossible")
            return
    indegree = [0] * len(graph)
    for i in range(len(graph)):
        graph[i].sort()
        for j in graph[i]:
            indegree[j] += 1

    result = []

    topological(graph, result, indegree)
if __name__ == "__main__":
    main()