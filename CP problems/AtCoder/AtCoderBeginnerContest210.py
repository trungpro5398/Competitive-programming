import sys
from sys import stdin


def A():
    n,a,x,y = map(int, input().split())
    print(min(n,a) * x + max(0, n-a)*y)

def B():
    n = input()
    s = input()
    res = True
    for i in range(0,len(s)):
        if s[i] == '1':
            if i % 2 == 1:
                res = False
                break
            else:
                break

    if res:
        print("Takahashi")
    else:
        print("Aoki")
from collections import defaultdict
def C():
    n, k = map(int, input().split())
    a = [int(x) for x in stdin.readline().split()]


    def countDistinct(arr, k, n):
        # Creates an empty hashmap hm
        mp = defaultdict(lambda: 0)

        # initialize distinct element
        # count for current window
        dist_count = 0

        # Traverse the first window and store count
        # of every element in hash map
        for i in range(k):
            if mp[arr[i]] == 0:
                dist_count += 1
            mp[arr[i]] += 1

        # Print count of first window

        res = dist_count
        # Traverse through the remaining array
        for i in range(k, n):

            # Remove first element of previous window
            # If there was only one occurrence,
            # then reduce distinct count.
            if mp[arr[i - k]] == 1:
                dist_count -= 1
            mp[arr[i - k]] -= 1

            # Add new element of current window
            # If this element appears first time,
            # increment distinct element count
            if mp[arr[i]] == 0:
                dist_count += 1
            mp[arr[i]] += 1

            # Print count of current window
            res = max(dist_count, res)
        print(res)



    countDistinct(a, k, n)

def D():
    h,w,c = map(int, input().split())
    a = list(map(int, input().split()))

    def cal(c, i, j, i1, j1):
        return c * (abs(i-i1) +(j-j1))

    d = [[0] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                d[i][j] = a[i][j]

D()
