
import sys

# Quang Trung Nguyen ID:30936179
def readInput(txtFileName, patFileName):
    # Open and read the text file
    txtFile = open(txtFileName, 'r')
    txt = txtFile.read()
    # Remember to close the file
    txtFile.close()
    # Open and read the pattern file
    patFile = open(patFileName, 'r')
    pat = patFile.read()
    # Remember to close the file
    patFile.close()

    return txt, pat


def writeOutput(occurrences):
    # Open output file with correct name
    outputFile = open('output_modkmp_5.txt', 'w')
    # Iterate through the occurrence list and write results to an output file
    outputFile.write(str(occurrences[0] + 1))
    for i in range(1, len(occurrences)):
        outputFile.write('\n')
        outputFile.write(str(occurrences[i] + 1))
    # Remember to close the file
    outputFile.close()


def charToInt(ch):
    return ord(ch)


def getDelta(pat):
    dp = [0] * 257
    # get delta just a way to set the location of each character existing in pattern to 0
    # for exampl pat = "abcabc", we have the char "a", so all the occurence of a will set 0
    # => 011011
    # this for run all char in asscii 2
    for i in range(0, 257):
        res = 0
        for j in range(len(pat) - 1, -1, -1):
            temp = charToInt(pat[j])
            if i != temp:
                res |= 1

            if j > 0:
                res <<= 1
        # which this char we have the bit respectively in the pattern
        # it will be easy to get the detla in O(1) when we find bitvector
        dp[i] = res

    return dp


def getBitVector(txt, pat):
    bitVector = [0] * len(txt)
    delta = getDelta(pat)
    lenPat = len(pat) - 1 # cuz like when find the 1 char, the total length that we want to find to decrease 1 unit
    cnt = []
    temp = ~(1 << lenPat)
    temp1 = 1 << (lenPat + 1)
    temp2 = (1 << lenPat)
    for i in range(0, len(txt)):
        if i == 0: # bitvector0
            bitVector[i] = temp1
            bitVector[i] -= 1
            if txt[0] == pat[0]:
                bitVector[i] ^= 1
        else:
            # why we need bitVector[i-1] & ~(1 << lenPat) here
            # i will give an example to make easily to understand
            # we have bitVector[7] = 10101 when we shift left 1, it will be 101010
            # but we want 01010 instead 101010. So before we shift left 1 bit
            # we should 10101 & ( ~(1 << lenPat)) = 10101 & ( ~(1 << 5)) = 10101 & 01111 = 0101
            # then 0101 << 1 = 01010
            bitVector[i] = ((bitVector[i - 1] & temp) << 1) | delta[charToInt(txt[i])]
        # it is easy to see that if the first bit of bitvector is 0 this mean the pat from [1...lenPat] == txt[i... i + lenpat]
        # so all bitvector[i] is less than (1<<lenPat), so i location will be the location of the last suffix
        # we must return the location of first prefix so i - lenPat
        if bitVector[i] < temp2:
            cnt.append(i - lenPat)
    return cnt


if __name__ == '__main__':
    txtFileName = sys.argv[1]
    patFileName = sys.argv[2]
    txt, pat = readInput(txtFileName, patFileName)
    occurrences = getBitVector(txt, pat)
    writeOutput(occurrences)
