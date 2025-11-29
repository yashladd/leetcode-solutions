# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = -float("inf")

        def f(n):
            nonlocal maxi
            if not n:
                return 0

            l, r = max(0, f(n.left)), max(0, f(n.right))
            maxi = max(n.val + l + r, maxi)

            return max(l , r) + n.val

        f(root)
        return maxi
        