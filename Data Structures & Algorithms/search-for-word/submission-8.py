class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def dfs(row, col): 
            if len(path) == len(word): 
                return True
            if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1 or (row, col) in path: 
                return False    
            if board[row][col] != word[len(path)]: 
                return False
            path.add((row, col))
            res = dfs(row + 1, col) or dfs(row - 1, col) or dfs(row, col + 1) or dfs(row, col - 1)
            path.remove((row,col))
            return res
        for row in range(len(board)): 
            for col in range(len(board[0])):
                if board[row][col] == word[0] and dfs(row, col): 
                    return True
        return False
