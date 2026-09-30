# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        ret = []
        d = collections.deque()
        d.append(root)
        while len(d) > 0: 
            toappend = []
            for _ in range(len(d)): 
                node = d.popleft()
                toappend.append(node.val)
                if node.left: 
                    d.append(node.left)
                if node.right: 
                    d.append(node.right)
            ret.append(toappend)
        return ret

        