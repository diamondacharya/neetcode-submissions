# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l = []
        def preorder(root): 
            if not root: 
                l.append('N')
                return
            l.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(l)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l = data.split(',')
        ind = 0
        def helper(): 
            nonlocal ind
            if l[ind] == 'N': 
                ind += 1
                return
            root = TreeNode(int(l[ind]))
            ind += 1
            root.left = helper()
            root.right = helper()
            return root
        return helper()
        