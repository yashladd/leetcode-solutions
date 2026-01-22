# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        INF = float("inf")
        cnt = 0
        def f(node, pathMax):
            nonlocal cnt
            if not node:
                return
            # print(node.val, pathMax)
            if node.val >= pathMax:
                cnt += 1
            pathMax = max(node.val, pathMax)
            f(node.left, pathMax)
            f(node.right, pathMax)

        f(root, -INF)
        return cnt

            


            


        