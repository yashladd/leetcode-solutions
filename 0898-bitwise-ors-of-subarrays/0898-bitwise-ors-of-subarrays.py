class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev = set()
        curr = set()
        res = set()

        for i, x in enumerate(arr):
            for y in prev:
                curr.add(y | x)
                res.add(y | x)

            curr.add(x)
            res.add(x)
            prev = curr
            curr = set()

        return len(res)