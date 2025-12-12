class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = defaultdict(int)
        for t in tasks:
            cnt[t] += 1
        maxHeap = [-x for x in list(cnt.values())]
        heapify(maxHeap)
        q = deque([])
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                currCnt = heappop(maxHeap)
                currCnt += 1
                nextAvailable = time + n
                if currCnt < 0:
                    q.append((currCnt, nextAvailable))
                    
            while q and q[0][1] <= time:
                remCnt, _ = q.popleft()
                heappush(maxHeap, remCnt)
                
        return time
         