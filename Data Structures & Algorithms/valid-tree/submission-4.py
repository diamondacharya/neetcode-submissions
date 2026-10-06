class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        for a, b in edges: 
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()
        path = set()
        # returns True if there is a cycle present
        def dfs(i, parent): 
            if i in path: 
                return True
            if i in visited: 
                return False
            path.add(i)
            visited.add(i)
            for neighbor in adjList[i]: 
                if neighbor != parent and dfs(neighbor, i): 
                    return True
            path.remove(i)
            return False
        if dfs(0, -1): 
            return False
        return len(visited) == n