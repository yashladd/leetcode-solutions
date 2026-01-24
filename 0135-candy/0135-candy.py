class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        [1, 2, 1, 5, 5, 4, 3, 2]
        """
        N = len(ratings)
        candies = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                candies[i] = 1 + candies[i-1]


        total = candies[N-1]
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], 1 + candies[i + 1])

            total += candies[i]

        return total