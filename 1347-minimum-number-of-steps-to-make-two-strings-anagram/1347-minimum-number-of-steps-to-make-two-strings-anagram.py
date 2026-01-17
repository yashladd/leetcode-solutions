class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sC = Counter(s)
        tC = Counter(t)
        print((Counter(t) - Counter(s)))
        res = 0
        for bet, cnt in sC.items():
            # print(bet, cnt , tC[bet])
            res += max(0, cnt - tC[bet])
        return res