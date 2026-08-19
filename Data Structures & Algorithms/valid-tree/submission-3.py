class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}        
        for a, b in edges: 
            adjList[a].append(b)
            adjList[b].append(a)
        path = set() # to help with cycle detection
        visited = set()
        def cyclePresent(i, parent): 
            if i in path: 
                return True
            path.add(i)
            visited.add(i)
            for neighbor in adjList[i]: 
                if neighbor != parent and cyclePresent(neighbor, i): 
                    return True
            path.remove(i)
        if cyclePresent(0, -1): 
            return False
        if len(visited) != n: 
            return False
        return True
