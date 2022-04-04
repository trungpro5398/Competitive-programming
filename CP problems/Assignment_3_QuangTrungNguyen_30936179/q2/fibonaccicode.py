# Returns pointer to the char string which
# corresponds to code for n

import copy
import sys


def fibonacciEncoding(n, right):
    # this code will start from the largest index of the fibonacci that f <= n
    code_word = ['0'] * (right + 2)

    # this loop will break when n =0, this means we find a sum of one or more distinct Fibonacci numbers

    # additional '1' bit
    code_word[index + 1] = '1'
    while n:

        # mark the index is 1
        code_word[right] = '1'

        # Subtract this fibonacci at index from n
        n -= fib[right]

        # move to the left
        right -= 1

        # mark all index of Fibonacci > n as not used (0 bit),
        # move to the left
        while (right >= 0 and fib[right] > n):
            code_word[right] = '0'
            right -= 1

    # return pointer to code_word
    return "".join(code_word)


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

    a = 1
    b = 2
    c = 0

    maxN = 3
    n = int(sys.argv[1])
    while c <= n:
        c = a + b
        a = copy.deepcopy(b)
        b = c
        maxN += 1

    fib = [0 for i in range(maxN + 1)]
    fib[0] = 1
    fib[1] = 2
    i = 2
    while fib[i - 1] <= n:
        fib[i] = fib[i - 1] + fib[i - 2]
        i += 1
    for i in range(1, n + 1):
        index = bisect_left(fib, i, 0, maxN)
        while fib[index] > i:
            index -= 1
        print("{} {}".format(i, fibonacciEncoding(i, index)))
