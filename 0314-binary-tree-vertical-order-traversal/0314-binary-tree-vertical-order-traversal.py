from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        verticals = defaultdict(list)

        q = deque([(root, 0, 0)])

        while q:
            node, vertical, level = q.popleft()
            verticals[vertical].append(node.val)
            if node.left:
                q.append((node.left, vertical-1, level + 1))
            if node.right:
                q.append((node.right, vertical+1, level - 1))

        return [ verticals[k] for k in sorted(verticals.keys()) ]