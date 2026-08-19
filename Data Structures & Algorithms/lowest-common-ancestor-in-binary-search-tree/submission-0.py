# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(root, p, q): 
            if not root: 
                return (0, None) 
            lcount, lanc = helper(root.left, p, q)
            rcount, ranc = helper(root.right, p, q)
            if lcount == 2: 
                return (2, lanc)
            if rcount == 2: 
                return (2, ranc)
            count = lcount + rcount + (root.val == p.val) + (root.val == q.val)
            return (count, root if count == 2 else None)
        return helper(root, p, q)[1]