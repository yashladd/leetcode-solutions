# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def d(root):
            nonlocal maxi
            if not root:
                return 0
            
            lh = d(root.left)
            rh = d(root.right)
            
            maxi = max(maxi, lh + rh)
            return 1 + max(lh , rh)
        
        d(root)
        return maxi
        
        