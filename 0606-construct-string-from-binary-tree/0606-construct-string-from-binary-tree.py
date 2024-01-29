# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        path = []
        def f(node):
            if not node:
                return 
            
            if not node.left and not node.right:
                path.append(str(node.val))
                return 
            
            path.append(f"{node.val}(")
            
            f(node.left)
            
            path.append(")")
            
            if node.right:
                path.append("(")
                
                f(node.right)
                
                path.append(")")
                
        f(root)
        print(path)
        return "".join(path)
            
            
            
        