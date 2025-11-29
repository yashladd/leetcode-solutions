# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stk = []
        res = []
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            node = stk.pop()
            res.append(node.val)
            cur = node.right
        return res


        