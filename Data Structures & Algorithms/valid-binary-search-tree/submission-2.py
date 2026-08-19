# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, lb, rb): 
            if not root: 
                return True
            if (root.val <= lb or root.val >= rb): 
                return False
            return isValid(root.left, lb, root.val) and isValid(root.right, root.val, rb)
        return isValid(root, float('-inf'), float('inf'))