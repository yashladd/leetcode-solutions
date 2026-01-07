# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MAXI = -float("inf")
    MOD = 10**9+7
    def getSum(self, node):
        if not node:
            return 0
        return node.val + self.getSum(node.left) + self.getSum(node.right)


    def dfs(self, node, total):
        if not node:
            return 0

        ls = self.dfs(node.left, total)
        rs = self.dfs(node.right, total)

        self.MAXI = max(self.MAXI, ((ls) * (total - ls)) , (rs * (total - rs)))
        return (node.val + ls + rs)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = self.getSum(root)

        self.dfs(root, total_sum)

        return (self.MAXI) %  self.MOD
        