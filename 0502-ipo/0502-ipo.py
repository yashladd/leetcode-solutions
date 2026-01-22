class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(c, p) for c, p in zip(capital, profits)]
        projects.sort()
        max_profits = []
        idx = 0
        while k:
            while idx < len(projects) and w >= projects[idx][0]:
                heappush(max_profits, -projects[idx][1])
                idx += 1
            if len(max_profits):
                w -= heappop(max_profits)
            else:
                break
            k -= 1

        return w



        