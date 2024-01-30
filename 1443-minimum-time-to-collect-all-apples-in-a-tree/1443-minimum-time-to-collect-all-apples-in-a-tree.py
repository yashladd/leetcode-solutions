class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            
        
        def dfs(node, par):
            cost = 0
            
            for nei in g[node]:
                if nei != par:
                    neiCost = dfs(nei, node)
                    if neiCost > 0 or hasApple[nei]:
                        cost += 2 + neiCost
            return cost
        
        
        return dfs(0, -1)
        
        