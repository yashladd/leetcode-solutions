class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []

        h = Counter(nums)

        for key, cnt in h.items():
            heappush(min_heap, (cnt, key))

            if len(min_heap) > k:
                heappop(min_heap)

        return list([x[1] for x in min_heap])