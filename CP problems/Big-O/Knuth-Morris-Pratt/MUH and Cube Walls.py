
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
    Z1 = [0 for i in range(n)]
    for j in range(n - 1, 0, -1):
        i = j + Z[j] - 1
        Z1[i] = Z[j]
    return Z1
def patternMatching(txt, pat):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0  # index for pat[]
    lps = lsp(pat, lps)
    i = 0
    cnt = 0
    ans = []
    while i < N and j < M:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            ans.append(i-j)
            cnt += 1
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return len(ans)
n, w = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = []
for i in range(n - 1):
    x = a[i + 1] - a[i]
    A.append(x)
B = []
for i in range(w - 1):
    x = b[i + 1] - b[i]
    B.append(x)

if len(B) == 0:
    print(n)
else:

    print(patternMatching(A,B))


