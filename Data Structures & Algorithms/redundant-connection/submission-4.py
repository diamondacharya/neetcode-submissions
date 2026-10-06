class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {i + 1: [] for i in range(len(edges))}
        def dfs(i, parent, visited): 
            if i in visited: 
                return True
            visited.add(i)
            for neighbor in adjList[i]: 
                if neighbor != parent and dfs(neighbor, i, visited): 
                    return True
        for a, b in edges: 
            adjList[a].append(b)
            adjList[b].append(a)
            if dfs(a, -1, set()): 
                return [a, b]
