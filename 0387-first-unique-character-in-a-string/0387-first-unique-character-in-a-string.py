class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = defaultdict(int)
        for ch in s:
            h[ch] += 1
        # print(h)
        
        for i, c in enumerate(s):
            if h[c] == 1:
                return i
                 
        return -1
