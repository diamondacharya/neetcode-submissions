# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        runningMax = float('-inf')
        def helper(root): 
            if not root: 
                return float('-inf')
            nonlocal runningMax
            lmax = helper(root.left)
            rmax = helper(root.right)
            toret = max(root.val, root.val + lmax, root.val + rmax)
            runningMax = max(runningMax, max(toret, root.val + lmax + rmax))
            return toret
        helper(root)
        return runningMax