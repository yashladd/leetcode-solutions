class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        h = Counter(nums)
        while original in h:
            original *= 2

        return original 
        