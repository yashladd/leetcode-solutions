class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        h = []
        for ha in happiness:
            heappush(h, -ha)
        cnt = 0
        while k:
            ha = heappop(h)
            ans += max(0, -ha-cnt)
            cnt += 1
            k -= 1
        return ans
        