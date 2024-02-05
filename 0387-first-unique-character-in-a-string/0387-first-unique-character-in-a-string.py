class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = defaultdict(int)
        for ch in s:
            h[ch] += 1
        # print(h)
        for k, v in h.items():
            if v == 1:
                for i, c in enumerate(s):
                    if c == k:
                        return i
                 
        return -1
