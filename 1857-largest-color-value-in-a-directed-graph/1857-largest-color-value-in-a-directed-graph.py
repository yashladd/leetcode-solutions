class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = defaultdict(list)
        ind = [0] * n
        for u, v in edges:
            g[u].append(v)
            ind[v] += 1
            
        traverse = [i for i , v in enumerate(ind) if v == 0]
        count = [[0] * 26 for _ in range(n)]
        q = deque(traverse)
        if not q: 
            return -1
        for i in range(n):
            count[i][ord(colors[i]) - ord('a')] += 1
        maxi = 0
        visited = 0
        
        while q:
            node = q.popleft()
            visited += 1
            for nei in g[node]:
                ind[nei] -= 1
                for i in range(26):
                    count[nei][i] = max(
                        count[nei][i], 
                        (1 if ord(colors[nei]) - ord('a') == i else 0) + count[node][i]
                    )
                if not ind[nei]:
                    q.append(nei)
            maxi = max(maxi, max(count[node]))
        
        return -1 if visited != n else maxi
                    
                    

        
        def dfs(node, cols, vis, pathVis):
            nonlocal maxi
            vis.add(node)
            pathVis[node]=1
            thisCol = ord(colors[node]) - ord('a')
            cols[thisCol] += 1
            for nei in g[node]:
                # if nei not in vis:
                if not pathVis[nei]: 
                    if dfs(nei, cols, vis, pathVis):
                        return True
                elif pathVis[nei]:
                    return True
            maxi = max(maxi, max(cols))
            # print("End", node, cols, pathVis)
            cols[thisCol] -= 1
            pathVis[node] = 0
            return False

        
        maxi = 1
        for node in traverse:
            cols = [0] * 26
            vis = set()
            path = [0] * n
            if dfs(node, cols, vis, path):
                return -1
        return maxi

