class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        heappush(h, 1)
        pops = 0
        seen = set()
        seen.add(1)
        while True:
            node = heappop(h)
            pops += 1
            if pops == n:
                return node

            for x in [2, 3, 5]:
                nex = node * x
                if nex not in seen:
                    seen.add(nex)
                    heappush(h, nex)

        return None

        