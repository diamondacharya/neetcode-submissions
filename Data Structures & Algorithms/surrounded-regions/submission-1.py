class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rowlen = len(board)
        collen = len(board[0])
        def dfs(row, col): 
            if row < 0 or row >= rowlen or col < 0 or col >= collen or board[row][col] != 'O': 
                return
            board[row][col] = 'Y'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        for row in range(rowlen): 
            dfs(row, 0)
            dfs(row, collen - 1)
        for col in range(collen): 
            dfs(0, col)
            dfs(rowlen - 1, col)
        for row in range(rowlen): 
            for col in range(collen): 
                if board[row][col] == 'Y': 
                    board[row][col] = 'O'
                elif board[row][col] == 'O': 
                    board[row][col] = 'X'
