#For each zero in a matrix convert the entire row and coloumn to zero

listTest = [0,2,3,4,5,6,7,8]

def startRight(index, list):
    try:
        list[index] = 0
    except IndexError:
        return 
    startRight(index + 1, list)
   
def startLeft(index, list):
    try:
        list[index] = 0
    except IndexError:
        return 
    startLeft(index - 1, list)


def testMethod(listTest):
    startRight(4, listTest)
    startLeft(4, listTest)
    print(listTest)


testMethod(listTest)