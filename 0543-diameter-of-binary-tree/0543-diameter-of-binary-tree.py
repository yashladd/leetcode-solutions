# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return 0
        maxi = -float("inf")
        
        def f(root):
            nonlocal maxi
            if not root: return 0
            if not root.left and not root.right:
                return 1

            left = f(root.left)
            right = f(root.right)
            
            maxi = max(maxi, left + right)

            return 1+max(left , right)
        
        f(root)
        return maxi
        
        
        