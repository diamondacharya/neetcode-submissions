class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [] # keeps track of the valid path
        cols = set()
        posDiagonals = set() # indexed by unique (r + c) values
        negDiagonals = set() # indexed by unique (r - c) values
        def dfs(row): 
            if row == n: 
                res.append(board[:]) # append a COPY
                return
            for col in range(n): # go through every cell in that row
                if col in cols or (row + col) in posDiagonals or (row - col) in negDiagonals: # skip
                    continue
                board.append("".join(['Q' if c == col else '.' for c in range(n)]))
                cols.add(col)
                posDiagonals.add(row + col)
                negDiagonals.add(row - col)
                dfs(row + 1)
                cols.remove(col)
                posDiagonals.remove(row + col)
                negDiagonals.remove(row - col)
                board.pop()
        dfs(0)
        return res