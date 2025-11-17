class Solution:
    def kLengthApart(self, a: List[int], k: int) -> bool:
        n = len(a)
        i = 0
        while True:
            while i < n and a[i] == 0:
                i += 1

            if i >= n-1: return True

            j = i + 1

            while j < n and a[j] == 0:
                j += 1

            if j >= n:
                return True


            if j-i-1 < k:
                return False

            i = j

        return True




        