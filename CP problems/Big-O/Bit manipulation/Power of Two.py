from sys import stdin
# Check if bitwise AND of any subset is power of two
t = int(stdin.readline())

def isPowerOf2(num):
    return (num and (num & (num - 1)) == 0)
while t:
    t -= 1
    n = int(stdin.readline())
    a = [int(x) for x in stdin.readline().split()]
    bl = False
    ans = 0
    for i in range(0, 32): # To set/turn on the j-th item (0-based indexing) of the set
        ans |= (1 << i)
    for i in range(0, 32):
        sum = ans
        for j in a:
            if j & (1<<i):
                sum &= j
        if isPowerOf2(sum):
            bl = True
            break
    if bl:
        print("YES")
    else:
        print("NO")