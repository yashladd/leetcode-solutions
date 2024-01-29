# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def f(root):
            if not root:
                return None
            if not root.left and not root.right:
                return root
            
            
            rgt, lft = root.right, root.left
            root.left = f(rgt)
            root.right = f(lft)
            
            return root
        
        return f(root)
        