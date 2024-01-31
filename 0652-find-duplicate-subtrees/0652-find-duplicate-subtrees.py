# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        h = defaultdict(list)
        def preorder(root):
            if not root:
                return "N"
            st = ",".join([str(root.val), preorder(root.left), preorder(root.right)])
            # print(st)
            h[st].append(root)
            return st
        # print(h)
        preorder(root)
        return [root[0] for root in h.values() if root[1:]]
        