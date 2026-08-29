class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowlen = len(board)
        collen = len(board[0])
        for i in range(rowlen): 
            seen = set()
            for j in range(collen): 
                if board[i][j] in seen: 
                    return False
                if board[i][j] != '.': 
                    seen.add(board[i][j])
        for j in range(collen): 
            seen = set()
            for i in range(rowlen): 
                if board[i][j] in seen: 
                    return False
                if board[i][j] != '.': 
                    seen.add(board[i][j])
        for rowblock in range(3): 
            for colblock in range(3): 
                seen = set()
                for x in range(3): 
                    for y in range(3): 
                        row = rowblock * 3 + x
                        col = colblock * 3 + y
                        if board[row][col] in seen: 
                            return False
                        if board[row][col] != '.': 
                            seen.add(board[row][col])
        return True
        

