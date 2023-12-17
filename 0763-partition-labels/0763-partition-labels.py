class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = defaultdict(int)
        for i, ch in enumerate(s):
            h[ch] = i
        n = len(s)
        l, r = 0, 0 
        ans = []
        while l < n and r < n:
            start = l
            r = max(r, h[s[l]])
            l += 1
            while  r >= l:
                # print(l, r)
                r = max(r, h[s[l]])
                l += 1
            ans.append(r-start+1)
            l = r + 1
            
        return ans
        