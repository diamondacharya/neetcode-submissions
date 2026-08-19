# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

            #     5
            # 1       10
            #       2    11
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # returns if the subtree rooted at root is a valid bst 
        def isValid(root, lb, rb): 
            if not root: 
                return True
            if not lb < root.val < rb: 
                return False
            return isValid(root.left, lb, root.val) and isValid(root.right, root.val, rb)
        return isValid(root, float('-inf'), float('inf'))