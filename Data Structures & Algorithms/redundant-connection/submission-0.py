class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {node: [] for node in range(len(edges) + 1)} # n edges = n nodes (nodes are 1 through n)
        # return True if cycle is present in the graph constructed till now
        def dfs(node, parent):
            if visited[node]: 
                return True
            visited[node] = True
            for neighbor in adjList[node]: 
                if neighbor != parent and dfs(neighbor, node): 
                    return True
            return False
        for u, v in edges: 
            adjList[u].append(v)
            adjList[v].append(u)
            visited = [False] * (len(edges) + 1)
            if dfs(u, -1): 
                return [u, v]
        
