# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def f(node, prev):
            if not node:
                return 0
            if not node.left and not node.right:
                return 0 if prev else node.val
            
            money = 0
            take = float("-inf")
            if not prev:
                take = f(node.left, 1) + f(node.right, 1) + node.val
            notTake = f(node.left, 0) + f(node.right, 0)
            
            money = max(take, notTake)
            return money
        
        return f(root, 0)
            
        