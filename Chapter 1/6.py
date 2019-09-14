# Compress the String: If string = aaaaabbbbbccaabb then return a5b5c2a2b2

def compress(word):
    lastLetter = word[0]
    newWord = []
    counter = 1
    for i in range(1, len(word)):
        if lastLetter == word[i]:
            counter += 1
        else:
            newWord.append(lastLetter)
            newWord.append(str(counter))
            counter = 1
            lastLetter = word[i]
    newWord.append(lastLetter)
    newWord.append(str(counter))

    return ''.join(newWord)


print(compress("aaaabbbbdddfgggggdssaaa"))
