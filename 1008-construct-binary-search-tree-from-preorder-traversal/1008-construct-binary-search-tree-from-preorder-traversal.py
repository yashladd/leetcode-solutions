# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        n = len(preorder)

        def f(lo, hi):
            nonlocal idx
            if lo > hi:
                return None
            if idx >= n:
                return None

            

            val = preorder[idx]

            if val < lo or val > hi:
                return None

            idx += 1
            root = TreeNode(val)
            root.left = f(lo, val)
            root.right = f(val, hi)

            return root

        return f(-inf, inf)
