# Rotate "square" matrix 90 degrees, let's do counterclock wise
# A 6*6 matrix I printed to make it easier for me to
# The approach is to start with the outer boundary first and then reach the center
# (0 , 0) | (0 , 1) | (0 , 2) | (0 , 3) | (0 , 4) | (0 , 5) |
# (1 , 0) | (1 , 1) | (1 , 2) | (1 , 3) | (1 , 4) | (1 , 5) |
# (2 , 0) | (2 , 1) | (2 , 2) | (2 , 3) | (2 , 4) | (2 , 5) |
# (3 , 0) | (3 , 1) | (3 , 2) | (3 , 3) | (3 , 4) | (3 , 5) |
# (4 , 0) | (4 , 1) | (4 , 2) | (4 , 3) | (4 , 4) | (4 , 5) |
# (5 , 0) | (5 , 1) | (5 , 2) | (5 , 3) | (5 , 4) | (5 , 5) |

# (0 , 0) | (0 , 1) | (0 , 2) | (0 , 3) | (0 , 4) | (0 , 5) | Top (i,j)
# (5 , 0) | (4 , 0) | (3 , 0) | (2 , 0) | (1, 0)  | (0 , 0) | Left ((len-j,i)
# (5 , 5) | (5 , 4) | (5 , 3) | (5 , 2) | (5 , 1) | (5 , 0) | Bottom (len-i, len-j)
# (0 , 5) | (1 , 5) | (2 , 5) | (3 , 5) | (4 , 5) | (5 , 5) | Right  (j, len-i)
# (0 , 0) | (0 , 1) | (0 , 2) | (0 , 3) | (0 , 4) | (0 , 5) | Top


def rotateCounter(matrix):
    size = len(matrix[0]) - 1

    for i in range(0, int(size)):
        for j in range(i, size - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][size - i]  # Top = Right
            temp2 = matrix[size - j][i]
            matrix[size - j][i] = temp          # Left = Top
            temp = matrix[size - i][size - j]
            matrix[size - i][size - j] = temp2  # Bottom = left
            matrix[j][size - i] = temp          # Right = Bottom
            print(str(i) + str(j), end="")
        print("\n")
    for line in matrix:
        print(line)


matrix = [[1, 2, 3, 4, 5, 6],
          [7, 8, 9, 10, 11, 12],
          [13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29, 30],
          [31, 32, 33, 34, 35, 36]]
rotateCounter(matrix)
