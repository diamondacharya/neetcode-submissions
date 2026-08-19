class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRowZero = False
        for row in range(len(matrix)): 
            for col in range(len(matrix[0])): 
                if matrix[row][col] == 0: 
                    matrix[0][col] = 0 
                    if row == 0: 
                        firstRowZero = True 
                    else: 
                        matrix[row][0] = 0
        for row in range(1, len(matrix)): 
            for col in range(1, len(matrix[0])): 
                if matrix[0][col] == 0 or matrix[row][0] == 0: 
                    matrix[row][col] = 0
        if matrix[0][0] == 0:   # process first column
            for row in range(len(matrix)): 
                matrix[row][0] = 0
        if firstRowZero == True: # process first row
            for col in range(len(matrix[0])): 
                matrix[0][col] = 0
        
        