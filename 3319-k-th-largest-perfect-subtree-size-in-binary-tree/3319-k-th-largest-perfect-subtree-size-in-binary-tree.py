# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        perfect_tree_sizes = []

        def is_perfect(node):
            if not node:
                return True, 0, 0

            is_left_perfect, left_height, left_size = is_perfect(node.left)
            is_right_perfect, right_height, right_size = is_perfect(node.right)

            if is_left_perfect and is_right_perfect and left_height == right_height:
                curr_size =  2 * left_size + 1 #right_size + left_size + 1
                curr_height = left_height + 1
                perfect_tree_sizes.append(curr_size)

                return True, curr_height, curr_size

            return False, -1, -1

        is_perfect(root)

        perfect_tree_sizes.sort(reverse=True)

        if len(perfect_tree_sizes) < k:
            return -1

        return perfect_tree_sizes[k-1]