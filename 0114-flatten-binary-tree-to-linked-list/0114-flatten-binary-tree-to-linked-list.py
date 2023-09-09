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
        if not root:
            return 
        
        prev = None
        def f(root):
            nonlocal prev
            if not root:
                return 

            f(root.right)
            f(root.left)

            root.right = prev
            root.left = None
            prev = root

        f(root)


