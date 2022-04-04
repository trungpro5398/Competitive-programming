def get_z_value(pattern, Z):

    n = len(pattern)
    j = 0
    for i in range(1,n):
        while j > 0 and pattern[i] != pattern[j]:
            j = Z[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        Z[i] = j
def lsp(pattern, Z):

    get_z_value(pattern, Z)
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


S = input()
Z = [0] * len(S)
lsp(S, Z)
dp = [0] * 1000004

for i in range(0,len(S)-1):
    dp[Z[i]] += 1

j = len(S)

res = False

while j > 0:
    j = Z[j-1]

    if j == 0:
        break
    if dp[j] > 0:
        print(S[0:j])
        res = True
        break
if not res:
    print("Just a legend")

