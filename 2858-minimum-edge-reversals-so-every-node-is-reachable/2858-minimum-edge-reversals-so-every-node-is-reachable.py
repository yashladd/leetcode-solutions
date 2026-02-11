class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for u, v in edges:
            g[u].append((v,0))
            g[v].append((u, 1))

        depth = [-1] * n
        costToReverse = [inf] * n
        costToReverse[0] = 0
        depth[0] = 0
        def dfs(src, par, d):
            totalCost = 0
            depth[src] = d
            for nei, wt in g[src]:
                if nei != par:
                    totalCost += wt
                    costToReverse[nei] = costToReverse[src] + wt
                    totalCost += dfs(nei, src, d + 1)

            return totalCost

        costOfSrc = dfs(0, -1, 0)
        res = [0] * n
        res[0] = costOfSrc
        for i in range(n):
            if i != 0:
                # For node to reach 0
                cost1 = depth[i] - costToReverse[i]
                # Other edges are already reversed If I can reach the original source, it means I've already acconted for reaching 
                # Other nodes in the total cost calculated in dfs 
                # But But that cost also includes the cost of src -> node i
                cost2 = costOfSrc - costToReverse[i]
                res[i] = cost1 + cost2

        return res





