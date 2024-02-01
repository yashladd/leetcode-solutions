# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        lmost = None
        while q:
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                if i == 0:
                    lmost = node.val
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
        return lmost
                
        