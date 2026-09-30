# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        res = []
        d = collections.deque()
        d.append(root)
        while len(d) > 0: 
            dlen = len(d)
            for i in range(len(d)): 
                popped = d.popleft()
                if i == dlen - 1: 
                    res.append(popped.val)
                if popped.left: d.append(popped.left)
                if popped.right: d.append(popped.right)
        return res
