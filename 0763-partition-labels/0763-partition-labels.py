class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = defaultdict(int)
        for i, ch in enumerate(s):
            h[ch] = i
        n = len(s)
        size, end = 0, 0
        ans = []
        for i in range(n):
            size += 1
            end = max(end, h[s[i]])
            if i == end:
                ans.append(size)
                size = 0
        return ans