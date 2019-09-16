#To check if one string is a rotation of another by calling isSubstirng method only once

def checkRotation(og, rot):
    if (len(og) == len(rot)):
        newString = og + og                 # concatenate the string to it self so that the rotation is a substring
        return isSubstring(newString, rot)
    return False

def isSubstring(string, subString):
    return subString in string

print(checkRotation("abcddfdsf", "ddfdsfabc"))