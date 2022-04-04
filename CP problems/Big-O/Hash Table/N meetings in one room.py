from sys import stdin


class meeting:

    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

t = int(input())

while t:
    t -= 1
    n = int(input())
    s = [int(x) for x in stdin.readline().split()]
    f = [int(x) for x in stdin.readline().split()]
    mt = []
    for i in range(0, n):
        mt.append(meeting(s[i], f[i], i))
    mt.sort(key = lambda x: x.end)

    ans = []
    ans.append(mt[0].pos)

    time = mt[0].end

    for i in range(1,n):
        if time < mt[i].start:
            ans.append(mt[i].pos)
            time = mt[i].end

    for i in ans:
        print(i+1, end = " ")
    print()