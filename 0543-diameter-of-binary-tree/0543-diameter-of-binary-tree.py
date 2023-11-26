# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxD = 0
        def f(root):
            nonlocal maxD
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            
            l = f(root.left)
            r = f(root.right)
            
            maxD = max(maxD, l + r)

            return 1 + max(l, r)
        
        f(root)
        return maxD
            
        