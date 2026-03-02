class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        Q = len(queries)
        L = len(logs)
        res = [0] * Q
        sorted_logs = sorted(logs, key = lambda x: x[1])
        sorted_queries = sorted(enumerate(queries), key = lambda x: x[1])

        server_cnt = defaultdict(int)
        left = right = 0
        for idx, time in sorted_queries:

            while right < L and sorted_logs[right][1] <= time:
                server_cnt[sorted_logs[right][0]] += 1
                right += 1
            
            while left < L and sorted_logs[left][1] < time - x:
                server_cnt[sorted_logs[left][0]] -= 1
                if not server_cnt[sorted_logs[left][0]]:
                    del server_cnt[sorted_logs[left][0]]
                left += 1

            res[idx] = n - len(server_cnt)

        return res