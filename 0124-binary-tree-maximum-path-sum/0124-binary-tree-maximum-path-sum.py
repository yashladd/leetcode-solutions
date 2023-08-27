# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = -float("inf")
        def f(root):
            nonlocal maxi
            if not root:
                return 0
            
            ls = max(0, f(root.left))
            
            rs = max(0, f(root.right))
            
            maxi = max(maxi, root.val + ls + rs)
            
            return root.val + max(ls, rs)
        
        f(root)
        return maxi
        