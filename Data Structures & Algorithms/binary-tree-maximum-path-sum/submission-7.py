# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        count = float('-inf')
        def helper(root): 
            if not root: 
                return 0
            nonlocal count
            lsum = helper(root.left)
            rsum = helper(root.right)
            nowrapsum = max(lsum + root.val, rsum + root.val, root.val)
            wrapsum = max(lsum, 0) + root.val + max(rsum, 0)
            if (wrapsum > count): 
                count = wrapsum
            return nowrapsum
        helper(root)
        return count