# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        res = []

        while cur:
            if cur.left:
                le = cur.left
                while le.right and le.right != cur:
                    le = le.right
                if le.right != cur:
                    le.right = cur
                    cur = cur.left
                else:
                    le.right = None
                    res.append(cur.val)
                    cur = cur.right
            else:
                res.append(cur.val)
                cur = cur.right
        return res
            