# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def f(root, lev):
            if root:
                if len(l) == lev:
                    l.append(root.val)
                    
                f(root.right, lev + 1)
                f(root.left, lev + 1)
                
        f(root, 0)
        return l
        