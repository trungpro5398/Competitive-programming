
def lower_bound(lst, num_search):
    l, r = 0, len(lst) - 1
    ans = -1

    while l <= r:
        m = ( l + r ) // 2
        if lst[m] == num_search:
            ans = m
            r = m - 1
        elif lst[m] > num_search:
            r = m - 1
        else:
            l = m + 1
    return ans