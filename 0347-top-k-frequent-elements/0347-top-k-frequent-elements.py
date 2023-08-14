class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)
        for i in nums:
            h[i] += 1
        
        q = []
        
        for num, freq in h.items():
            heappush(q, (-freq, num))
        
        ans = []
        while k:
            _, x = heappop(q)
            ans.append(x)
            k -= 1
            
        return ans
        