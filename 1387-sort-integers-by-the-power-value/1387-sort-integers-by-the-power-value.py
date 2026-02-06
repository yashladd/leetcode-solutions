class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        h = []
        from functools import cache

        @cache
        def build(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return 1 + build(num // 2)
            else:
                return 1 + build(3 * num + 1)

        for x in range(lo, hi + 1):

            heappush(h, (-build(x), -x))
            if len(h) > k:
                heappop(h)

        return -h[0][1]



        