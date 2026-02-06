class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        currentCapital = w
        projectsMeeetCapital = []
        minCapitalProjects = [(c, -p) for p, c in zip(profits, capital)]
        heapify(minCapitalProjects)

        for _ in range(k):
            while minCapitalProjects and minCapitalProjects[0][0] <= currentCapital:
                _, profit = heappop(minCapitalProjects)
                heappush(projectsMeeetCapital, profit)

            if not projectsMeeetCapital:
                break
                
            maxProfit = heappop(projectsMeeetCapital)
            currentCapital += -maxProfit

        return currentCapital




