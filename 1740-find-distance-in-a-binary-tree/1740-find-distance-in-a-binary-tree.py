# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def _build(node, t, out):
            if not node:
                return False

            if node.val == t:
                out.append(node.val)
                return True

            l_f = _build(node.left, t, out)
            r_f = _build(node.right, t, out)

            if l_f or r_f:
                out.append(node.val)
                return True

            return False

        one, two = [], []

        _build(root, p, one)
        _build(root, q, two)


        while one and two and one[-1] == two[-1]: one.pop(), two.pop()

        return len(one) + len(two)
                