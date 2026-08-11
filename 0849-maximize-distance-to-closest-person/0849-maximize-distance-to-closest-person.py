class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        prev_occ_pos = -inf
        distance = [inf] * N

        for i in range(N):
            if seats[i]:
                prev_occ_pos = i
                distance[i] = 0
            else:
                distance[i] = i - prev_occ_pos

        prev_occ_pos = inf

        for i in range(N-1, -1, -1):
            if seats[i]:
                prev_occ_pos = i
            else:
                right_distance = prev_occ_pos - i
                distance[i] = min(distance[i], right_distance)

        max_distance = 0

        for i in range(N):
            if not seats[i]:
                max_distance = max(max_distance, distance[i])

        return max_distance


