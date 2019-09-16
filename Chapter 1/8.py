#For each zero in a matrix convert the entire row and coloumn to zero

matrix = [[9,2,3,4,5,6,7,8],[9,2,3,0,5,6,7,8],[8,2,3,4,5,8,7,8]]

def goRight(i, j, matrix):
    try:
        matrix[i][j] = 0
    except IndexError:
        return 
    goRight(i, j + 1, matrix)
   
def goLeft(i, j , matrix):
    try:
        matrix[i][j] = 0
    except IndexError:
        return 
    goLeft(i, j - 1, matrix)

def goUp(i, j , matrix):
    try:
        matrix[i][j] = 0
    except IndexError:
        return 
    goUp(i-1, j ,matrix)

def goDown(i, j , matrix):
    try:
        matrix[i][j] = 0
    except IndexError:
        return 
    goDown(i + 1,j, matrix)

def convertZero(matrix):
    zeroList = []
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] == 0:
                zeroList.append([i,j])
    for index in zeroList:
        goUp(index[0],index[1], matrix)
        goRight(index[0], index[1], matrix)
        goLeft(index[0],index[1], matrix)
        goDown(index[0],index[1], matrix)
    print(matrix)


convertZero(matrix)