class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        N = len(ms)
        total = sum(ms)
        if total % 4:
            return False
        req_side = total // 4
        if max(ms) > req_side:
            return False
        sides = [0] * 4
        ms.sort(reverse=True)
        def back(i):
            if i == N:
                return True

            for j in range(4):
                if sides[j] + ms[i] <= req_side:
                    sides[j] += ms[i]
                    if back(i+1): return True
                    sides[j] -= ms[i]

            return False

        return back(0)