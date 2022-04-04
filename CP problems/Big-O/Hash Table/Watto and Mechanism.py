
import sys

# Quang Trung Nguyen ID:30936179
def get_z_value(pattern, Z):

    n = len(pattern)
    k, l, r = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and pattern[r-l] == pattern[r]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < n and pattern[r-l] == pattern[r]:
                    r += 1
                Z[i] = r - l
                r -= 1

def Z_al():
    t = int(input())
    for j in range(1, t + 1):
        s = input()
        Z = [0] * len(s)
        cnt = 0
        get_z_value(s, Z)
        for i in range(1, len(Z)):
            if Z[i] + i == len(Z):
                cnt += 1
        print("Case {}: {}".format(j, cnt))


#pre Compute Pow
Pow = [0] * 4000001

base = 33
Pow[0] = 1


n,m = [int(x) for x in sys.stdin.readline().split()]
hashed = []

mod = 10**9+7
for i in range(1, 4000001):
    Pow[i] =(Pow[i-1]*base) % mod
def computeHash(s):
    res = 0
    for i in range(0, len(s)):
        res += ((ord(s[i])- ord('a')+1) * Pow[i]) % mod
    return res
for j in range(1, n + 1):
    s = input()



    hashed.append(computeHash(s))

hashed.sort()


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1
for i in range(m):
    s = input()
    res = computeHash(s)
    ans = False
    for j in range(0, len(s)):
        sav = ((ord(s[j])- ord('a')+1) * Pow[j]) % mod
        res -= sav
        k = "abc"
        for c in k:
            if c != s[j]:
                sav1 = ((ord(c)- ord('a')+1) * Pow[j]) % mod
                res += sav1

                if binary_search(hashed,0, len(hashed)-1, res) != -1:
                    ans = True
                    break
                res -= sav1

                if ans:
                    break
            if ans:
                break
        if ans:
            break
        res += sav
    if ans:
        print("YES")
    else:
        print("NO")