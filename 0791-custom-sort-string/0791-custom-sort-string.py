class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h = defaultdict(int)
        cnt = 1
        for x in order:
            h[x] = cnt
            cnt += 1
        
        return "".join(sorted(s, key = lambda x: h[x]))

        