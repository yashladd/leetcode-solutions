# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
        target_depths = {p: 0, q: 0}
        lca_depth = [0]


        def dfs(node, curr_depth) -> None:
            if not node:
                return None

            if node.val == p:
                target_depths[p] = curr_depth
                
            if node.val == q:
                target_depths[q] = curr_depth

            left_found = dfs(node.left, curr_depth + 1)
            right_found = dfs(node.right, curr_depth + 1)

            is_target = (node.val == p or node.val == q)

            if left_found and right_found or (is_target and (left_found or right_found)):
                lca_depth[0] = curr_depth

            return left_found or right_found or is_target

        dfs(root, 0)

        return target_depths[p] + target_depths[q] - 2 * lca_depth[0]
            





            

            
