# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def f(left, right):
            if not left or not right:
                return left == right
            
            isLeft = f(left.left, right.right)
            isRight = f(left.right, right.left)
            
            return left.val == right.val and isLeft and isRight
        
        return f(root.left, root.right)
            
            
        