class Solution:
    def maxDistance(self, g: List[List[int]]) -> int:
        q = deque([])
        n = len(g)
        for i in range(n):
            for j in range(n):
                if g[i][j]:
                    q.append((i,j))
                    
        if not q or len(q) == (n*n):
            return -1
        
        dist = [[-1] * n for _ in range(n)]
        
        def inb(x,y):
            return x >= 0 and x < n and y >= 0 and y < n
        
        curr = 1
        ans = -float("inf")
        while q:
            zs = len(q)
            for _ in range(zs):
                r, c = q.popleft()
                for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                    i, j = r + dx, c + dy
                    if inb(i, j) and dist[i][j] == -1 and not g[i][j]:
                        dist[i][j] = curr
                        if curr > ans:
                            ans = curr
                        q.append((i,j))
            curr += 1

        return ans
                        
                        
        