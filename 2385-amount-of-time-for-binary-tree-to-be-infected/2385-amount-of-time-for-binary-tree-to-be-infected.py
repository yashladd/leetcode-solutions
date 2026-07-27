# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(list)

        vis = set()
        def build(node, par):
            vis.add(node)
            if not node:
                return 

            if node and par:
                g[node.val].append(par.val)
                g[par.val].append(node.val)

            if node.left:
                build(node.left, node)
            
            if node.right:
                build(node.right, node)

        build(root, None)


        level = [start]
        vis = {start}
        time = 0
        while level:
            next_level = []
            for node in level:
                for ch in g[node]:
                    if ch not in vis:
                        vis.add(ch)
                        next_level.append(ch)
            level = next_level
            if next_level:
                time += 1


        return time