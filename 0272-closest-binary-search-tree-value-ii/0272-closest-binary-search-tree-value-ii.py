# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], x: float, k: int) -> List[int]:

        ino = []

        def f(node):
            if node:
                f(node.left)
                ino.append(node.val)
                f(node.right)


        f(root)
        N = len(ino)
        lo = 0
        hi = N - k

        while lo < hi:
            mid = (lo + hi) >> 1

            if x - ino[mid] > ino[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid

        return ino[lo: lo + k]


        