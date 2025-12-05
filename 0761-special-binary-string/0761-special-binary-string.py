class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        l = 0
        res = []
        cnt = 0
        for r, c in enumerate(s):
            cnt += 1 if c == "1" else -1
            if cnt == 0:
                inner = self.makeLargestSpecial(s[l+1:r])
                res.append("1" + inner + "0")
                cnt = 0
                l = r + 1

        return "".join(sorted(res, reverse=True))

        