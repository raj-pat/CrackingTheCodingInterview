# To check if the permutation of the string can be a palindrome

def checkPermutationPalindrome(word):
    freqTable = {}  # dictionary
    Odd = set()  # Set
    for letter in word:
        freqTable[letter] = freqTable[letter] + 1 if letter in freqTable.keys() else 1
        if freqTable[letter] % 2 != 0:
            Odd.add(letter)
        else:
            if letter in Odd:
                Odd.remove(letter)
    if len(freqTable) == 1:
        return True
    if len(word) % 2 == 0 and len(Odd) == 0:  # if even then there should be only one odd letter
        return True
    elif len(Odd) == 1:
        return True
    else:
        return False


print(checkPermutationPalindrome("bbaaaakkggjj"))
