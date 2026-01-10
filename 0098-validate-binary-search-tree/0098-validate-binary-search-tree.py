# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def f(node, minVal, maxVal):
            if not node:
                return True

            # if not node.left and not node.right:
            #     return True
            
            if node.val >= maxVal or node.val <= minVal:
                return False

            isLeftValid = f(node.left, minVal, node.val)
            isRightValid = f(node.right, node.val, maxVal)

            return isLeftValid and isRightValid


        return f(root, -float("inf"), float("inf"))

            

            

            
        


        