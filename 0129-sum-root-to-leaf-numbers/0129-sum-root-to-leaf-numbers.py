# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def f(node, currNum):
            if not node:
                return 0
            if not node.left and not node.right:
                return currNum * 10 + node.val
            res = 0
            res += f(node.left, currNum * 10 + node.val)
            res += f(node.right, currNum * 10 + node.val)
            
            return res
        
        return f(root, 0)
            
            
            