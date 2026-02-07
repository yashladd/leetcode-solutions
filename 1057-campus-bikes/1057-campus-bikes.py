class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        W = len(workers)
        B = len(bikes)
        distances = defaultdict(list)
        for i in range(W):
            for j in range(B):
                d = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                distances[d].append((i, j))

        workers_used = set()
        bikes_used = set()
        bikes = [None] * W

        for d in sorted(distances.keys()):
            for w, b in distances[d]:
                if w not in workers_used and b not in bikes_used:
                    bikes[w] = b
                    workers_used.add(w)
                    bikes_used.add(b)

        return bikes
