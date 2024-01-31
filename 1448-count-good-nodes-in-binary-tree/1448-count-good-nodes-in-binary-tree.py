# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def f(node, maxi):
            if not node:
                return 0
            return int(node.val >= maxi) + f(node.left, max(maxi, node.val)) + f(node.right, max(maxi, node.val))
        
        return f(root, root.val)
        