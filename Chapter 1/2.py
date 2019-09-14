# check permutation in two string
import sys


def checkPermutation(word1, word2):
    letters = [0] * 128
    if (len(word1) != len(word2)): return False
    for letter in word1:
        letters[ord(letter)] += 1
    for letter in word2:
        letters[ord(letter)] -= 1
        if (letters[ord(letter)] < 0):
            return False
    return True


print(checkPermutation(sys.argv[1], sys.argv[2]))
