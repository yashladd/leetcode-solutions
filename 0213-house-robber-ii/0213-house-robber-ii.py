class Solution:
    def rob1(self, nums: List[int]) -> int:
        

        N = len(nums)

        @cache
        def f(i):
            if i >= N:
                return 0

            return max(nums[i] + f(i+2), f(i+1))
        return f(0)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        

        def f(a):
            """
            1 2 3 2 4 5
                4 4 8 9          
            """
            if len(a) == 1:
                return a[0]

            prev1 = a[0]
            prev2 = max(prev1, a[1])

            max_money = prev2
            N = len(a)
            for i in range(2, N):
                curr = max(a[i] + prev1, prev2)
                max_money = max(max_money, curr)
                prev2, prev1 = curr, prev2

            return max_money

        return max(f(nums[:-1]), f(nums[1:]))