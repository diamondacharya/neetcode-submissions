# our formula
# (row, col) --> (col, n - 1 - row) --> (n - 1 - row, n - 1 - col) --> (n - 1 - col, row) --> (row, col)
# (row, col) --> top left
# (col, n - 1 - row) --> top right
# (n - 1 - row, n - 1 - col) --> bottom right
# (n - 1 - col, row) --> bottom left

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2): 
            for j in range(i, n - 1 - i): 
                # save top left
                temp = matrix[i][j]
                # move bottom left to top left
                matrix[i][j] = matrix[n - 1 - j][i] 
                # move bottom right to bottom left
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # move top right to bottom right
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # move top left (temp) to top right
                matrix[j][n - 1 - i] = temp
