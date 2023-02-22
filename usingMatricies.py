from Matrix import matrix
if "y" == input("Would you like to make matricies from here?").lower():
    while True:
        try:
            numMatricies = int(input("Number of matricies: "))
            break
        except:
            print("Invalid input!")
    matricies = []
    for matrixNum in range(numMatricies):
        print(f"Matrix #{matrixNum}")
        while True:
            try:
                rows, cols = int(input("Number of columns: ")),int(input("Number of columns: "))
                break
            except:
                print("Invalid Inputs")
        mtx = []
        currentRow = []
        for rowNumber in range(rows):
            for colNumber in range(cols):
                currentRow.append(int(input(f"Enter element {rowNumber}-{colNumber}: ")))
            mtx.append(currentRow)
            currentRow = []
        matricies.append(matrix(mtx))

# definition of a matrix
matrix1 = matrix([
    [-1,2],
    [1,3]
    ])
print(matrix1**3)
# for rowNum in range(matrix1.rows):
#     row = []
#     for colNum in range(matrix1.columns):
#         print(f"Row: {rowNum} Col: {colNum}")
#         row.append(matrix1.cofactor(rowNum,colNum))
#     print(row)
