# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        maxi = 0
        while q:
            first, last = 0, 0
            n = len(q)
            for i in range(n):
                node, pos = q.popleft()
                if i == 0:
                    first = pos
                if i == n-1:
                    last = pos
                    
                if node.left:
                    q.append((node.left, 2*(pos - first) + 1))
                if node.right:
                    q.append((node.right, 2*(pos - first) + 2))
                    
            maxi = max(maxi, (last- first+ 1))
            
        return maxi
                