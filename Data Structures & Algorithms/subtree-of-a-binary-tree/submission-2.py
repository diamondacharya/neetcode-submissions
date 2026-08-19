# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def areSameTree(p, q): 
            if not p and not q: 
                return True
            if p and not q or not p and q: 
                return False
            return p.val == q.val and areSameTree(p.left, q.left) and areSameTree(p.right, q.right)
        if not root and not subRoot or root and not subRoot: 
            return True
        elif not root: 
            return False
        d = collections.deque()
        d.append(root)
        while len(d) > 0: 
            popped = d.pop()
            if popped.left: 
                d.append(popped.left)
            if popped.right: 
                d.append(popped.right)
            if popped.val == subRoot.val and areSameTree(popped, subRoot): 
                return True 
        return False
