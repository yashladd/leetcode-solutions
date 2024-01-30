# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ino = []
        def f(root):
            if root:
                f(root.left)
                ino.append(root.val)
                f(root.right)
        f(root)
        prev, diff = ino[0], float("inf")
        for num in ino[1:]:
            diff = min(diff, abs(num-prev))
            prev= num
            
        return diff
                
        