# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        d = collections.deque()
        d.append(root)
        res = []
        while len(d) > 0: 
            toAppend = []
            for _ in range(len(d)): 
                popped = d.popleft()
                toAppend.append(popped.val)
                if popped.left: d.append(popped.left)
                if popped.right: d.append(popped.right)
            res.append(toAppend)
        return res