# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def f(r, maxi = -1e9):
            return f(r.left, max(r.val, maxi)) + f(r.right, max(r.val, maxi)) + (r.val >= maxi) if r else 0
                
        return f(root, -1e9)