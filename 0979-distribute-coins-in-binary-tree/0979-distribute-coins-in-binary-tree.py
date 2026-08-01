# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def min_transfer(node):
            if not node:
                return 0, 0 

            left_bal, left_moves = min_transfer(node.left)
            right_bal, right_moves = min_transfer(node.right)


            return (
                ( node.val - 1 ) + left_bal + right_bal,
                left_moves + right_moves + abs(left_bal) + abs(right_bal)
            )

        _, moves = min_transfer(root)

        return moves