# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if not root:
            return 0

        def f(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and f(n.left, val, path):
                path.append("L")
            elif n.right and f(n.right, val, path):
                path.append("R")
            return len(path) > 0

        p1 = [] 
        f(root, p, p1)
        p2 = []
        f(root, q, p2)
        print(p1, p2)
        while p1 and p2 and  p1[-1] == p2[-1]:
            p1.pop()
            p2.pop()

        return len(p1) + len(p2)

