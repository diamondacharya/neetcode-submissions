# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = collections.deque()
        q.append(root)
        res = []
        while q: 
            toAppend = []
            for _ in range(len(q)): 
                popped = q.popleft()
                toAppend.append(popped.val)
                if (popped.left): q.append(popped.left)
                if (popped.right): q.append(popped.right)
            res.append(toAppend)
        return res 
