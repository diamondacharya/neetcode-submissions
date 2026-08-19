class Solution:
    # word="SEE"
    # board=
    # [
    # ["A","B","C","E"],
    # ["S","F","C","S"],
    # ["A","D","E","E"]
    # ]
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        path = set()
        def dfs(i, j): 
            if len(path) == len(word): 
                return True
            if i < 0 or i > R - 1 or j < 0 or j > C - 1 or (i, j) in path or board[i][j] != word[len(path)]: 
                return False
            path.add((i, j))
            res = dfs(i - 1, j) or dfs(i + 1, j) or dfs(i, j - 1) or dfs(i, j + 1)
            path.remove((i, j))
            return res
        for i in range(R): 
            for j in range(C): 
                if board[i][j] == word[0] and dfs(i, j): 
                    return True
        return False
