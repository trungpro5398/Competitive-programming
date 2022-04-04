import copy
import sys

import bitarray


def fibonacciEncoding(n, right):
    # this code will start from the largest index of the fibonacci that f <= n
    code_word = [0] * (right+2)

    # additional '1' bit
    code_word[right + 1] = 1
    # this loop will break when n =0, this means we find a sum of one or more distinct Fibonacci numbers

    while n:

        # mark the index is 1
        code_word[right] = 1

        # Subtract this fibonacci at index from n
        n -= fib[right]

        # move to the left
        right -= 1

        # mark all index of Fibonacci > n as not used (0 bit),
        # move to the left
        while (right >= 0 and fib[right] > n):
            code_word[right] = 0
            right -= 1



    # return pointer to code_word
    return code_word


class nodeHuffan:
    def __init__(self, frequencies, c, leftNode = None, rightNode = None):
        # the frequencies of each unique character
        self.frequencies = frequencies
        # the unique character
        self.c = c
        # node left of current node
        self.leftNode = leftNode
        # node right of current node
        self.rightNode = rightNode
        # the bit of node 0 if the in the left, and 1 in the right
        self.bit = None


def getHuffanCodeWord(node, c):
    global dp
    # plus the current bit of this node to the string c

    c_1 = copy.deepcopy(c)
    if node.bit is not None:
        c_1.append(node.bit)

    # if node left not null move to the node left
    if node.leftNode:
        getHuffanCodeWord(node.leftNode, c_1)
    # if node right not null move to the node right
    if node.rightNode:
        getHuffanCodeWord(node.rightNode, c_1)
    # if both node are null, this is the final binary value of this char of this node
    if not node.rightNode and not node.leftNode:
        dp[ord(node.c)] = c_1


def huffan(nodes):

    while len(nodes) > 1:
        # sort the node following to the frequencies of each char
        nodes = sorted(nodes, key=lambda x: x.frequencies)

        l, r = nodes[0], nodes[1]
        # the small value is in the left node and set 0 bit
        # the large value is in the right node and set 1 bit
        l.bit = 0
        r.bit = 1
        # remove two of them of the array
        nodes.pop(0)
        nodes.pop(0)
        # create a new node represents the sum of frequencies of two node left and right
        combinedNode = nodeHuffan(l.frequencies + r.frequencies, l.c + r.c, l, r)

        # add new node to the array
        nodes.append(combinedNode)

    getHuffanCodeWord(nodes[0], [])


def writeOutput(bits):

    # Open output file with correct name
    with open('encodedBWT.bin', 'wb') as fh:
        bits.tofile(fh)


def readInput(txtFileName):
    # Open and read the text file
    txtFile = open(txtFileName, 'r')
    txt = txtFile.read()
    # Remember to close the file
    txtFile.close()

    return txt


def bisect_left(a, x, left, right):
    # This function returns the place in the sorted list where the number specified in the argument may be added
    # to keep the resultant list sorted. If the element already exists in the list,
    # the left most position  which it must be added is returned.
    while left < right:
        mid = (left + right) // 2
        if x <= a[mid]:
            right = mid
        else:
            left = mid + 1
    return right


if __name__ == '__main__':
    bits = bitarray.bitarray()
    global dp
    dp = [[]] * 127
    txtFileName = sys.argv[1]
    s = readInput(txtFileName)

    freq = [0] * 127
    nUniqChars = []
    frequencies = []
    # count the frequencies of each char
    for i in s:
        freq[ord(i)] += 1

    for i in range(0, 127):
        if freq[i] > 0:
            nUniqChars.append(chr(i))
            frequencies.append(freq[i])
    nodes = []
    # push both char and its frequency to the nodes
    for i in range(len(nUniqChars)):
        nodes.append(nodeHuffan(frequencies[i], nUniqChars[i]))

    # after this progress we will save the code word of each char in the dp array
    huffan(copy.deepcopy(nodes))
    maxN = 3
    a = 1
    b = 2
    c = 0
    # find the maximum index that when c > len(s) this loop will break
    while c <= len(s):
        c = a + b
        a = copy.deepcopy(b)
        b = c
        maxN += 1

    fib = [0 for i in range(maxN + 1)]
    fib[0] = 1
    fib[1] = 2
    i = 2
    # initialize the array fibonacci with max length is maxN
    # it will reduce the time in the next step when we find the fibonacci code word
    while fib[i - 1] <= len(s):
        fib[i] = fib[i - 1] + fib[i - 2]
        i += 1
    # use the bisect left that we created to find the lower bound of len(s) in the array fibonacci we create above
    # log(n) time complexity
    index = bisect_left(fib, len(s), 0, maxN)
    while fib[index] > len(s) or fib[index] == 0:
        index -= 1
    bits.extend( fibonacciEncoding(len(s), index))
    #print(maxN, fib[index], bits)
    index = bisect_left(fib, len(nUniqChars), 0, maxN)
    while fib[index] > len(nUniqChars) or fib[index] == 0:
        index -= 1
    bits.extend(fibonacciEncoding(len(nUniqChars), index))
    #print(fib[index], bits)
    for i in nodes:
        # convert char to ascii binary
        temp = str(bin(ord(i.c)))
        temp = temp[2:len(temp)]
        # if the binary length is less than 7 append 0 in the start until the length temp equal 7
        for j in range(len(temp), 7):
            temp = "0" + temp
        #print(bits, temp)
        for j in range(0, 7):
            if temp[j] == "0":
                bits.append(0)
            else:
                bits.append(1)
        # get the fibonacci code len
        index = bisect_left(fib, len(dp[ord(i.c)]), 0, maxN)
        while fib[index] > len(dp[ord(i.c)]) or fib[index] == 0:
            index -= 1
        bits.extend(fibonacciEncoding(len(dp[ord(i.c)]), index))
        # extend to bits huffman code of i.c
        bits.extend( dp[ord(i.c)])
        #print(bits,i, temp, fibonacciEncoding(len(dp[ord(i.c)]), index), dp[ord(i.c)])
    mark = [0] * 127
    for i in s:
        # if this char is marked, it will continue
        if mark[ord(i)]:
            continue
        mark[ord(i)] = 1
        # extend to bits huffman code of i.c
        bits.extend(dp[ord(i)])
        # get the fibonacci run len
        index = bisect_left(fib, freq[ord(i)], 0, maxN)
        while fib[index] > freq[ord(i)] or fib[index] == 0:
            index -= 1
        bits.extend(fibonacciEncoding(freq[ord(i)], index))
    #print(bits)
    writeOutput(bits)
