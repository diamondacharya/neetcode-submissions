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
            for _ in range(len(q) - 1): 
                node = q.popleft()
                if (node.left): 
                    q.append(node.left)
                if (node.right): 
                    q.append(node.right)
            node = q.popleft()
            res.append(node.val)
            if (node.left): 
                q.append(node.left)
            if (node.right): 
                q.append(node.right)
        return res
