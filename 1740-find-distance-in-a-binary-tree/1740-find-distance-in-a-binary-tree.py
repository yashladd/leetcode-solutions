# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        def populate_reverse_path(node, path_info, target):
            if not node:
                return False

            if node.val == target:
                path_info.append(node.val)
                return True

            left_found = populate_reverse_path(node.left, path_info, target)
            right_found = populate_reverse_path(node.right, path_info, target)


            if left_found or right_found:
                path_info.append(node.val)
                return True

            return False


        p_path = []

        populate_reverse_path(root, p_path, p)

        q_path = []
        populate_reverse_path(root, q_path, q)

        while p_path and q_path and p_path[-1] == q_path[-1]:
            p_path.pop()
            q_path.pop()


        return len(p_path) + len(q_path)

