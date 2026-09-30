# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(root): 
            if not root: 
                return True, 0
            lbalanced, lheight = recurse(root.left)
            rbalanced, rheight = recurse(root.right)
            balanced = abs(lheight - rheight) <= 1
            return lbalanced and rbalanced and balanced, 1 + max(lheight, rheight)
        return recurse(root)[0]
