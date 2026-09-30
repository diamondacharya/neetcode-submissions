# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def recurse(root): 
            nonlocal res
            if not root: 
                return -1
            lmax = recurse(root.left)
            rmax = recurse(root.right)
            wrappedLen = lmax + rmax + 2
            res = max(res, wrappedLen)
            return 1 + max(lmax, rmax)
        recurse(root)
        return res