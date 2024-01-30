# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(left, right):
            if not left or not right:
                return left == right

            
            isleft = f(left.left, right.right)
            isright = f(left.right, right.left)

            return left.val == right.val and isleft and isright

        return f(root.left, root.right)
        
        
            
        