# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        idx = 0
        q = deque([root])
        while q:
            sz = len(q)
            prev = float("inf") if idx % 2 else -float("inf")

            for _ in range(sz):
                node = q.popleft()
                if idx % 2:
                    if node.val % 2 or node.val >= prev:
                        return False
                else:
                    if not node.val % 2 or node.val <= prev:
                        return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            idx += 1
        return True
        