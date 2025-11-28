class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        res = 0
        def f(i, p):
            nonlocal res
            total = values[i]

            for nei in g[i]:
                if nei != p:
                    total += f(nei, i)
            if not total % k:
                res += 1
            return total 
        f(0, -1)
        return res


        