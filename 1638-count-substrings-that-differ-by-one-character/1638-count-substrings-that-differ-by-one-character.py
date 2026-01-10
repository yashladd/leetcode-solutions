class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] != t[j]:
                    l, r = 1, 1
                    while i - l >= 0 and j - l >= 0 and s[i-l] == t[j-l]:
                        l+=1
                    while i + r < len(s) and j + r < len(t) and s[i+r] == t[j + r]:
                        r += 1
                    res += (l * r )


                # while i + pos < len(s) and j + pos < len(t) and miss < 2:
                #     miss += s[i + pos] != t[j + pos]
                #     res += miss == 1
                #     pos += 1
        return res