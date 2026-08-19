class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def marky(row, col): 
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'O': 
                return
            board[row][col] = 'Y'
            marky(row + 1, col)
            marky(row - 1, col)
            marky(row, col + 1)
            marky(row, col - 1)
        # handle Os in first and last rows 
        for row in [0, len(board) - 1]: 
            for col in range(len(board[0])): 
                if board[row][col] == 'O': 
                    marky(row, col)
        # handle Os in first and last columns 
        for row in range(len(board)): 
            for col in [0, len(board[0]) - 1]: 
                if board[row][col] == 'O': 
                    marky(row, col)
        # mark all remaining Os as Xs and revert Ys back to Os
        for row in range(len(board)): 
            for col in range(len(board[0])): 
                if board[row][col] == 'O': 
                    board[row][col] = 'X'
                elif board[row][col] == 'Y': 
                    board[row][col] = 'O'
