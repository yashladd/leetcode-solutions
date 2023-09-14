# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node, mini, maxi):
            if not node:
                return True
            
            if node.val <= mini or node.val >= maxi:
                return False

            return rec(node.left, mini, node.val) and rec(node.right, node.val, maxi)

        return rec(root, -float("inf"), float("inf"))


        