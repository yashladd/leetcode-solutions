# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = 0
        res  = []
        if not root: return res
        q = deque([root])
        while q:
            level = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if h % 2:
                res.append(level[::-1])
            else:
                res.append(level)
                
            h += 1
            
        return res
            
                    