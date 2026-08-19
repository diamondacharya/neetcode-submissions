class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for col in range(n)] for row in range(m)]
        for row in range(m): 
            arr[row][n - 1] = 1
        for col in range(n): 
            arr[m - 1][col] = 1
        for row in range(m - 2, -1, -1): 
            for col in range(n - 2, -1, -1): 
                arr[row][col] = arr[row + 1][col] + arr[row][col + 1]                
        return arr[0][0]

