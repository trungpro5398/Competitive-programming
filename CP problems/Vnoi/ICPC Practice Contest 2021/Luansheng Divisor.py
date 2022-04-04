import copy


def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    res = []
    for p in range(n + 1):
        if prime[p]:
            res.append(p)
    return res

prime = SieveOfEratosthenes(10**6 + 6)
t = int(input())

while t:
    t -= 1

    n = int(input())
    divisor = [1]
    temp = copy.deepcopy(n)
    l = 0
    while n > 1 and l < len(prime):
        if n % prime[l] == 0:
            divisor.append(prime[l])
            divisor.append(n)
        while n % prime[l] == 0:
            n //= prime[l]
        l += 1
    ans = []
    divisor.sort()
    print(divisor)
    for i in range(len(divisor)):
        if temp % ( divisor[i] + 1) == 0:
            ans.append(divisor[i])
        if i > 0 and  temp % ( divisor[i] - 1) == 0:
            if divisor[i] - 1 not in ans:
                ans.append(divisor[i]-1)
    ans.sort()
    if len(ans) == 0:
        print(-1)
    else:
        for i in ans:
            print(i, end = " ")
        print()