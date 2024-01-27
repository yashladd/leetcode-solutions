class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for u, v in tickets:
            heappush(g[u], v)
        
        res = []
        def dfs(node):
            
            while g[node]:
                nei = heappop(g[node])
                dfs(nei)
                
                
            res.append(node)
            
        dfs("JFK")
        
        return res[::-1]
        