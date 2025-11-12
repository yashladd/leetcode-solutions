class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        2 6 3 4

        """

        def gcd(a,b):
            if b == 0:
                return a
            if b > a:
                return gcd(b, a)
            return gcd(b, a%b)
        n = len(nums)
        onesCnt = sum([int(x==1) for x in nums])

        if onesCnt >= 1:
            return len(nums) - onesCnt

        miniSub = float("inf")

        for i in range(n-1):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    miniSub = min(miniSub, j-i + 1)
        if miniSub == float("inf"): return -1
        return (miniSub-1) + n - 1
