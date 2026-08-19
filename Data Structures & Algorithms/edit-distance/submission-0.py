class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {} # caches values for dfs(i, j) subproblems 
        def dfs(i, j): 
            if i == len(word1): 
                return len(word2) - j
            if j == len(word2): 
                return len(word1) - i
            if (i, j) in cache: 
                return cache[(i, j)]
            if word1[i] == word2[j]: 
                cache[(i, j)] = dfs(i + 1, j + 1)
            else: 
                insert = 1 + dfs(i, j + 1) # match word2[j] by inserting
                delete = 1 + dfs(i + 1, j) # delete word1[i]
                replace = 1 + dfs(i + 1, j + 1) # replace word1[i] with word2[j]
                cache[(i, j)] = min(insert, delete, replace)
            return cache[(i, j)]
        return dfs(0, 0)