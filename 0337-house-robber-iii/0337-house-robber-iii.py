# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def f(node):
            if not node:
                return [0, 0]
            
            take = node.val + f(node.left)[1] + f(node.right)[1]
            notTake = max(f(node.left))  + max(f(node.right))
            
            return [take, notTake]
        
        return max(f(root))
        