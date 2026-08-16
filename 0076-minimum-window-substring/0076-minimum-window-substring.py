class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tf = Counter(t)

        req = len(tf)

        mat = 0

        sf = Counter()

        l = 0
        min_l = inf
        min_s = ""
        for r, ch in enumerate(s):
            sf[ch] += 1
            if sf[ch] == tf[ch]:
                mat += 1

            while req == mat and l <= r:
                if (r-l + 1) < min_l:
                    min_l = r - l  +1
                    min_s = s[l:r+1]

                sf[s[l]] -= 1
                if sf[s[l]] < tf[s[l]]:
                    mat -= 1

                if not sf[s[l]]:
                    del sf[s[l]]

                l += 1

        return min_s



        