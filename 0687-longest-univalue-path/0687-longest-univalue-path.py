# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def f(node):
            if not node:
                return 0
            
            left_len = f(node.left)
            right_len = f(node.right)
            
            left_path = right_path = 0
            
            if node.left and node.left.val == node.val:
                left_path = left_len + 1
                
            if node.right and node.right.val == node.val:
                right_path = right_len + 1
            
            self.res = max(self.res, left_path + right_path)
        
            return max(left_path, right_path)

        f(root)
        return self.res



            
