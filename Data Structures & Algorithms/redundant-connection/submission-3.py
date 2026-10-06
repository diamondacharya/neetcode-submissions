class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {i + 1: [] for i in range(len(edges))}
        # path = set()
        # returns true if the graph has a cycle
        def dfs(i, parent, visited): 
            # if i in path: 
            #     return True
            if i in visited: 
                return True
            visited.add(i)
            # path.add(i)
            for neighbor in adjList[i]: 
                if neighbor != parent and dfs(neighbor, i, visited): 
                    return True
            # path.remove(i)
        for a, b in edges: 
            adjList[a].append(b)
            adjList[b].append(a)
            if dfs(a, -1, set()): 
                return [a, b]
