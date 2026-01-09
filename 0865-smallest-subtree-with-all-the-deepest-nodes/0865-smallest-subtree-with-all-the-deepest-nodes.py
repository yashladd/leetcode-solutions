class Solution(object):
    def subtreeWithAllDeepest(self, root):
        depth = {}
        def dfs(node, d):
            if not node: 
                return
            depth[node] = d
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)

        maxd = max(depth.values())
        def dfs_d(node: TreeNode) -> TreeNode:
            if not node or depth[node] == maxd:
                return node
            L = dfs_d(node.left)
            R = dfs_d(node.right)
            if L and R:
                return node
            return L or R

        return dfs_d(root)