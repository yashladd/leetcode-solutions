# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def f(r, x, y):
            if not r:
                return True
            
            if not r.val > x or not r.val < y:
                return False
            
            return f(r.left, x, r.val) and f(r.right, r.val, y)
        
        return f(root, -float("inf"), float("inf"))
            
        