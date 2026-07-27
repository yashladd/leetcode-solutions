# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = self._check_depth(root)
        if depth == -1:
            return False

        return True

    def _check_depth(self, node):
        if not node:
            return 0

        l_d = self._check_depth(node.left)
        r_d = self._check_depth(node.right)

        if l_d == -1 or r_d == -1 or abs(l_d - r_d) > 1:
            return -1
        
        return 1 + max(l_d, r_d)

        