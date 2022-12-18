class matrix(): # Just a simple cheat sheet for the first half of Lin alg 1
    def __init__(self,matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def calcEntry(self,m2,row,column):
        sum = 0
        for idx in range(self.columns): # Sums the product of all elements in the row and column 
            print(row,column)
            sum += self.matrix[row][idx] * m2.matrix[idx][column]
        return sum

    def __mul__(self,m2):
        # m1 * m2
        if self.columns != m2.rows: # Ensures it's a legal Multiplication
            raise ValueError
        dimensions = (self.rows, m2.columns)
        resultMat = []
        for rowNum in range(dimensions[0]): # Calls the calcEntry method for each cell of the new matrix and adds it to resultMat
            row = []
            for columnNum in range(dimensions[1]):
                row.append(self.calcEntry(m2,rowNum,columnNum))
            resultMat.append(row)
        return resultMat


    def __add__(self,m2):
        # m1 + m2
        if not(self.rows == m2.rows and self.columns == m2.columns): # Ensures it's a legal addition
            raise ValueError
        newMat = []
        for rowNum in range(self.rows): # Adds all coresponging entries in the matricies and enters them into newMat
            row = []
            for columnNum in range(self.columns):
                row.append(self.matrix[rowNum][columnNum] + m2.matrix[rowNum][columnNum])
            newMat.append(row)
        return newMat

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
        if self.rows == 2: # Base case when matrix is square
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        for columnNum,entry in enumerate(self.matrix[0]): # Sums the cofactor expansion for each element in the top row
            sum += sign*entry* self.subMatrix(0,columnNum).det()
            sign *= -1
        return sum

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
                out = out + str(self.matrix[rowNum][columnNum])+ " | "
            out = out + "\n"
        return out


matA = matrix([[1,2,3],[4,5,6]])
matB = matrix([[1,2],[3,4],[5,6]])
matC = matrix([[1,2,3],[4,5,6]])
matD = matrix([[5,4],[3,2]])
matE = matrix([[1,2,3],[4,5,6],[7,8,9]])
matF = matrix([[2,0,0],[0,2,0],[0,0,2]])
print(matA)