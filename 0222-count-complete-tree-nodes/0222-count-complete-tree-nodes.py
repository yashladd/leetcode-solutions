# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.cnt = 0
        def f(node):
            if node:
                self.cnt += 1
                f(node.left)
                f(node.right)
                
        f(root)
        return self.cnt
        