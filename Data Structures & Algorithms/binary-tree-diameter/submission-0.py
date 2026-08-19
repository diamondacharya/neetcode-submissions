# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(root): 
            nonlocal res
            if not root: 
                return -1
            lheight = dfs(root.left)
            rheight = dfs(root.right)
            wrappedLen = lheight + 1 + rheight + 1
            res = max(res, wrappedLen)
            return max(lheight + 1, rheight + 1)
        dfs(root)
        return res