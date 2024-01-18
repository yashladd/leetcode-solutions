class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = [-s for s in stones]
        heapify(a)
        # print(a, a[0], a[1], -a[0])
        while len(a) >= 2:
            x = -heappop(a)
            y = -heappop(a)
            # print(x, y)
            if x == y:
                continue
            else:
                heappush(a, -(x - y))
        return -a[0] if len(a) else 0
        