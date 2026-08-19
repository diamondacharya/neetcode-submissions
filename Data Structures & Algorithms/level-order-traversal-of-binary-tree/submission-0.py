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
        ret = []
        d = collections.deque()
        d.append(root)
        while len(d) > 0: 
            toAppend = []
            for _ in range(len(d)): 
                root = d.popleft()
                toAppend.append(root.val)
                if root.left: 
                    d.append(root.left)
                if root.right: 
                    d.append(root.right)
            ret.append(toAppend)
        return ret
