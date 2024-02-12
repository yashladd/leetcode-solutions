class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        el = -1
        for n in nums:
            if not cnt:
                el = n
                cnt += 1
            elif n == el:
                cnt += 1
            else:
                cnt -= 1
                
        return el
        