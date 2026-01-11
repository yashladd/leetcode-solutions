class Solution:
    def finalPrices(self, p: List[int]) -> List[int]:
        stk = [p[-1]]
        res = p[:]
        res[-1] = p[-1]
        for i in range(len(p)-2, -1, -1):
            # print(i, p[i], stk)

            while stk and stk[-1] > p[i]:
                stk.pop()

            # print(i, stk)

            if stk:
                res[i] -= stk[-1]

            stk.append(p[i])

        return res

        