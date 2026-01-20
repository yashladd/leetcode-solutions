class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        h = []
        def build(num):
            q = deque([(num, 0)])
            seen = set()
            while q:
                sz = len(q)
                for _ in range(sz):
                    num, step = q.popleft()
                    if num == 1:
                        return step
                    
                    if num%2:
                        if num * 3 + 1 not in seen:
                            seen.add(num * 3 + 1)
                            q.append((num * 3 + 1, step + 1))
                    else:
                        if num // 2 not in seen:
                            seen.add(num//2)
                            q.append((num//2, step + 1))

        for x in range(lo, hi + 1):
            # print(h, x, build(x))
            heappush(h, (-build(x), -x))
            if len(h) > k:
                heappop(h)

        return -h[0][1]



        