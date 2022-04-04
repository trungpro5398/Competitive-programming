def get_z_value(pattern, Z):
    n = len(pattern)
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = Z[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        Z[i] = j

def lsp(pattern, Z):

    get_z_value(pattern, Z)
    n = len(pattern)
    # This is finding long proper suffix from left to right
    # i = 1
    # Z1 = [0 for i in range(n)]
    # while i < n:
    #     r = Z[i] - 1
    #     temp = copy.deepcopy(Z[i])
    #     if r <= 0:
    #         Z1[i] = max(temp, Z1[i])
    #         i += 1
    #         continue
    #     Z1[i + r] = max(temp, Z1[i+r])
    #     Z[i] = 0
    #
    #     i += 1

    return Z

while True:
    s = input()
    if '*' in s:
        break
    l = len(s)
    res = 1
    Z = [0] * len(s)
    lsp(s, Z)
    k = l - Z[l-1]
    if k < l and l % k == 0:
        res = l // k

    print(res)