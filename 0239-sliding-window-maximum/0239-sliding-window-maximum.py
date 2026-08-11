class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_max = deque()
        #  0 1  2 3  4 5 6 7  
        # [1,3,-1,-3,5,3,6,7]
        res = []
        for i, val in enumerate(nums):
            if window_max and i - window_max[0][1] >= k:
                window_max.popleft()

            while window_max and window_max[-1][0] <= val:
                window_max.pop()

            window_max.append((val, i))


            if i + 1 >= k:
                res.append(window_max[0][0])

        
        return res