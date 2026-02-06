class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        [5, 1, 5, 5, 0]
        """
        h = {0:-1}
        currMod = 0
        for i, x in enumerate(nums):
            currMod += x
            currMod %= k
            if currMod in h:
                if i - h[currMod] >= 2:
                    return True
            else:
                h[currMod] = i

        return False

        