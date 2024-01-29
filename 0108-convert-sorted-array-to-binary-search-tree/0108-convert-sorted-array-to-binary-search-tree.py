# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def bst(arr):
            if not arr:
                return None
            
            mid = len(arr) //2
            
            node = TreeNode(arr[mid])
            
            node.left = bst(arr[:mid])
            node.right = bst(arr[mid+1:])
            return node
        
        return bst(nums)