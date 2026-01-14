class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        best = 0
        for start in range(N):
            cnt = 0
            for offset in range(N):
                if nums1[(start + offset) % N] == nums2[offset]:
                    cnt += 1
            best = max(best, cnt)
        return best       