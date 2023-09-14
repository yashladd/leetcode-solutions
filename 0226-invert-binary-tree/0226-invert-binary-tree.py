# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(node):
            if not node:
                return None
            
            rch = f(node.right)
            lch = f(node.left)
            
            node.left = rch
            node.right = lch
            
            return node
        
        return f(root)
        