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
        lh = self.depth(node.left)
        if lh == -1: return -1
        rh = self.depth(node.right)
        if rh == -1: return -1
        return -1 if abs(lh-rh) > 1 else 1 + max(lh, rh)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        return self.depth(root) != -1
        

        
        