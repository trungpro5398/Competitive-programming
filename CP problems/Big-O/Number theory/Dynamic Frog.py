import copy

t = int(input())

for j in range(1, t+1):
    n, d = input().split()
    n = int(n)
    d = int(d)
    s = input().split()
    ans = 0
    queue = []
    queue.append([True,0])
    for i in range(n+1):
        if i < n:
            ty, st = s[i].split('-')
            st = int(st)
        else:
            st = d

        dis = copy.deepcopy(st)
        # compare with previous stone if last one is a big
        # compare with i - 2 stone if last one is a small (we can ignore previous stone since it is the min or used)
        if queue[-1][0]:
            dis -= queue[-1][1]
        else:
            dis -= queue[-2][1]
        ans = max(ans, dis)
        if i < n:
            queue.append([ty == 'B', int(st)])

    print("Case {}: {}".format(j, ans))

