class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []

        def push(n):
            if not max_heap or -max_heap[0] >= n:
                heappush(max_heap, -n)
            else:
                heappush(min_heap, n)
            balance()


        def balance():
            if len(max_heap) > 1 + len(min_heap):
                heappush(min_heap, -heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))


        def shift(heap, n):
            try:
                index = heap.index(n)
                # Swap the element with the last element
                heap[index] = heap[-1]
                heap.pop()
                heapq._siftup(heap, index)
                heapq._siftdown(heap, 0, index)
            except:
                pass
        
        def remove(n):
            if -max_heap[0] >= n:
                shift(max_heap, -n)
            else:
                shift(min_heap, n)
            balance()

        def getMedian():
            if len(max_heap) > len(min_heap): return -max_heap[0]
            # if len(min_heap) > len(max_heap): return min_heap[0]
            return (min_heap[0] - max_heap[0]) / 2

        N = len(nums)
        L = 0
        res = []
        for R in range(N):
            push(nums[R])
            if R - L + 1 == k:
                res.append(getMedian())
                remove(nums[L])
                L += 1

        return res


        