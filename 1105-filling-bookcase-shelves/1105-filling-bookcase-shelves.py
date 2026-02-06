from functools import lru_cache

class Solution:
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)

        @lru_cache(None)
        def f(i):
            if i == n:
                return 0

            best = float("inf")
            width = 0
            max_h = 0

            # try ending the current shelf at j
            for j in range(i, n):
                width += books[j][0]
                if width > shelfWidth:
                    break
                max_h = max(max_h, books[j][1])
                best = min(best, max_h + f(j + 1))

            return best

        return f(0)
