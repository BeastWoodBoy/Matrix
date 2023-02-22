from copy import deepcopy
class DimensionError(Exception):
    ...
class NotDefinedYet(Exception):
    ...
class matrix(): # Just a simple cheat sheet for the first half of Lin alg 1
    def __init__(self,matrix):
        if matrix != []:
            cols = len(matrix[0])
            for row in matrix:
                if len(row) != cols:
                    raise DimensionError
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def calcEntry(self,m2,row,column):
        sum = 0
        for idx in range(self.columns): # Sums the product of all elements in the row and column 
            sum += self.matrix[row][idx] * m2.matrix[idx][column]
        return sum

    def __mul__(self,m2):
        # m1 * m2
        if self.columns != m2.rows:
            return DimensionError
        resultMat = []
        if type(m2) in (int,float):
            for rowNum,_ in enumerate(self.matrix):
                newRow = []
                for entry in self.matrix[rowNum]:
                    newRow.append(entry * m2)
                resultMat.append(newRow)
        else:
            if self.columns != m2.rows: # Ensures it's a legal Multiplication
                raise ValueError
            dimensions = (self.rows, m2.columns)
            
            for rowNum in range(dimensions[0]): # Calls the calcEntry method for each cell of the new matrix and adds it to resultMat
                row = []
                for columnNum in range(dimensions[1]):
                    row.append(self.calcEntry(m2,rowNum,columnNum))
                resultMat.append(row)
        return matrix(resultMat)

    def __pow__(self,exponent): # Used to take exponents of matricies
        if exponent < 0:
            self = self.inverse()
            exponent = abs(exponent)
        newMat = deepcopy(self)
        for _ in range(exponent-1):
            newMat *= self
        return newMat
    def inverse(self): # Returns the unverse of a matrix; This is done using the adjoint/determinant method for the inverse
        determinant = self.det()
        adjoint = self.adjoint()
        invMat = []
        for rowNum in range(adjoint.rows):
            currentRow = []
            for elem in adjoint.matrix[rowNum]:
                currentRow.append(elem/determinant)
            invMat.append(currentRow)
        return matrix(invMat)
    def cofactor(self,rowNum,colNum): # Returns the cofactor of a cell given the matrix itself, and the row and column of the cell
        return (-1)**(rowNum+colNum) * (self.subMatrix(rowNum,colNum)).det()
    def adjoint(self): # Returnes the Adjoint Matrix given a matrix object; returned the transpose of the matrixs' cofactor matrix
        adjMat = []
        for rowNum in range(self.rows):
            row = []
            for colNum in range(self.columns):
                row.append(self.cofactor(rowNum,colNum))
            adjMat.append(row)
            row = []
        return matrix(adjMat).transpose()
    def __add__(self,m2): # Definition for the sum of a matrix and another matrix
        # m1 + m2
        if not(self.rows == m2.rows and self.columns == m2.columns): # Ensures it's a legal addition
            raise ValueError
        newMat = []
        for rowNum in range(self.rows): # Adds all coresponging entries in the matricies and enters them into newMat
            row = []
            for columnNum in range(self.columns):
                row.append(self.matrix[rowNum][columnNum] + m2.matrix[rowNum][columnNum])
            newMat.append(row)
        return matrix(newMat)

    def subMatrix(self, rowNumRmv,columnNumRmv): # Used for finding determinant as it requires 
        newMat = []
        for rowNum in range(self.rows): # Reconstructs the matrix excluding given row and column
            row = []
            for columnNum in range(self.columns):
                if not(rowNum == rowNumRmv or columnNum == columnNumRmv): # Responsible for exclusion
                    row.append(self.matrix[rowNum][columnNum])
            if rowNum != rowNumRmv:
                newMat.append(row)
        return matrix(newMat)

    def det(self): # Recursive algorithm for calculating determiannt using cofactor expansion method
        if self.rows != self.columns: # Ensures matrix is square
            raise ValueError
        sign = 1
        sum = 0
        if self.rows == 1: # Base case For 1x1 matricies
            return self.matrix[0][0]
        if self.rows == 2: # Base case when matrix is square
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        for columnNum,entry in enumerate(self.matrix[0]): # Sums the cofactor expansion for each element in the top row
            sum += sign*entry* self.subMatrix(0,columnNum).det()
            sign *= -1
        return sum
    def transpose(self):
        tp =[]

        for colNum,_ in enumerate(self.matrix[0]):
            row = []
            for r in self.matrix:
                row.append(r[colNum])
            tp.append(row)

        return matrix(tp)
    def trace(self): 
        trc = 0
        for diagonalIdx in range(min(self.rows,self.columns)): # Iterates through the idx pair for every diagonal element and adds it up
            trc += self.matrix[diagonalIdx][diagonalIdx]
        return trc

    def addColumns(self,m2): # Adds the columns of another matrix to the right of self
        if self.rows != m2.rows:
            raise DimensionError
        newMat = []
        for rowNum in range(self.rows):
            curRow = []
            for elem in self.matrix[rowNum]:
                curRow.append(elem)
            for elem in m2.matrix[rowNum]:
                curRow.append(elem)
            newMat.append(curRow)
        return matrix(newMat)

    def addRows(self,m2): # Adds the rows of another matrix to the bottom of self
        if self.columns != m2.columns:
            raise DimensionError
        newMat = []
        for row in self.matrix :
            newMat.append(row)
        for row in m2.matrix:
            newMat.append(row)
        return matrix(newMat)
        
            
    def __eq__(self,m2):
        if not(self.rows == m2.rows and self.columns == m2.columns): # Ensures dimensions are the same first to avoid indexing errors
            return False
        for rowNum in range(self.rows): # Checks for equality of every element in the 2 matricies
            for columnNum in range(self.columns):
                if self.matrix[rowNum][columnNum] != m2.matrix[rowNum][columnNum]:
                    return False
        return True

    def __str__(self): # Formats Matricies to make them easier to read
        out = ""

        for rowNum in range(self.rows):
            out = out + "| "
            for columnNum in range(self.columns):
                out = out + str(round(self.matrix[rowNum][columnNum],2))+ " | "
            out = out + "\n"
        return out
