# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = 0
        def f(r):
            nonlocal cnt, ans
            if r:
                f(r.left)
                cnt += 1
                if cnt == k:

                    ans = r.val
                    # return r.val
                f(r.right)
        f(root) 
        return ans
                

            

            


        