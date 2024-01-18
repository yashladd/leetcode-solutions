class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = [-x for x in nums]
        heapify(a)
        print(a[0])
        res = 0
        while k:
            res = heappop(a)
            k -= 1
            
        return -res
        