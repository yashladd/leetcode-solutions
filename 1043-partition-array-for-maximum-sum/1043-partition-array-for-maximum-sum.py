class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def f(i):
            if i == n:
                return 0

            maxi = -float("inf")
            for j in range(i, min(n, i + k)):
                thisSum = max(arr[i:j+1]) * (j-i+1) + f(j + 1)
                maxi = max(maxi, thisSum)

            return maxi
        return f(0)


        