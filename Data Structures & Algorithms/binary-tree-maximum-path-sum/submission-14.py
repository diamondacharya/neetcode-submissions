# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(root): 
            nonlocal res
            if not root: 
                return 0
            leftres = dfs(root.left)
            rightres = dfs(root.right)
            unwrapped = root.val + max(max(0, leftres), max(0, rightres))
            wrapped = root.val + max(0, leftres) + max(0, rightres)
            if wrapped > res: 
                res = wrapped
            return unwrapped 
        dfs(root)
        return res 


        