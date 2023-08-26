# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        q = deque([(root, 0)])
        while q:
            n = len(q)
            l, r = 0, 0
            # _, first = q[0]
            for i in range(n):
                node, vo = q.popleft() 
                if i == 0:
                    l = vo
                if i == n-1:
                    r = vo
                if node.left: 
                    q.append((node.left, 2 * (vo - l) + 1))
                if node.right:
                    q.append((node.right, 2 * (vo -l) + 2))  
            width = r - l + 1
            maxi = max(maxi, width)
        return maxi
                