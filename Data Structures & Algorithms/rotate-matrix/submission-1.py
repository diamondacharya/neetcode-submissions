# 1   2   3   4   5   
# 6   7   8   9   10
# 11  12  13  14  15
# 16  17  18  19  20
# 21  22  23  24  25

# (0, 0) --> (0, 2)
# (0, 1) --> (1, 2)
# (0, 2) --> (2, 2)
# (1, 0) -->  (0, 1)

# n - 1 - (n - 1 - r)
# r
# n - 1 - (n - 1 - c) = c

# (r, c) [top-left] --> 
# (c, n - 1 - r) [top-right] --> 
# (n - 1 - r, n - 1 - c) [bottom-right]--> 
# (n - 1 - c, r) [bottom-left]--> 
# (r, c)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2): 
            for j in range(i, n - 1 - i): 
                topLeft = matrix[i][j]
                temp = topLeft
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp
        