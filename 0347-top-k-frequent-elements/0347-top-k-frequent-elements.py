class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        h = defaultdict(int)
        for i in nums:
            h[i] += 1
        
        freq = [[] for _ in range(n+1)]
        
        for num, f in h.items():
            freq[f].append(num)
        
        res = []
        cnt = 0
        for i in range(n, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
        
        