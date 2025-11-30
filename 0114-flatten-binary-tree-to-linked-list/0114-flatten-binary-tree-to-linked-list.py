# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def f(node):
            nonlocal prev
            if not node:
                return 

            f(node.right)
            f(node.left)
            node.left = None
            node.right = prev
            prev = node
        
            return node

        return f(root)
        