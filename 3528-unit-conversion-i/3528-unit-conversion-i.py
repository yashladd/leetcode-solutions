class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        n = len(conversions)
        MOD = 10 ** 9 + 7
        g = defaultdict(list)
        h = {0:1}

        for i, (u, v , w) in enumerate(conversions):
            g[u].append((v, w))

        q = deque([(0, 1)])
        vis = set()
        vis.add(0)
        while q:
            idx, wt = q.popleft()
            for nextIdx, w in g[idx]:
                if nextIdx not in vis:
                    currWt = (wt * w) % MOD
                    vis.add((nextIdx, currWt))
                    h[nextIdx] = currWt
                    q.append((nextIdx, currWt))

        res = [1] * (n+1)
        print(h, res)
        for idx, wt in h.items():
            print(idx, wt)
            res[idx] = wt

        return res


        