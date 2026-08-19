# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pi = 0
        d = {val: i for i, val in enumerate(inorder)}
        def helper(l, r): 
            if l > r: 
                return None
            nonlocal pi
            root = TreeNode(preorder[pi])
            ii = d[preorder[pi]]
            pi += 1
            root.left = helper(l, ii - 1) 
            root.right = helper(ii + 1, r)
            return root
        return helper(0, len(inorder) - 1)