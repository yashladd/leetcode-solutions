class Solution:

    def __init__(self, nums: List[int]):
        self._value_to_idxs = defaultdict(list)
        for i, num in enumerate(nums):
            self._value_to_idxs[num].append(i)    

    def pick(self, target: int) -> int:
        return random.choice(self._value_to_idxs[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)