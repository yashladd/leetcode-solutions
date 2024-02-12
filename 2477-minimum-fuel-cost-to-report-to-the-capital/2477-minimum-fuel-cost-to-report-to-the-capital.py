class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = defaultdict(list)
        node = set()
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)
            node.add(u)
            node.add(v)
            
        ans = 0

        def dfs(node, par):
            nonlocal ans
            passangers = 1
            for nei in g[node]:
                if nei != par:
                    p = dfs(nei, node)
                    ans += int(ceil(p/seats))
                    passangers += p
            return passangers
        dfs(0, -1)
        return ans
            
            
            
        