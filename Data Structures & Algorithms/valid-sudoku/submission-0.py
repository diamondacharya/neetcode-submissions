class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)): 
            seen = set()
            for col in range(len(board[0])): 
                if board[row][col] in seen: 
                    return False
                if board[row][col] != '.': 
                    seen.add(board[row][col])
        for col in range(len(board[0])): 
            seen = set()
            for row in range(len(board)): 
                if board[row][col] in seen: 
                    return False
                if board[row][col] != '.': 
                    seen.add(board[row][col])
        for block_row in range(3): 
            for block_col in range(3): 
                seen = set()
                for i in range(3): 
                    for j in range(3): 
                        row = block_row * 3 + i
                        col = block_col * 3 + j
                        if board[row][col] in seen: 
                            return False
                        if board[row][col] != '.': 
                            seen.add(board[row][col])
        return True
                        