from sys import stdin

t = int(input())

while t:
    t -= 1
    n = int(input())
    a = [int(x) for x in stdin.readline().split()]

    ans = 0
    for i in range(0, 31):

        odd, even = 0, 1
        cnt = 0
        sum = 0
        for j in a:
            if j & ( 1 << i):
                cnt += 1
            if cnt % 2 == 1:
                odd += 1
                sum += even
            else:
                even += 1
                sum += odd
            print(even, odd, sum)
        ans += sum * (1<<i)
    print(ans)
