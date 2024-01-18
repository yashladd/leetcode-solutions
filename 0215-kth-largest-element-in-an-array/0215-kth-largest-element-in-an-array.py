class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums[:k]
        heapify(q)
        for n in nums[k:]:
            if n > q[0]:
                heappop(q)
                heappush(q, n)
                
        return q[0]