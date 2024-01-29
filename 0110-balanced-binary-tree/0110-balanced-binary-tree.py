# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def d(root):
            if not root:
                return 0
            
            lh = d(root.left)
            if lh == -1:
                return -1
            rh = d(root.right)
            if rh == -1:
                return -1
            return -1 if abs(lh-rh) > 1 else 1 + max(lh, rh)
            
            
        return False if d(root) == -1 else True
        
    
        
        
        