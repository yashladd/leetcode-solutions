class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        h = []
        N = len(s)
        f = Counter(s)
        for k, v in f.items():
            heappush(h, (-v, k))
        
        while h:
            mostFreq, ch = heappop(h)
            if len(res) and res[-1] == ch:
                if not h:
                    return ""
                secmostFreq, ch2 = heappop(h)
                res.append(ch2)
                if secmostFreq + 1 != 0:
                    heappush(h, (secmostFreq + 1, ch2))
                heappush(h, (mostFreq, ch))
            else:
                res.append(ch)
                if mostFreq + 1 != 0:
                    heappush(h, (mostFreq + 1, ch))
        return "".join(res)

        