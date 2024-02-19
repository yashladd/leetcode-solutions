# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        def f(node):
            nonlocal res
            if not node:
                return 0
            
            ls = f(node.left)
            rs = f(node.right)
            
            res += abs(ls-rs)
            
            return node.val + ls + rs
        
        f(root)
        return res