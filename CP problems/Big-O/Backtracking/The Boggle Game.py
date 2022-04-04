# import copy
#
# mat1 = [[0 for _ in range(4)] for _ in range(4)]
# mat2 = [[0 for _ in range(4)] for _ in range(4)]
# vis = [[0 for _ in range(4)] for _ in range(4)]
# dx = [-1,0,1,-1,1,-1,0,1]
# dy = [-1,-1,-1,0,0,1,1,1]
#
# def check(s):
#     cnt = 0
#     for i in s:
#         if i == "A" or i == "E" or i == "O" or i == "U" or i == "I" or i == "Y":
#             cnt += 1
#     return cnt
#
# def dfs(i, j, mat, string, res):
#     string.append(mat[i][j])
#
#     if len(string) == 4:
#         str1 = copy.deepcopy(string)
#
#         if check(str1) == 2:
#
#             res.append(str1)
#         string.pop(3)
#         return
#
#     vis[i][j] = 1
#     for k in range(8):
#         x = dx[k] + i
#         y = dy[k] + j
#         if x < 0 or y < 0 or x >= 4 or y >= 4 :
#             continue
#
#         if vis[x][y] == 0:
#             dfs(x, y, mat, string, res)
#     vis[i][j] = 0
#     string.pop(len(string)-1)
# while True:
#
#     for i in range(4):
#         s = input()
#
#         s = s.replace(" ", "")
#         if s[0] == '#':
#             exit()
#         for j in range(4):
#             mat1[i][j] = s[j]
#         l = 0
#         for j in range(4, 8):
#             mat2[i][l] = s[j]
#             l += 1
#     res1 = []
#     res2 = []
#     string1  = []
#     string2 = []
#
#     for i in range(4):
#         for j in range(4):
#             dfs(i, j, mat1, string1, res1)
#             dfs(i, j, mat2, string2, res2)
#     res = []
#
#     for i in res1:
#         for j in res2:
#            if i == j:
#                res.append(i)
#     if len(res) == 0:
#         print("There are no common words for this pair of boggle boards.")
#     else:
#         res.sort()
#         ans = []
#         for i in res:
#             if i not in ans:
#                 ans.append(i)
#             else:
#                 continue
#             for j in i:
#                 print(j, end ="")
#             print()
#     print()
#
#
#     input()
VOWELS = "AEOYIU"
DIRs = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
start = True


def count_vowels(word):
    res = 0
    for w in word:
        if w in VOWELS:
            res += 1
    return res


def find_words(board, x, y, cur_word, visited, found_words):
    if len(cur_word) == 4:
        if count_vowels(cur_word) == 2:
            found_words.add(cur_word)
        return

    visited[x][y] = True
    for d in DIRs:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
            new_cur_word = cur_word + board[nx][ny]
            find_words(board, nx, ny, new_cur_word, visited, found_words)
    visited[x][y] = False


def solve():
    global start

    board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(2)]

    if not start:
        input()

    for i in range(4):
        line = list(input().split())
        if line[0] == '#':
            exit()
        for j in range(8):
            board[j >> 2][i][j & 3] = line[j]

    if not start:
        print()
    start = False

    visited = [[False for _ in range(4)] for _ in range(4)]
    words = [set() for _ in range(2)]

    for board_id in [0, 1]:
        for i in range(4):
            for j in range(4):
                cur_word = ""
                cur_word += board[board_id][i][j]
                find_words(board[board_id], i, j, cur_word, visited, words[board_id])

    common_words = list()
    for word in words[0]:
        if word in words[1]:
            common_words.append(word)

    common_words.sort()
    if len(common_words) == 0:
        print("There are no common words for this pair of boggle boards.")
    else:
        for word in common_words:
            print(word)


if __name__ == "__main__":
    while True:
        solve()