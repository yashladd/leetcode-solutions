# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        

        def validate(node, lo, hi):
            if not node:
                return True
            val = node.val
            if val <= lo or val >= hi:
                return False

            return validate(node.left, lo, val) and validate(node.right, val, hi)

        return validate(root, -inf, inf)