# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        par = {}
        q = deque([root])
        p = deque([])
        vis = {} 
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft() 
                if node.left:
                    par[node.left] = node
                    q.append(node.left)
                if node.right:
                    par[node.right] = node
                    q.append(node.right)
                if node == target:
                    p.append(node)
                    vis[node] = True
                    
        # print(p)   
        res = []
        while True:
            print(len(p))
            if k == 0:
                while p:
                    x = p.popleft()
                    res.append(x.val)
                return res
            n = len(p)
            for _ in range(n):
                node = p.popleft()
                if node.left and node.left not in vis:
                    vis[node.left] = True
                    p.append(node.left)
                if node.right and node.right not in vis:
                    vis[node.right] = True
                    p.append(node.right)
                if par.get(node, None) and par[node] not in vis:
                    vis[par[node]] = True
                    p.append(par[node])
                    
            k -= 1
            
        return res
                
            
                
                