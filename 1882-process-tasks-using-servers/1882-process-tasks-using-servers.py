class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        avail = [(wt, i) for i, wt in enumerate(servers)]
        heapify(avail)

        ans = []

        busy = []

        for enqT, procT in enumerate(tasks):
            while busy and busy[0][0] <= enqT:
                _, wt, i = heappop(busy)
                heappush(avail, (wt, i))
            if avail:
                wt, i = heappop(avail)
                ans.append(i)
                heappush(busy, (enqT + procT, wt, i))
            else:
                time, wt, i = heappop(busy)
                ans.append(i)
                heappush(busy, (time + procT, wt, i))

        return ans
        