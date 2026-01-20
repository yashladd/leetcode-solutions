# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = defaultdict(list)

        q = deque([(0, 0, root)])

        while q:
            vert, lev, node = q.popleft()
            positions[vert].append((lev, node.val))
            if node.left:
                q.append((vert-1, lev + 1, node.left))

            if node.right:
                q.append((vert+1, lev + 1, node.right))
        res = []
        for vert in sorted(positions.keys()):
            res.append([x[1] for x in sorted(positions[vert])])
        return res
