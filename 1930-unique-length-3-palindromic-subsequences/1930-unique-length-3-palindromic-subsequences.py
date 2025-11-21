class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        l = set()
        r = Counter(s)
        for m in s:
            r[m] -= 1
            for c in l:
                if r[c]:
                    res.add(m + c)
            l.add(m)

        return len(res)