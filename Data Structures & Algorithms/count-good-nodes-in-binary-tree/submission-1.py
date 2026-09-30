# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def recursive(root, maxval): 
            nonlocal res
            if not root: 
                return
            if root.val >= maxval: 
                res += 1
            recursive(root.left, max(root.val, maxval))
            recursive(root.right, max(root.val, maxval))
        recursive(root, float('-inf'))
        return res
            
        