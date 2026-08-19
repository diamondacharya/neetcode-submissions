#             0
#         /   |     \
#         1   2      3
#        /
#       4
# visited = (0, 1, )
# dfs(0, None)
#     dfs(1, 0)
#         dfs(0, 1)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = {i: [] for i in range(n)}
        visited = set()
        for edge in edges: 
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        def dfs(node, prev): 
            if node in visited: 
                return False
            visited.add(node)
            for neighbor in d[node]: 
                if (neighbor != prev) and (not dfs(neighbor, node)): 
                    return False
            return True
        return dfs(0, None) and n == len(visited)
            
        