class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []
        for i, v in enumerate(nums):
            if q and i - q[0][0] == k:
                q.popleft()
            while q and q[-1][1] < v:
                q.pop()
            q.append((i, v))
            if i + 1 - k >= 0:
                res.append(q[0][1])
        return res            
            
        