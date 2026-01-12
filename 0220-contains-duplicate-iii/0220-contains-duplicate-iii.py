class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0: return False

        win = SortedList()

        for i, n in enumerate(nums):
            if i > k:
                win.remove(nums[i- k - 1])

            """
            For the current number n, we want to know if our SortedList (window) contains any value x such that:
            n - t <= x <= n + t$$
            Method 1: The "One Bisect + Check" (Most Common)You only need bisect_left. You look for the smallest number in the window that is greater than or equal to the lower bound (n - t). Then, you just verify if that specific number is within the upper bound (n + t).Logic:Find position pos = bisect_left(window, n - t).Valid Case: If pos is a valid index AND window[pos] <= n + t, then you found a match.
            """

            pos1 = win.bisect_left(n - t)

            if pos1 >=0 and pos1 < len(win) and win[pos1] <= n + t:
                return True

            win.add(n)

        return False

        