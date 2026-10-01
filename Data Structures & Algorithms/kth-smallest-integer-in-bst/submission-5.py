# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        i = 0
        while stack or root: 
            while root: 
                stack.append(root)
                root = root.left
            popped = stack.pop()
            i += 1
            if i == k: 
                return popped.val
            root = popped.right
        

        
        