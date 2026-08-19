class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        al = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):  # populate adjacency list
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2): # invalid if prefix comes before word
                return ""
            for j in range(minLen): 
                if w1[j] != w2[j]: 
                    al[w1[j]].add(w2[j])
                    break
        visited = set()
        path = set()
        res = []
        def dfs(char): # return true if cycle exists
            if char in path: 
                return True
            if char in visited: 
                return False
            path.add(char)
            visited.add(char)
            for neighbor in al[char]: 
                if dfs(neighbor): 
                    return True
            res.append(char)
            path.remove(char)
        for c in al: 
            if c not in visited and dfs(c): 
                return ""
        res.reverse()
        return "".join(res)
        

