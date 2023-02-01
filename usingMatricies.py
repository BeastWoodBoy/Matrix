from Matrix import matrix

# definition of a matrix
matrix1 = matrix([
    [1,2,3,4],
    [5,6,7,4]
])
matrix2 = matrix([
    [5,6,7],
    [5,6,7],
    [3,4,5],
    [1,3,3]
])

print(matrix1*matrix1.transpose())