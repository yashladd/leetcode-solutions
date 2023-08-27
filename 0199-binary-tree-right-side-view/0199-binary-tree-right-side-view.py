# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def r(root, level):
            if root:
                if level == len(res):
                    res.append(root.val)
                r(root.right, level+1)
                r(root.left, level+1)

        r(root, 0)
        return res

