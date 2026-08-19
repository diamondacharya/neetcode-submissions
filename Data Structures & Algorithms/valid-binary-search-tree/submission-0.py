# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def boundaryCheck(root, lb, rb): 
            if not root: 
                return True
            return lb < root.val < rb and boundaryCheck(root.left, lb, root.val) and boundaryCheck(root.right, root.val, rb)
        return boundaryCheck(root, float('-inf'), float('inf'))