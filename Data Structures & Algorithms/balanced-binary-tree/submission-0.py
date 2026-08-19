# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root): 
            if not root: 
                return True, 0 
            lHeightBalanced, lHeight = dfs(root.left)
            rHeightBalanced, rHeight = dfs(root.right)
            currHeightBalanced = abs(lHeight - rHeight) <= 1
            return lHeightBalanced & rHeightBalanced & currHeightBalanced, 1 + max(lHeight, rHeight)
        return dfs(root)[0]
        