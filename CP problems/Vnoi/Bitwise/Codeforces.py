from sys import stdin


def CF_484_A():
    def countBits(n):
        cnt = 0
        while n:
            cnt += 1
            n >>= 1
        return cnt

    def countSetBits(n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        cntA = countBits(a[0])
        cntB = countBits(a[1])
        if cntB > cntA:
            if countSetBits(a[1]) == cntB:
                print(a[1])
            else:
                print((1 << (cntB-1))-1)
        else:
            a[0] <<= cntB - cntA
            for i in range(0, cntB + 1):
                res = a[0] | (1 << i)
                if res > a[1]:

                    break
                a[0] = res
            print(a[0])
def CF_1329_B():
    return 0
CF_1329_B()