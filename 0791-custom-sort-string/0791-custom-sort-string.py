class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h = defaultdict(int)
        cnt = 0
        for x in order:
            h[x] = cnt
            cnt += 1
        orders = [[] for _ in range(26)]
        for ch in s:
            if ch in h:
                orders[h[ch]].append(ch)
            else:
                orders[-1].append(ch)
                
        res = []
        for o in orders:
            if o:
                res.extend(o)
        
        return "".join(res)

        