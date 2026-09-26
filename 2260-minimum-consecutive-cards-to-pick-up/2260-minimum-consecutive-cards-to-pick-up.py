class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        mini = inf

        mp = {}

        for i, v in enumerate(cards):
            if v in mp:
                mini = min(mini, i - mp[v] + 1)
            mp[v] = i

        return -1 if mini == inf else mini