class Solution:
    def minDeletions(self, s: str) -> int:
        f = Counter(s)
        v = list(sorted(f.values(), reverse=True))

        dels = 0

        """
        5 3 3 3 

        3 3 2
        """
        preMax = v[0]
        dels = 0
        # print(v)
        for i in range(1, len(v)):
            # print(preMax, v[i])
            if preMax > 0 and v[i] >= preMax:
                reqF = preMax - 1
                dels += (v[i] - reqF)
                preMax = reqF
            elif preMax == 0:
                dels += v[i]
            else:
                preMax = v[i]

        return dels