# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False
        
        
        def flip(r1, r2):
            if not r1 or not r2:
                return r1 == r2
            
            if r1.val != r2.val:
                return False
            
            return (flip(r1.left, r2.left) and flip(r1.right , r2.right)) or \
                    (flip(r1.right, r2.left) and flip(r1.left , r2.right))
            
            
#             lft, rgt = r1.left, r1.right
#             one = r1.val == r2.val and 
#             two = r1.val == r2.val and flip(TreeNode(r1.val, rgt, lft), r2)
            
#             return one or two 
        
        return flip(root1, root2)
            
            
            
            