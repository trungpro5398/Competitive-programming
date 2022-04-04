from sys import stdin
# Extended Euclidean Algorithm:
# Extended Euclidean algorithm also finds integer coefficients x and y such that:
#
#   ax + by = gcd(a, b)

# function for extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y
t = int(input())
while t:
    t -= 1
    x, k = [int(x) for x in stdin.readline().split()]
    if x % k == 0:
        print("{} {}".format(0, k))
    elif x < k:
        print("{} {}".format(0, x))
    else:
        a = x // k
        b = x // k + 1
        g, x1, y1 = gcdExtended(a, b)

        x1 *= x // g
        y1 *= x // g
        print("{} {}".format(x1,y1))