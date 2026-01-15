class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sC = Counter(s)
        tC = Counter(t)
        print((Counter(t) - Counter(s)))
        res = 0
        for bet, cnt in sC.items():
            # print(bet, cnt , tC[bet])
            res += max(0, cnt - tC[bet])
        return sum( list(x if x > 0 else 0 for x in (sC - tC).values()))