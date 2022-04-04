import copy
import sys

import bitarray


def bits2string(x):
    return ''.join(chr(int(x, 2)))


def decodeFibonacciWord(s, l):
    # this code will return the binary string to number in linear time
    # it will get the string s and l index
    a = 1
    b = 2
    lenWord = 0
    # it will run until s[l] == s[l+1] == "1". It is easy to see that
    # Fibonacci code words always have the same last 2 digits and are equal to 1
    while not (s[l] == s[l + 1] and s[l] == "1"):
        # it will plus to the lenWord if s[l] == "1"
        if s[l] == "1":
            lenWord += a
        c = a + b
        a = copy.deepcopy(b)
        b = c
        l += 1
    l += 2
    lenWord += a
    # return new l index and the number
    return l, lenWord


def writeOutput(result):
    # Open output file with correct name
    outputFile = open('decodedBWT.txt', 'w')
    # Iterate through the occurrence list and write results to an output file
    outputFile.write(result)
    # Remember to close the file
    outputFile.close()


def readInput(txtFileName):
    file = bitarray.bitarray()
    with open(txtFileName, 'rb') as fh:
        file.fromfile(fh)
    s = ""
    for i in file:
        s += str(i)
    return s


if __name__ == '__main__':

    txtFileName = sys.argv[1]
    s = readInput(txtFileName)
    l = 0
    lenBwt = 0
    # find the length of the string because in the encoder, we use FibonacciCode to find the binary
    # so we must decode it
    l, lenBwt = decodeFibonacciWord(s, l)
    nUniqChars = 0
    # find the number of the unique chars
    l, nUniqChars = decodeFibonacciWord(s, l)
#    dpCh = {}
    # This is the dictionary to save the char when we convert it from the binary, which the key value is huffan code of
    # it.
    dpBiCh = {}

    for i in range(0, nUniqChars):

        tempL = copy.deepcopy(l)
        l += 7
        # when we find the code len of the huffan code of this char by decode the fibonacci word
        l, temp = decodeFibonacciWord(s, l)
        #print(l, temp, s[l:l + temp])
#        dpCh[ord(bits2string(s[tempL:tempL + 7]))] = s[l:l + temp]
        # we will save the huffan code to dictionary with their char
        dpBiCh[s[l:l + temp]] = bits2string(s[tempL:tempL + 7])
        l += temp
    finalResult = ""
#    print(dpCh, dpBiCh)
    for i in range(0, nUniqChars):
        temp = ""
        temp += s[l]
        # in this step we will add char from left to right until the string made up of them is found in dictionary
        while temp not in dpBiCh:
            l += 1
            temp += s[l]
            # print(temp, l)
        l += 1
        # then we decode the run length, this step will find how many number of this char in the string
        l, secondTemp = decodeFibonacciWord(s, l)
        #print(l, secondTemp)
        # plus all occurrence of this string
        for j in range(0, secondTemp):
            finalResult += dpBiCh[temp]
    #print(finalResult)
    writeOutput(finalResult)
