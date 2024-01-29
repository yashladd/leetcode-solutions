# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def f(p, q):
            if not p and not q:
                return None
            
            val = p.val if p else 0
            val += q.val if q  else 0
            root = TreeNode(val)
            
            root.left = f(q.left if q and q.left else None, p.left if p and p.left else None)
            root.right = f(q.right if q and q.right else None, p.right if p and p.right else None)
            
            return root
        
        return f(root1, root2)
                    