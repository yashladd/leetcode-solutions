class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        INF = float("inf")
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        N = n1 + n2

        isEven = N % 2 == 0

        lo, hi = 0, n1

        while lo <= hi:
            m1 = (lo + hi) >> 1
            l1, r1 = m1-1, m1
            m2 = (N + 1) // 2 - m1
            l2, r2 = m2-1, m2
            l1 = nums1[l1] if l1 >= 0 else -INF
            r1 = nums1[m1] if r1 < n1 else INF
            l2 = nums2[l2] if l2 >= 0 else -INF
            r2 = nums2[m2] if m2 < n2 else INF

            if l1 <= r2 and l2 <= r1:
                return (max(l1, l2) + min(r1, r2)) / 2 if isEven else max(l1, l2)

            if l1 > r2:
                hi = m1 - 1
            else:
                lo = m1 + 1

        return 0


        