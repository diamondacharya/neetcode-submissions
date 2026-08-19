class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)): 
            s = set()
            for col in range(len(board[0])): 
                if board[row][col] in s: 
                    return False
                elif board[row][col] != '.': 
                    s.add(board[row][col])
        for col in range(len(board[0])): 
            s = set()
            for row in range(len(board)): 
                if board[row][col] in s: 
                    return False
                elif board[row][col] != '.': 
                    s.add(board[row][col])
        for r in range(3): 
            for c in range(3): 
                s = set()
                for row in range(3*r, 3*r + 3): 
                    for col in range(3*c, 3*c + 3): 
                        if board[row][col] in s: 
                            return False
                        elif board[row][col] != '.': 
                            s.add(board[row][col])
        return True