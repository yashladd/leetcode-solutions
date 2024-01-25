class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        G = defaultdict(list)
        
        for sr, de in connections:
            G[sr].append(de)
            G[de].append(sr)
            
        tin = [0] * n
        low = [0] * n
        time = [0]
        
        vis = set()
        res = []
        def dfs(node, par):
            vis.add(node)
            tin[node] = time[0]
            low[node] = time[0]
            time[0] += 1
            
            for nei in G[node]:
                if nei == par:
                    continue
                    
                if nei not in vis:
                    dfs(nei, node)
                    
                if low[nei] > tin[node]:
                    res.append([node, nei])
                    
                low[node] = min(low[node], low[nei])
        dfs(0, -1)
        return res
            
        
        