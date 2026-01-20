class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            original = num
            candidate = -1
            for j in range(original):
                if (j | (j + 1)) == original:
                    candidate = j
                    break
            result.append(candidate)
        return result