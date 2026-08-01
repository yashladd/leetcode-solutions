# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from enum import Enum, auto
class State(Enum):
    HAS_CAMERA = auto()
    SIBLING_COVERS = auto()
    NEEDS_COVER = auto()

class Solution:
    """
       1

     2   3

        4
      2     5
     2 
        1   6   
    """
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def get_min_cameras(node: Optional[TreeNode]) -> int:
            if not node:
                return 0, State.SIBLING_COVERS


            if not node.left and not node.right:
                return 0, State.NEEDS_COVER


            left_cameras, left_state = get_min_cameras(node.left)

            right_cameras, right_state = get_min_cameras(node.right)

            if left_state == State.NEEDS_COVER or right_state == State.NEEDS_COVER:
                return 1 + left_cameras + right_cameras, State.HAS_CAMERA

            if left_state == State.HAS_CAMERA or right_state == State.HAS_CAMERA:
                return left_cameras + right_cameras, State.SIBLING_COVERS

            

            return left_cameras + right_cameras, State.NEEDS_COVER


        min_cameras, root_state = get_min_cameras(root)

        if root_state == State.NEEDS_COVER:
            min_cameras += 1

        return min_cameras

            