# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root): 
            if not root: 
                return [None, 0]
            lroot, lcount = dfs(root.left)
            rroot, rcount = dfs(root.right)
            if lcount == 2: return [lroot, 2]
            if rcount == 2: return [rroot, 2]
            totalCount = lcount + rcount + int(root.val == p.val) + int(root.val == q.val)
            return [root, totalCount]
        return dfs(root)[0]
