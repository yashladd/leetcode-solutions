# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        cur = root


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
                    k -= 1
                    if not k:
                        return cur.val
                    cur = cur.right
            else:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
        return -1
            