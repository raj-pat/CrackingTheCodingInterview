# replace spaces with %20 in the same string don't use a different string or stringbuilder
# for ex: Raj_Patel_26____ >> Raj%20Patel%20
# Can be done in one scan if sufficient space is given Else
# the approach is to count the spaces between words and then adding two more spaces at the end for each space counted
# for our solution we will assume the spaces isn't given
import sys


def URLify(sentence):
    spacesToAdd = 0
    sentence = sentence.strip()
    for letter in sentence:
        if (letter == ' '):
            spacesToAdd += 2
    k = len(sentence) - 1
    sentence += (' ' * spacesToAdd)
    j = len(sentence) - 1
    sentence = list(sentence)  # strings are immutable in python
    # print(sentence)
    for i in range(k, 0, -1):
        if (sentence[i] == ' '):
            sentence[j] = '0'
            j -= 1
            sentence[j] = '2'
            j -= 1
            sentence[j] = '%'
            j -= 1
        else:
            if i == j:
                break
            sentence[j] = sentence[i]
            sentence[i] = ' '
            j -= 1
    return ''.join(sentence)


print(URLify(sys.argv[1]))
