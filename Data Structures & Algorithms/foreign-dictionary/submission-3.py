# a -> b -> c
# d -> e

# a: [b, c]
# b: [c]

        # a ---------------> b
        # \                  /
        #         c

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        al = {c: set() for word in words for c in word} # adj list 
        for i in range(len(words) - 1): 
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):  # invalid ordering if prefix comes after word
                return ""
            for j in range(minLen): 
                if w1[j] != w2[j]: 
                    al[w1[j]].add(w2[j])
                    break
        visited = set()
        path = set()
        res = []
        def dfs(c): # returns True if cycle exists, else False
            if c in path: # check this before checking visited
                return True
            if c in visited: 
                return False
            visited.add(c)
            path.add(c)
            for neighbor in al[c]: 
                if dfs(neighbor): 
                    path.remove(c)
                    return True
            path.remove(c)
            res.append(c)
            return False
        for c in al: 
            if c not in visited and dfs(c): 
                return ""
        res.reverse()
        return "".join(res)

        
