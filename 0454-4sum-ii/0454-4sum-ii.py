class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        h = defaultdict(int)
        for i in nums1:
            for j in nums2:
                h[i+j] += 1
        res = 0
        for i in nums3:
            for j in nums4:
                res += h[0 - i - j]

        return res

        