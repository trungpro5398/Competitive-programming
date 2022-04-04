import copy
import sys

a = []
while True:
    try:
        input_ = input()
        a.append(input_.replace(" ", ""))
    except EOFError:
        break


import re

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.isValid = False
        self.num = None

def solve(tokens):
    tokens = re.findall(re.compile('(-*\d+|[^ 0-9\n])'), tokens)
    root = None
    I = None
    res = []
    for token in tokens:
        if token == '(':
            n = Node()
            if len(res) > 0:
                if res[-1].left == None:
                    res[-1].left = n
                else:
                    res[-1].right = n
            else:
                root = n
            res.append(n)
        elif token == ')':
            res.pop(-1)
            if len(res) == 0:
                yield I, root
                root = None
                I = None
        else:
            if len(res) == 0:
                I = int(token)
            else:
                res[-1].isValid = True
                res[-1].num = int(token)
    return
def dfs(I, root, current ):
    sum = current
    if not root:
        return False
    if root.isValid:
        sum += root.num
        if root.left.isValid == root.right.isValid == False:
            return sum == I
        if dfs(I, root.left, sum):
            return True
        return dfs(I, root.right, sum)

s1 = ""
for s in a:
    s1 += s

for I, root in solve(s1):
    if dfs(I, root, 0):
        print('yes')
    else:
        print('no')
