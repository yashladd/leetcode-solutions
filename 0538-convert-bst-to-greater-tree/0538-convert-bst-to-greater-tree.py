# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        currSum = 0
        def f(root):
            nonlocal currSum
            if not root:
                return
            f(root.right)
            tmp = root.val
            root.val += currSum
            currSum += tmp
            f(root.left)
        
        f(root)
        return root
            
            