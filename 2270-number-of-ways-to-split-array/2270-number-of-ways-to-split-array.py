class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = [0 for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            pref[i+1] = pref[i] + nums[i]

        cnt= 0
        #[0 10 14 6 13]
        # 0 1  2  3  4
        for i in range(len(nums)-1):
            left = pref[i+1]
            right = pref[-1] - pref[i+1]
            # print(left, right)
            if left  >= right:
                cnt += 1

        return cnt