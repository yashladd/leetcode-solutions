class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(sqrt((x**2 + y**2)), [x, y]) for x, y in points]
        
        heapify(dist)
        res = []
        while k:
            _, p = heappop(dist)
            res.append(p)
            k -= 1
        return res
            
        