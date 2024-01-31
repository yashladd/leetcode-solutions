class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, v in enumerate(manager):
            if v != -1:
                g[v].append(i)
        
        q = deque([(headID, 0)])
        maxi = 0
        while q:
            node, time = q.popleft()
            maxi = max(maxi, time)
            for nei in g[node]:
                q.append((nei, time + informTime[node]))
                
        return maxi        
        