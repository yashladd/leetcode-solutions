# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # return None
        
        def bst(i, j):
            if i > j:
                return None
            
            mid = (i + j) // 2
            
            node = TreeNode(nums[mid])
            
            node.left = bst(i, mid-1)
            node.right = bst(mid+1, j)
            return node
        
        return bst(0, len(nums)-1)