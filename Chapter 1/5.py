# The three edits problem: Given two strings, write a function to check if they are one edit away: Insert, Add, or Replace a character
# Pseudo
# Check the length of both words to determine what operation was performed


def oneEdit(word1, word2):
    if len(word1) > len(word2):
        longWord = word1
        shortWord = word2
    else:  # Else part will be executed if they're of the same length
        longWord = word2
        shortWord = word1
    if len(longWord) - 1 != len(shortWord):
        if (len(longWord) != len(shortWord)):
            return False  # more than one edit
    edits = 0
    for i in range(0, len(shortWord)):
        if (longWord[i] != shortWord[i]):
            edits += 1
            if edits == 2:
                return False
    try:  # Checking if the last letter exist in the longWord
        lastLetter = longWord[i + 1]
        edits += 1
        return True if edits == 1 else False
    except IndexError:
        return True


print(oneEdit("abaac", "akak"))
