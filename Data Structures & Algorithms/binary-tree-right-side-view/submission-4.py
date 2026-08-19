# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while len(q) > 0: 
            levelSize = len(q)
            for i in range(levelSize): 
                node = q.popleft()
                if i == levelSize - 1: 
                    res.append(node.val)
                if (node.left): 
                    q.append(node.left)
                if (node.right): 
                    q.append(node.right)
        return res
