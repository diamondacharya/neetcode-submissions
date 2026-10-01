# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pi = 0 # preorder index
        d = {val: i for i, val in enumerate(inorder)}
        def dfs(l, r): # takes the left and right indices of the inorder array to process 
            nonlocal pi
            if l > r: 
                return None
            val = preorder[pi]
            pi += 1
            node = TreeNode(val)
            ii = d[val] # inorder index
            node.left = dfs(l, ii - 1)
            node.right = dfs(ii + 1, r)
            return node
        return dfs(0, len(inorder) - 1)

        