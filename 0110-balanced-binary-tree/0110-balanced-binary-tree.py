# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node):
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        ld = self.depth(root.left)
        rd = self.depth(root.right)
        
        return abs(ld-rd) <= 1 and self.isBalanced(root.left) \
                and self.isBalanced(root.right)
        

        
        