class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 3  (4567) 8

        # 4 (5678)
        if low == high:
            return int(low % 2)

        if high - low == 1:
            return 1
        res = 0
        if low % 2:
            res += 1
            rem = (high - low) - 1
            res += rem // 2
        else:
            rem = (high - low) - 1
            res += (rem + 1) // 2
        res += int(high % 2 != 0)
        return res