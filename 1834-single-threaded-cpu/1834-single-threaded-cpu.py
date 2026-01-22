class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sched = []
        for i, t in enumerate(tasks):
            sched.append((t[0], i, t[1]))

        sched.sort()
        ans = []
        h = []
        q = deque(sched)
        time = q[0][0]
        while len(q) or len(h):
            while len(q) and time >= q[0][0]:
                enqTime, idx, procTime = q.popleft()
                heappush(h, (procTime, idx))
            
            if len(h):
                procTime, idx = heappop(h)
                ans.append(idx)
                time += procTime
            else:
                if len(q):
                    time = max(q[0][0], time)
        
        return ans


        