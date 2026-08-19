class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        al = {i: [] for i in range(n)}
        for a, b in edges: 
            al[a].append(b)
            al[b].append(a)
        def dfs(node): 
            if node in visited: 
                return
            visited.add(node)
            for neighbor in al[node]: 
                dfs(neighbor)
        count = 0
        visited = set()
        for node in range(n): 
            if node not in visited: 
                dfs(node)
                count += 1
        return count