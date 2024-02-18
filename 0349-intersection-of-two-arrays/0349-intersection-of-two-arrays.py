class Solution:
    def intersection(self, p: List[int], q: List[int]) -> List[int]:
        p.sort()
        q.sort()
        n, m = len(p), len(q)
        ans = []
        i, j = 0, 0
        while i<n and j < m:
            if p[i] < q[j]:
                i += 1
            elif p[i] > q[j]:
                j += 1
            else:
                ans.append(p[i])
                while i < n and p[i] == ans[-1]:
                    i += 1
                while j < m and q[j] == ans[-1]:
                    j += 1
        return ans