# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0, 0)])
        levels = defaultdict(list)
        while q:
            node, vertical, level = q.popleft() 
            levels[vertical].append((level, node.val))
            if node.left:
                q.append((node.left, vertical - 1, level + 1))
            if node.right:
                q.append((node.right, vertical + 1, level + 1))
                
        return [[x[1] for x in sorted(level)] for _, level in sorted(levels.items())]
            
        