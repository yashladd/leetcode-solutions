# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -1
        mini= float("inf")
        def f(root):
            nonlocal mini, prev
            if root:
                f(root.left)                
                if prev>=0:
                    mini = min(mini, abs(root.val-prev))    
                prev = root.val
                f(root.right)
        f(root)
        return mini
                
        