# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # counter = [float('-inf')]
        counter = float('-inf')
        def helper(root): 
            nonlocal counter
            if not root: 
                return 0
            lmax = helper(root.left)
            rmax = helper(root.right)
            nowrapSum = max(root.val + lmax, root.val + rmax, root.val)
            wrapSum = max(lmax,0) + root.val + max(rmax,0)
            # if wrapSum > counter[0]: # wrapSum always >= noWrapSum
            #     counter[0] = wrapSum
            if wrapSum > counter: # wrapSum always >= noWrapSum
                counter = wrapSum
            return nowrapSum
        helper(root)
        # return counter[0]
        return counter