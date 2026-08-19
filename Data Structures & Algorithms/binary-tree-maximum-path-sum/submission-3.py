# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        counter = [float('-inf')]
        def helper(root): 
            if not root: 
                return 0
            lmax = helper(root.left)
            rmax = helper(root.right)
            nowrapSum = max(root.val + lmax, root.val + rmax, root.val)
            wrapSum = max(lmax,0) + root.val + max(rmax,0)
            # if nowrapSum > counter[0]: #actually not needed (coz wrapCounter is always >=)
            #     counter[0] = nowrapSum
            if wrapSum > counter[0]: 
                counter[0] = wrapSum
            return nowrapSum
        helper(root)
        return counter[0]