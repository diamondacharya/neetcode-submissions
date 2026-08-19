class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        def dfs(r, c): 
            if len(path) == len(word): 
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in path or board[r][c] != word[len(path)]: 
                return False
            path.add((r, c))
            res = dfs(r - 1, c) or dfs(r + 1, c) or dfs(r, c - 1) or dfs(r, c + 1)
            path.remove((r, c))
            return res
        for r in range(rows): 
            for c in range(cols): 
                if board[r][c] and dfs(r, c): 
                    return True
        return False
