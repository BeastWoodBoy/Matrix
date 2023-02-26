from Matrix import matrix
def computeEquation(matricies,eq = ):
    equation = input("Enter equation> ")
    equation = equation.replace(" ","")
    
def showMatricies(matricies): # Returns a string with all info about a list of matricies
    printStmt = ""
    for idx,mtx in enumerate(matricies):
        printStmt += f"Matrix {idx+1}\n{mtx}\n"
    return printStmt
def newMat():
    while True: # Getting dimensions of the new matrix
        try:
            rowNum, colNum = int(input("Number of Rows> ")),int(input("Number of Columns> "))
            break
        except:
            print("Invalid Input!")
    newMat = []
    for r in range(rowNum):
        currentRow = []
        for c in range(colNum):
            while True:
                try:
                    currentRow.append(float(input(f"Value of {r+1}-{c+1}> ")))
                    break
                except:
                    print("Invalid Input")
        newMat.append(currentRow)
    return matrix(newMat)

def outerParentheses(expr):

    istart = []  # stack of indices of opening parentheses
    pairs = []

    for i, c in enumerate(expr):
        if c == '(':
            istart.append(i)
        if c == ')':
            try:
                if len(istart) <= 1:
                    pairs.append((istart.pop(), i))
                else:
                    istart.pop()
            except IndexError:
                raise Invalidexpression
    if istart:  # check if stack is empty afterwards
        raise Invalidexpression
    return pairs
# definition of a matrix
matricies = []
matrix1 = matrix([
    [1,0,0],
    [1,0,1],
    [0,1,0]
    ])
matricies.append(matrix1)
print("Command List\nq:quit\nn: enter new matrix\ns: show matricies\nd: delete matrix\ne: enter equation")
while True:
    command = input("> ").lower()
    if command == 'q':
        break
    elif command == 'n':
        matricies.append(newMat())
    elif command == 's':
        print(showMatricies(matricies))
    elif command == 'd':
        while True:
            try:
                delNum = int(input("Number of Matrix to delete> "))
                break
            except:
                print("Invalid Input")
        matricies.pop(delNum-1)
    elif command == 'e':
        print(computeEquation(matricies))

