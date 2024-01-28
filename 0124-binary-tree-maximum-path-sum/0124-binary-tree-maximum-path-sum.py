# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxi = [-1e9]
        def f(root):
            if not root:
                return 0
    
            ls, rs = max(f(root.left), 0), max(f(root.right), 0)
            maxi[0] = max(maxi[0], root.val + ls + rs)
            
            return root.val + max(ls , rs)
        
        f(root)
        return maxi[0]
        
        
        