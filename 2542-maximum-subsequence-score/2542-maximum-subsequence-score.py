class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = []
        for x,y in zip(nums1, nums2):
            nums.append((x,y))
        # Sorted in reverse
        maxi = 0
        nums.sort(key=lambda x: -x[1])
        h = []
        max_sum = 0
        for x, y in nums:
            heappush(h, x)
            max_sum += x

            if len(h) > k:
                p = heappop(h)
                max_sum -= p
            
            if len(h) == k:
                maxi = max(maxi, max_sum * y)
        return maxi


        