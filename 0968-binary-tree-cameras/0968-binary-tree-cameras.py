# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from enum import Enum

class State(Enum):
    NEEDS_COVER = 0
    HAS_CAMERA = 1
    PARENT_COVERS = 2

     
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, State.PARENT_COVERS

            if not node.left and not node.right:
                return 0, State.NEEDS_COVER

            left_cameras, left_state = dfs(node.left)
            right_cameras, right_state = dfs(node.right)

            if left_state == State.NEEDS_COVER or right_state == State.NEEDS_COVER:
                return 1 + left_cameras + right_cameras, State.HAS_CAMERA


            if left_state == State.HAS_CAMERA or right_state == State.HAS_CAMERA:
                return left_cameras + right_cameras, State.PARENT_COVERS

            return left_cameras + right_cameras, State.NEEDS_COVER


        cameras, root_state = dfs(root)

        if root_state == State.NEEDS_COVER:
            cameras += 1

        return cameras



        