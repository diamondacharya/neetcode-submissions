class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowlen = len(board)
        collen = len(board[0])
        for row in range(rowlen): 
            s = set()
            for col in range(collen): 
                if board[row][col] in s: 
                    return False
                if board[row][col] != '.': 
                    s.add(board[row][col])
        for col in range(collen): 
            s = set()
            for row in range(rowlen): 
                if board[row][col] in s: 
                    return False
                if board[row][col] != '.': 
                    s.add(board[row][col])
        for rowblock in range(3): 
            for colblock in range(3): 
                s = set()
                for i in range(3): 
                    for j in range(3): 
                        row = rowblock * 3 + i
                        col = colblock * 3 + j
                        if board[row][col] in s: 
                            return False
                        if board[row][col] != '.': 
                            s.add(board[row][col])
        return True
