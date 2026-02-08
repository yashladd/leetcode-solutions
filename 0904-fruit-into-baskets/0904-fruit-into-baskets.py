class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = {}
        l = 0
        best = 0
        for r, fruit in enumerate(fruits):
            types[fruit] = 1 + types.get(fruit, 0)
            while len(types) > 2:
                types[fruits[l]] -= 1
                if not types[fruits[l]]:
                    del types[fruits[l]]
                l += 1
            best = max(best, r - l + 1)
        return best