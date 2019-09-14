import sys


# Unique character in a string without using any other data structure

def uniqueCharacter(word):
    ascii = [None] * 256  # size is 256 for ASCII
    for char in word:
        if ascii[ord(char)] == None:
            ascii[ord(char)] = 1
        else:
            return False
    return True


print(uniqueCharacter((sys.argv[1])))
