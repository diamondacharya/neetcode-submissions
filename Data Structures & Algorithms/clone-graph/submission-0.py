"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}  # maps old nodes to new nodes
        def dfs(old): 
            if old in oldtonew: 
                return oldtonew[old]
            new = Node(old.val)
            oldtonew[old] = new
            for neighbor in old.neighbors: 
                new.neighbors.append(dfs(neighbor))
            return new
        return dfs(node) if node else None