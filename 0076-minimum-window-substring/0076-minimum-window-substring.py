class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s, t = s.lower(), t.lower()
        tCnt = Counter(t)

        i, j, n = 0, 0, len(s)
        m = len(t)
        matches = 0
        sCnt = Counter()
        mini = float("inf")
        res = ""
        while j < n:
            sCnt[s[j]] += 1
            while sCnt >= tCnt:
                if j - i + 1 < mini:
                    mini = j - i + 1
                    res = s[i:j+1]
                sCnt[s[i]] -= 1
                i += 1
            j += 1

        return res





        