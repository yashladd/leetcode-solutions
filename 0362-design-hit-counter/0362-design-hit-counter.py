class HitCounter:
    def __init__(self):
        # Arrays to store timestamp and hit count for each of the 300 buckets
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        
        if self.times[idx] != timestamp:
            # This bucket holds data from an old cycle (e.g., 300 seconds ago)
            # Reset it for the new timestamp
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            # Same second, just increment count
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            # Sum up hits if the time in the bucket is within the last 300 seconds
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total