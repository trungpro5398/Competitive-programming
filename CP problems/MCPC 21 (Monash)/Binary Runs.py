

s = input()


def calculate(p, q):
    mod = 1000000007
    expo = 0
    expo = mod - 2

    # Loop to find the value
    # until the expo is not zero
    while (expo):

        # Multiply p with q
        # if expo is odd
        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod

        # Reduce the value of
        # expo by 2
        expo >>= 1

    return p

res = 100029997
p = 100029997
q = 200000000
for i in range(0, len(s)):
    if i == len(s)- 1:
        p *= 100029997
        p %= 1000000007
        q *= 200000000
        q %= 1000000007
        break
    if s[i] == s[i+1]:
        p *= 29997
        p %= 1000000007
        q *= 200000000
        q %= 1000000007
    else:
        p *= 100029997
        p %= 1000000007
        q *= 200000000 * 2
        q %= 1000000007

print(calculate(p,q))
