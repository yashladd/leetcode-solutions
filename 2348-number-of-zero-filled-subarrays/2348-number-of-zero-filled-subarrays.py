class Solution:
    def zeroFilledSubarray(self, a: List[int]) -> int:
        i = 0
        res = 0
        n = len(a)
        while i < n:
            if a[i] == 0:
                l = i
                while i < n and a[i] == 0:
                    i += 1
                z = i - l
                res += z * (z + 1) // 2
            i += 1
        return res
